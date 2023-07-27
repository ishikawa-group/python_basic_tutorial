# Making plot with *matplotlib* library
* To make a simple plot like line plot, curve plot etc., *matplotlib* is helpful for you.
* In this chapter, we'll look at the basic usage of matplotlib, then also see a similar library *seaborn* which makes cooler plot.

# Matplotlib
## loading the library
```python
import matplotlib.pyplot as plt
```

## basic example
```python
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
y = np.cos(x)

plt.plot(x,y)
plt.xlabel("x")
plt.ylabel("f = cos(x)")
plt.show()
```

## limits
```python
plt.xlim([-2, 2])
plt.ylim([0, 10])
```

## plot
```python
plt.plot(x, y)
plt.show()
# plt.savefig()
```

## label
```python
plt.xlabel("xlabel")
plt.ylabel("ylabel")
```

## ticks
```python
plt.xticks(np.arange(0, 2+0.1, 9.5))
```

## figure configuration
```python
plt.rcParams["font.family"] = "Arial"
plt.rcParams["font.size"] = 16
plt.rcParams["xtick.direction"] = "out"
plt.rcParams["ytick.direction"] = "out"
plt.rcParams['xtick.major.width'] = 1.2
plt.rcParams['ytick.major.width'] = 1.2
plt.rcParams['axes.linewidth'] = 1.2

# controling the figure size and dpi
fig = plt.figure(figsize=(16, 9), dpi=120)

plt.tight_layout()
```

# seaborn
## loading the library
```python
import seaborn as sns
```
