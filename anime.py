from __future__ import print_function
#%matplotlib inline
import argparse
import os
import random
import torch
import torch.nn as nn
import torch.nn.parallel
import torch.backends.cudnn as cudnn
import torch.optim as optim
import torch.utils.data
import torchvision.datasets as dset
import torchvision.transforms as transforms
import torchvision.utils as vutils
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#from IPython.display import HTML

# set random seed for reproducibility
manualSeed = 999
# manualSeed = random.randint(1, 10000)  # use if you want new results
print("Random seed:", manualSeed)
random.seed(manualSeed)
torch.manual_seed(manualSeed)
torch.use_deterministic_algorithms(True)

dataroot = "./images2004"
workers = 0
batch_size = 128
image_size = 64
nc = 3
nz = 100
ngf = 64
ndf = 64
num_epochs = 40  # 40 -> 1000 iterations
lr = 1.0e-4
beta1 = 0.5

dataset = dset.ImageFolder(root=dataroot,
                           transform=transforms.Compose([
                               transforms.Resize(image_size),
                               transforms.CenterCrop(image_size),
                               transforms.ToTensor(),
                               transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                               ]))
dataloader = torch.utils.data.DataLoader(dataset, batch_size=batch_size,
                                         shuffle=True, num_workers=workers)

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

print("device is :", device)

# -- Plot some training images
real_batch = next(iter(dataloader))
plt.figure(figsize=(8, 8))
plt.axis("off")
plt.title("Training images")
#plt.imshow(np.transpose(vutils.make_grid(real_batch[0].to(device)[:64], padding=2, normalize=True).cpu(), (1,2,0)))
# transpose (channel,height,width) -> (height,width,channel)
# numpy.transpose(a, axes = None): so axes=(0,1,2) does nothing (original)
plt.imshow(np.transpose(vutils.make_grid(real_batch[0].to(device)[0:64], normalize=True).cpu(), (1,2,0)))
plt.show()

# customize weights initialization called on netG and netD
# nn.init.normal_ gives normal distribution
def weights_init(m):
    classname = m.__class__.__name__
    if classname.find("Conv") != -1:
        # Conv2d or ConvTransposed2d
        nn.init.normal_(m.weight.data, mean=0.0, std=0.02)
    elif classname.find("BatchNorm") != -1:
        # BatchNorm
        nn.init.normal_(m.weight.data, mean=1.0, std=0.02)
        nn.init.constant_(m.bias.data, 0)

# Generator
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.main = nn.Sequential(
            # input is Z, going into a convolution
            nn.ConvTranspose2d(in_channels=nz, out_channels=ngf*8, kernel_size=4, stride=1, padding=0, bias=False),
            nn.BatchNorm2d(ngf*8),
            nn.ReLU(True),
            # state size: (ngf*8, 4, 4) in (channel, height, width)
            nn.ConvTranspose2d(in_channels=ngf*8, out_channels=ngf*4, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf*4),
            nn.ReLU(True),
            # state size: (ngf*4, 8, 8)
            nn.ConvTranspose2d(in_channels=ngf*4, out_channels=ngf*2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf*2),
            nn.ReLU(True),
            # state size: (ngf*2, 16, 16)
            nn.ConvTranspose2d(in_channels=ngf*2, out_channels=ngf, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ngf),
            nn.ReLU(True),
            # state size: (ngf, 32, 32)
            nn.ConvTranspose2d(in_channels=ngf, out_channels=nc, kernel_size=4, stride=2, padding=1, bias=False),
            nn.Tanh()
            # state size: (nc, 64, 64)
        )

    def forward(self, input):
        return self.main(input)

# create the generator
netG = Generator().to(device)

# apply the weights_init function to randomly initialize all weights to mean = 0, stdev = 0.2
netG.apply(weights_init)

class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.main = nn.Sequential(
            # input is (nc, 64, 64)
            nn.Conv2d(in_channels=nc, out_channels=ndf, kernel_size=4, stride=2, padding=1, bias=False),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (ndf, 32, 32)
            nn.Conv2d(in_channels=ndf, out_channels=ndf*2, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ndf*2),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (ndf*2, 16, 16)
            nn.Conv2d(in_channels=ndf*2, out_channels=ndf*4, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ndf*4),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (ndf*4, 8, 8)
            nn.Conv2d(in_channels=ndf*4, out_channels=ndf*8, kernel_size=4, stride=2, padding=1, bias=False),
            nn.BatchNorm2d(ndf*8),
            nn.LeakyReLU(0.2, inplace=True),
            # state size: (ndf*8, 4, 4)
            nn.Conv2d(in_channels=ndf*8, out_channels=1, kernel_size=4, stride=1, padding=0, bias=False),
            nn.Sigmoid()
        )

    def forward(self, input):
        return self.main(input)

