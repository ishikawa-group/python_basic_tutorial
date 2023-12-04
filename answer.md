## variable
<p id="variable"></p>

```python{cmd}
x = 4
y = 7

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

print(addition)
print(subtraction)
print(multiplication)
print(division)
```

## control
<p id="control"></p>
```python{cmd}
x = 2
y = 1
if x > y:
    print("x is greater than y")
else:
    print("y is greater than or equal to x")
```
```python{cmd}
a = [0, 1, 2, 3, 4]
for i in a:
    print(i)
b = ["John", "Paul", "George, H.", "Ringo", "George, M."]
for i in b:
    print(i)
```

## dict
<p id="dict"></p>

```python{cmd}
# Create a dictionary representing a person
person = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Access specific elements in the dictionary
print("Name:", person['name'])
print("Age:", person['age'])
print("City:", person['city'])
```