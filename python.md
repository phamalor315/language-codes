<h1>Python</h1>

<h2>Python roll a 1 to 6</h2>

```python
import random

class RandomNumber:
    def __init__(self):
        self.number = 0

    def generate_random_number(self):
        self.number = random.randint(1, 6)
        return self.number

    def random_button(self):
        print("Random number generated:", self.generate_random_number())

# Example usage
if __name__ == '__main__':
    random_number_generator = RandomNumber()
    random_number_generator.random_button()
```

prompt: ***python code to number and random 1 to 6 max, random button,***

<h2>Python random seed/id</h2>

```python
import random

def generate_random_number():
    return random.randint(1, 1000000000000)

# Example usage
if __name__ == '__main__':
    random_number = generate_random_number()
    print(random_number)
```
prompt: ***python code to number random 1 to 1000000000000, random button number***

<h2>Python roll a die</h2>

```python
import random

def roll_dice():
    return random.randint(1, 6)

# Example of rolling the dice
result = roll_dice()
print(f'You rolled a {result}')
```
prompt: ***python code roll a dice 1 to 6 random button, python import random 1 to 6,***
