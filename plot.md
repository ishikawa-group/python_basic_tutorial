# Making plot with *matplotlib* library

## loading the library
```python
import matplotlib.pyplot as plt
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

plt.tight_layout()
```
