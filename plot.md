# Making a plot in python
* To make a simple plot like line plot, curve plot etc., *matplotlib* is helpful for you.
* In this chapter, we'll look at the basic usage of matplotlib, then also see a similar library *seaborn* which makes cooler plot.

## matplotlib
### loading the library
```python
import matplotlib.pyplot as plt
```

### example
```python {cmd}
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2*np.pi, 2*np.pi, 100)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f = cos(x)")
plt.show()
```

### setting limits
```python
plt.xlim([-2, 2])
plt.ylim([0, 10])
```

### setting labels
```python
plt.xlabel("xlabel")
plt.ylabel("ylabel")
```

### setting ticks
```python
plt.xticks(np.arange(0, 2+0.1, 9.5))
```

## Figure and Axes
* In matplotlib, there are two ways to make plots.
* One is use `plt.plot()`, which is shown above. This is in similar way to MATLAB (actually MATplotlib means MATLAB-like plot library).
* Another way to plot is use `Figure` and `Axes` objects. `Figure` controls the figure part, and `Axes` controls the axes part of each figure.
* This is more advanced, but I recommend to use it because it enables finer control of the figure.

### example
```python {cmd}
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

fig, ax = plt.subplots()

ax.plot(x, y)
plt.show()
```

### setting limits
```python
ax.set_xlim([0, 1])
ax.set_xlim([0, 1])
```
### setting labels
```python
ax.set_xlabel("x")
ax.set_ylabel("y = sin(x)")
ax.set_title("sine curve")
```

### bar plot
```python {cmd}
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1, 6)
y = np.array([83, 32, 54, 22, 78])

fig, ax = plt.subplots()
ax.bar(x, y)

plt.show()
```

### histogram
```python {cmd}
import numpy as np
import matplotlib.pyplot as plt

values = 10.0 * np.random.randn(100) + 100

fig, ax = plt.subplots()
ax.hist(values, bins=10, ec="k")

plt.show()
```

### displaying image
```python {cmd}
import matplotlib.pyplot as plt

img = plt.imread("image.jpg")
fig, ax = plt.subplots()
ax.imshow(img)

plt.show()
```

### figure configuration
```python {cmd}
import numpy as np
import matplotlib.pyplot as plt

# setting font family
plt.rcParams["font.family"] = "Arial"

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

# controling the figure size and dpi
fig, ax = plt.subplots(figsize=(10, 6), dpi=120)

ax.plot(x, y)

# set x and y labels
ax.set_xlabel("x-axis", fontsize=16)
ax.set_ylabel("y = sin(x)", fontsize=16)

# when changing font size
## old ticklabels
xticklabel = ax.get_xticklabels()
yticklabel = ax.get_yticklabels()

## new ticklabels
ax.set_xticklabels(labels=xticklabel, fontsize=16)
ax.set_yticklabels(labels=yticklabel, fontsize=16)

# adjusting tick parameters
ax.tick_params(direction="in", length=10, width=1)

plt.tight_layout()
plt.show()
```

# seaborn
## loading the library
```python
import seaborn as sns
```
