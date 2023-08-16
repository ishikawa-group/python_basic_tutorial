import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torchvision
import torchvision.transforms as transforms

import numpy as np
import matplotlib.pyplot as plt

train_dataset = torchvision.datasets.MNIST(root="./data",
                                            train=True, transform=transforms.ToTensor(),
                                            download=True)

test_dataset  = torchvision.datasets.MNIST(root="./data",
                                            train=False, transform=transforms.ToTensor(),
                                            download=True)

batch_size = 256

train_loader = torch.utils.data.DataLoader(dataset=train_dataset,
                                            batch_size=batch_size,
                                            shuffle=True)

test_loader  = torch.utils.data.DataLoader(dataset=test_dataset,
                                            batch_size=batch_size,
                                            shuffle=False)

num_classes = 10

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.fc1 = nn.Linear(28*28, 1024)
        self.fc2 = nn.Linear(1024, 512)
        self.fc3 = nn.Linear(512, num_classes)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x


device = "cuda" if torch.cuda.is_available() else "cpu"
model = Net().to(device)

criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)

def train_fn(model, train_loader, criterion, optimizer, device="cpu"):
    train_loss = 0.0
    num_train = 0

    model.train()

    for i, (images, labels) in enumerate(train_loader):
        num_train += len(labels)

        images, labels = images.view(-1, 28*28).to(device), labels.to(device)

        optimizer.zero_grad()

        outputs = model(images)

        loss = criterion(outputs, labels)

        loss.backward()

        optimizer.step()

        train_loss += loss.item()

    train_loss = train_loss/num_train

    return train_loss

def valid_fn(model, train_loader, criterion, optimizer, device="cpu"):
    valid_loss = 0.0
    num_valid = 0

    model.eval()

    with torch.no_grad():
        for i, (images, labels) in enumerate(test_loader):
            num_valid += len(labels)
            images, labels = images.view(-1, 28*28).to(device), labels.to(device)
            outputs = model(images)
            loss = criterion(outputs, labels)
            valid_loss += loss.item()

        valid_loss = valid_loss / num_valid

    return valid_loss

def run(model, train_loader, test_loader, criterion, optimizer, device="cpu"):
    train_loss_list = []
    valid_loss_list = []

    for epoch in range(num_epochs):
        _train_loss = train_fn(model, train_loader, criterion, optimizer, device=device)
        _valid_loss = valid_fn(model, train_loader, criterion, optimizer, device=device)

        print(f"Epoch [{epoch+1}], train_loss: {_train_loss:.5f}, val_loss: {_valid_loss:.5f}")

        train_loss_list.append(_train_loss)
        valid_loss_list.append(_valid_loss)

    return train_loss_list, valid_loss_list


num_epochs = 5
train_loss_list, test_loss_list = run(model, train_loader, test_loader, criterion, optimizer, device=device)

fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(range(len(train_loss_list)), train_loss_list, c="b", label="train loss")
ax.plot(range(len(test_loss_list)), test_loss_list, c="r", label="test loss")

ax.set_xlabel("epoch", fontsize=20)
ax.set_ylabel("loss", fontsize=20)
ax.set_title("training and validation loss", fontsize=20)
ax.grid()
ax.legend(fontsize=20)

plt.show()

image, label = test_dataset[1]
image = image.view(-1, 28*28).to(device)

prediction_label = torch.argmax(model(image))

fig, ax = plt.subplots()
ax.imshow(image.detach().to("cpu").numpy().reshape(28, 28), cmap="gray")

ax.axis("off")
ax.set_title(f"True label : {label}, Prediction : {prediction_label}", fontsize=20)

plt.show()