# create the discriminator
netD = Discriminator().to(device)

# apply the weights_init function to randomly initialize all weights to mean = 0 and stdev = 0.2
netD.apply(weights_init)

# initialize BCELoss function
criterion = nn.BCELoss()

# create batch of latent vectors that we will use to visualize the pregress of the generator
fixed_noise = torch.randn(64, nz, 1, 1, device=device)

# establish convention for real and fake labels during training
real_label = 1.0
fake_label = 0.0

# setup Adam optimizers for both G and D
optimizerD = optim.Adam(netD.parameters(), lr=lr, betas=(beta1, 0.999))
optimizerG = optim.Adam(netG.parameters(), lr=lr, betas=(beta1, 0.999))

# training loop

# lists to keep track of progress
img_list = []
G_losses = []
D_losses = []
iters = 0

print("Start training loop ... ")
for epoch in range(num_epochs):
    for i, data in enumerate(dataloader, 0):
        # 1. Update D: maximize log(D)+log(1-D(G))
        ## 1-1. train with all-real batch
        netD.zero_grad()

        ### format batch
        real_cpu = data[0].to(device)
        b_size = real_cpu.size(0)
        label = torch.full((b_size,), real_label, dtype=torch.float, device=device)

        ### forward pass real bathc through D
        output = netD(real_cpu).view(-1)

        ### calculate loss on all-real batch
        errD_real = criterion(output, label)

        ### calculate gradients for D in backward pass
        errD_real.backward()
        D_x = output.mean().item()

        ## 1-2. train with all-fake batch
        ### generate batch of latent vectors
        noise = torch.randn(b_size, nz, 1, 1, device=device)

        ### generate fake image batch with G
        fake = netG(noise)
        label.fill_(fake_label)

        ### classify all fake batch with D
        output = netD(fake.detach()).view(-1)

        ### calculate D's loss on the all-fake batch
        errD_fake = criterion(output, label)

        ### calculate the gradients for this batch, summed with previous gradients
        errD_fake.backward()
        D_G_z1 = output.mean().item()

        ### compute error of D as sum over the fake and the real batches
        errD = errD_real + errD_fake

        ### update D
        optimizerD.step()

        # 2. Update G: maximize log(D(G))
        netG.zero_grad()
        label.fill_(real_label)

        ### perform another forward pass of all-fake batch through D
        output = netD(fake).view(-1)

        ### calculate G's loss based on this output
        errG = criterion(output, label)

        ### calculate gradients for G
        errG.backward()
        D_G_z2 = output.mean().item()

        ### update G
        optimizerG.step()

        # output training stats
        if i % 10 == 0:
            print("[%d/%d][%d/%d]\tLoss_D: %.4f\tLoss_G: %.4f\tD(x): %.4f\tD(G(z)): %.4f / %.4f" % (epoch+1, num_epochs, i, len(dataloader), errD.item(), errG.item(), D_x, D_G_z1, D_G_z2))

        # save losses for plotting
        G_losses.append(errG.item())
        D_losses.append(errD.item())

        # check how the generator is doing by saving G's output on fixed noise
        if (iters % 500 == 0) or ((epoch == num_epochs-1) and (i == len(dataloader)-1)):
            with torch.no_grad():
                fake = netG(fixed_noise).detach().cpu()
            img_list.append(vutils.make_grid(fake, normalize=True))

        iters += 1

plt.figure(figsize=(10, 5))
plt.title("Generator and discriminator loss during training")
plt.plot(G_losses, label="G")
plt.plot(D_losses, label="D")
plt.xlabel("Iterations")
plt.ylabel("Loss")
plt.legend()
plt.show()

# -- capture
#fig = plt.figure(figsize=(8, 8))
#plt.axis("off")
#ims = [[plt.imshow(npn.transpose(i, (1,2,0)), animated=True)] for i in img_list]
#ani = animation.ArtistAnimation(fig, ims, interval=1000, repeat_delay=1000, blit=True)
#HTML(ani.to_jshtml())
#ani.save("sample_anime_new.gif", writer="imagemagick")

# grab a batch of real images from the dataloader
real_batch = next(iter(dataloader))

# plot the real images
plt.figure(figsize=(5, 5))
plt.subplot(1, 2, 1)
plt.axis("off")
plt.title("Real images")
plt.imshow(np.transpose(vutils.make_grid(real_batch[0].to(device)[0:64], normalize=True).cpu(), (1, 2, 0)))

# plot the fake images from the last epoch
plt.subplot(1, 2, 2)
plt.axis("off")
plt.title("Fake images")
plt.imshow(np.transpose(img_list[-1], (1, 2, 0)))
plt.show()

