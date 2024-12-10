import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy

# Hyperparameters
latent_size = 100
hidden_size = 256
image_size = 28 * 28
num_epochs = 3
batch_size = 32
learning_rate = 0.0002

# MNIST dataset
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])

train_dataset = torchvision.datasets.MNIST(
    root="./data", train=True, transform=transform, download=True)
train_loader = torch.utils.data.DataLoader(
    dataset=train_dataset, batch_size=batch_size, shuffle=True)

# Generator model
class Generator(nn.Module):
    def __init__(self):
        super(Generator, self).__init__()
        self.fc1 = nn.Linear(latent_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, image_size)
    
    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = F.sigmoid(x)
        return x

# Discriminator model
class Discriminator(nn.Module):
    def __init__(self):
        super(Discriminator, self).__init__()
        self.fc1 = nn.Linear(image_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 1)
    
    def forward(self, x):
        x = x.view(-1, image_size)
        x = self.fc1(x)
        x = torch.relu(x)
        x = self.fc2(x)
        x = torch.sigmoid(x)
        return x

# Initialize models
generator = Generator()
discriminator = Discriminator()

# Loss function and optimizers
criterion = nn.BCELoss()
optimizer_g = torch.optim.Adam(generator.parameters(), lr=learning_rate)
optimizer_d = torch.optim.Adam(discriminator.parameters(), lr=learning_rate)

# Training the GAN
for epoch in range(num_epochs):
    for i, (images, _) in enumerate(train_loader):

        # Generate random latent vectors
        z = torch.randn(batch_size, latent_size)
        
        # Generator forward and backward
        fake_images = generator(z)
        g_loss = criterion(discriminator(fake_images), torch.ones(batch_size, 1))
        
        optimizer_g.zero_grad()
        g_loss.backward()
        optimizer_g.step()
        
        # Discriminator forward and backward for real images
        real_images = images.view(-1, image_size)
        real_labels = torch.ones(batch_size, 1)
        d_real_loss = criterion(discriminator(real_images), real_labels)
        
        # Discriminator forward and backward for fake images
        fake_labels = torch.zeros(batch_size, 1)
        d_fake_loss = criterion(discriminator(fake_images.detach()), fake_labels)
        
        d_loss = d_real_loss + d_fake_loss
        
        optimizer_d.zero_grad()
        d_loss.backward()
        optimizer_d.step()
        
        if (i+1) % 100 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], "
                  f"D_loss: {d_loss.item():.4f}, G_loss: {g_loss.item():.4f}")

# Generate and visualize fake images
z = torch.randn(10, latent_size)
fake_images = generator(z)
fake_images = fake_images.view(-1, 28, 28).detach().numpy()

plt.figure(figsize=(8, 4))
for i in range(10):
    plt.subplot(2, 5, i+1)
    plt.imshow(fake_images[i], cmap='gray')
    plt.axis('off')
plt.tight_layout()
plt.show()