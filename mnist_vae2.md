```python {cmd}
# PyTorch
import torch
import torch.nn as nn
import torch.nn.functional as F
 
# PyTorch画像用
import torchvision
import torchvision.transforms as transforms
 
# 画像表示用
import matplotlib.pyplot as plt

batch_size = 256
 
# データセットの取得
train_dataset = torchvision.datasets.MNIST(
    root='./data',
    train=True,
    transform=transforms.ToTensor(),
    download=True,
)
# DataLoaderの作成
train_loader = torch.utils.data.DataLoader(
    dataset=train_dataset,
    batch_size=batch_size,
    shuffle=True,
    num_workers=0
)


class Encoder(nn.Module):
  def __init__(self, input_dim, hidden_dim, latent_dim):
    super(Encoder, self).__init__()
    self.fc = nn.Linear(input_dim, hidden_dim)
    self.fc_mu = nn.Linear(hidden_dim, latent_dim)
    self.fc_var = nn.Linear(hidden_dim, latent_dim)

  def forward(self, x):
    # ニューラルネットワークで事後分布の平均・分散を計算する
    h = torch.relu(self.fc(x))
    mu = self.fc_mu(h) # μ
    log_var = self.fc_var(h) # log σ^2

    # 潜在変数を求める
    ## 標準正規乱数を振る
    eps = torch.randn_like(torch.exp(log_var))
    ## 潜在変数の計算 μ + σ・ε
    z = mu + torch.exp(log_var / 2) * eps
    return mu, log_var, z


class Decoder(nn.Module):
  def __init__(self, input_dim, hidden_dim, latent_dim):
    super(Decoder, self).__init__()
    self.fc = nn.Linear(latent_dim, hidden_dim)
    self.fc_output = nn.Linear(hidden_dim, input_dim)

  def forward(self, z):
      h = torch.relu(self.fc(z))
      output = torch.sigmoid(self.fc_output(h))
      return output

class VAE(nn.Module):
  def __init__(self, input_dim, hidden_dim, latent_dim):
    super(VAE, self).__init__()
    self.encoder = Encoder(input_dim, hidden_dim, latent_dim)
    self.decoder = Decoder(input_dim, hidden_dim, latent_dim)

  def forward(self, x):
    mu, log_var, z = self.encoder(x) # エンコード
    x_decoded = self.decoder(z) # デコード
    return x_decoded, mu, log_var, z


def loss_function(label, predict, mu, log_var):
  reconstruction_loss = F.binary_cross_entropy(predict, label, reduction='sum')
  kl_loss = - 0.5 * torch.sum(1 + log_var - mu.pow(2) - log_var.exp())
  vae_loss = reconstruction_loss + kl_loss
  return vae_loss, reconstruction_loss, kl_loss


image_size = 28 * 28
h_dim = 32
z_dim = 16
num_epochs = 5
learning_rate = 1e-3

device = "cpu"

model = VAE(image_size, h_dim, z_dim).to(device)
optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

losses = []
model.train()
for epoch in range(num_epochs):
  train_loss = 0
  for i, (x, labels) in enumerate(train_loader):
    # 予測
    x = x.to(device).view(-1, image_size).to(torch.float32)
    x_recon, mu, log_var, z = model(x)
    # 損失関数の計算
    loss, recon_loss, kl_loss = loss_function(x, x_recon, mu, log_var)

    # パラメータの更新
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    # 損失の表示
    if (i+1) % 10 == 0:
      print(f'Epoch: {epoch+1}, loss: {loss: 0.4f}, reconstruct loss: {recon_loss: 0.4f}, KL loss: {kl_loss: 0.4f}')
    losses.append(loss)

model.eval()

with torch.no_grad():
  z = torch.randn(25, z_dim).to(device)
  out = model.decoder(z)
out = out.view(-1, 28, 28)
out = out.cpu().detach().numpy()

fig, ax = plt.subplots(nrows=5, ncols=5, figsize=(10, 10))
plt.gray()
for i in range(25):
  idx = divmod(i, 5)
  ax[idx].imshow(out[i])
  ax[idx].axis('off');
fig.show()
```
