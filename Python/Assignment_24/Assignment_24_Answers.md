```md
# Assignment 24 — Answers

## Q1. What is a lambda function in Python? How is it different from a normal function?

A **lambda function** is a small, anonymous function defined using the `lambda` keyword. It is generally used when a simple function is needed for a short period of time.

**Syntax:**

```python
lambda arguments: expression
```

**Example:**

```python
square = lambda x: x * x

print(square(5))
```

**Output:**

```text
25
```

### Lambda Function vs Normal Function

| Lambda Function | Normal Function |
|---|---|
| Defined using the `lambda` keyword | Defined using the `def` keyword |
| Usually anonymous | Usually has a name |
| Contains a single expression | Can contain multiple statements |
| Automatically returns the result of the expression | Uses an explicit `return` statement |
| Best suited for short, simple operations | Suitable for complex and reusable logic |

**Normal function:**

```python
def square(x):
    return x * x
```

**Lambda function:**

```python
square = lambda x: x * x
```

Both perform the same operation, but lambda functions are more concise.

---

## Q2. What are the limitations of lambda functions?

Lambda functions are useful for simple operations, but they have several limitations:

1. **Only one expression is allowed.** A lambda cannot contain multiple independent statements.

2. **They are not suitable for complex logic.** If the logic becomes complicated, a normal `def` function is easier to read and maintain.

3. **No explicit statements such as loops or assignments** can be written inside a lambda.

4. **They can reduce readability** when the expression becomes too long or complicated.

5. **They are generally intended for short-lived operations**, such as functions passed to `map()`, `filter()`, and `reduce()`.

For example, this is simple and appropriate:

```python
square = lambda x: x * x
```

But complex logic is better written using `def`:

```python
def calculate_result(x):
    # Multiple steps can be written here
    result = x * 2
    result = result + 10
    return result
```

Therefore, lambda functions should be used when the operation is **small, simple, and easy to understand**.

---

## Q3. Explain the working of the map() function with an example.

The **`map()`** function applies a given function to every element of an iterable and returns a **map iterator** containing the transformed results.

**Syntax:**

```python
map(function, iterable)
```

### Example:

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

**Output:**

```text
[2, 4, 6, 8, 10]
```

### How it works

The lambda function:

```python
lambda x: x * 2
```

is applied to each element:

```text
1 → 2
2 → 4
3 → 6
4 → 8
5 → 10
```

Therefore:

```text
Input  → [1, 2, 3, 4, 5]
             ↓
          map()
             ↓
Output → [2, 4, 6, 8, 10]
```

`map()` returns an iterator, so `list()` is used above to display all results immediately.

---

## Q4. How does map() differ from using a for loop?

Both `map()` and a `for` loop can be used to apply an operation to every element, but they differ in style and usage.

### Using a for loop:

```python
numbers = [1, 2, 3, 4, 5]

result = []

for number in numbers:
    result.append(number * 2)

print(result)
```

### Using map():

```python
numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

### Difference

| `map()` | `for` loop |
|---|---|
| Functional programming style | Procedural/imperative style |
| Applies a function to each element | Gives explicit control over each iteration |
| Returns an iterator | Can directly build or modify collections |
| Concise for simple transformations | Better for complex logic |
| Works well with other functional tools | Easier to understand for beginners and multi-step operations |

For a simple transformation, `map()` can be concise. For complex logic involving multiple statements, conditions, or side effects, a `for` loop is often clearer.

---

## Q5. What is the filter() function and when should it be used?

The **`filter()`** function is used to select elements from an iterable based on a condition.

It applies a function to each element and keeps only the elements for which the function returns a **truthy value**.

**Syntax:**

```python
filter(function, iterable)
```

### Example:

```python
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

**Output:**

```text
[2, 4, 6]
```

Here:

```python
lambda x: x % 2 == 0
```

checks whether each number is even.

```text
1 → False → Removed
2 → True  → Kept
3 → False → Removed
4 → True  → Kept
5 → False → Removed
6 → True  → Kept
```

### When should `filter()` be used?

`filter()` should be used when we want to **select only those elements that satisfy a particular condition**.

For example:

- Selecting even numbers
- Finding students who passed
- Selecting employees with salary above a threshold
- Filtering positive numbers
- Selecting products that are in stock

---

## Q6. Difference between map() and filter().

Both `map()` and `filter()` operate on elements of an iterable, but their purposes are different.

| `map()` | `filter()` |
|---|---|
| Transforms each element | Selects elements based on a condition |
| Function usually returns a transformed value | Function returns a truthy/falsy value |
| Usually produces one output for each input | May produce fewer outputs than inputs |
| Used for data transformation | Used for data selection |
| Example: square every number | Example: select only even numbers |

### Example of map():

```python
numbers = [1, 2, 3, 4]

result = map(lambda x: x * 2, numbers)

print(list(result))
```

**Output:**

```text
[2, 4, 6, 8]
```

### Example of filter():

```python
numbers = [1, 2, 3, 4]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))
```

**Output:**

```text
[2, 4]
```

In simple terms:

```text
map()    → Transform
filter() → Select
```

---

## Q7. What is reduce()? Why is it not a built-in function in Python?

The **`reduce()`** function repeatedly applies a function to the elements of an iterable and combines them into a **single final value**.

In Python 3, `reduce()` is available in the `functools` module rather than being a built-in function.

**Syntax:**

```python
from functools import reduce

reduce(function, iterable)
```

### Example:

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

**Output:**

```text
15
```

The calculation happens conceptually as:

```text
1 + 2 = 3
3 + 3 = 6
6 + 4 = 10
10 + 5 = 15
```

### Why is reduce() not a built-in function?

In Python 3, `reduce()` was moved from the built-in namespace to the `functools` module because it can sometimes make code less readable than alternatives such as:

- `sum()`
- `max()`
- `min()`
- `any()`
- `all()`
- A normal `for` loop

For example:

```python
sum([1, 2, 3, 4, 5])
```

is clearer than:

```python
reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])
```

Therefore, `reduce()` is still available when a **custom reduction operation** is required, but it is not a built-in function in Python 3.

---

## Q8. Explain how reduce() works internally.

`reduce()` processes the elements of an iterable **two at a time** and continuously combines the result with the next element until only one final value remains.

Consider:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers)

print(result)
```

The process is:

```text
Step 1:
x = 1, y = 2
1 + 2 = 3

Step 2:
x = 3, y = 3
3 + 3 = 6

Step 3:
x = 6, y = 4
6 + 4 = 10
```

Final result:

```text
10
```

Conceptually:

```text
[1, 2, 3, 4]
     ↓
  1 + 2 = 3
     ↓
  3 + 3 = 6
     ↓
  6 + 4 = 10
     ↓
    10
```

### Using an initializer

`reduce()` can also accept an optional initial value:

```python
from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y: x + y, numbers, 10)

print(result)
```

**Output:**

```text
20
```

Here, the initial value `10` is used first:

```text
10 + 1 = 11
11 + 2 = 13
13 + 3 = 16
16 + 4 = 20
```

Therefore, `reduce()` gradually reduces multiple values into **one final value**.

---

## Q9. Can lambda functions be used with map, filter, and reduce together? Explain.

**Yes.** Lambda functions are commonly used with `map()`, `filter()`, and `reduce()` because these functions often require a small function as an argument.

For example, suppose we want to:

1. Select even numbers.
2. Square those numbers.
3. Calculate their sum.

```python
from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = filter(lambda x: x % 2 == 0, numbers)

squared_numbers = map(lambda x: x * x, even_numbers)

result = reduce(lambda x, y: x + y, squared_numbers)

print(result)
```

**Output:**

```text
56
```

### Step-by-step:

First, `filter()` selects even numbers:

```text
[2, 4, 6]
```

Then, `map()` squares them:

```text
[4, 16, 36]
```

Finally, `reduce()` adds them:

```text
4 + 16 + 36 = 56
```

The overall flow is:

```text
Original Data
     ↓
  filter()
     ↓
[2, 4, 6]
     ↓
   map()
     ↓
[4, 16, 36]
     ↓
  reduce()
     ↓
   56
```

This demonstrates how functional programming operations can be **chained together** to build a data-processing pipeline.

---

## Q10. When should functional programming be preferred over procedural style in Python?

**Functional programming** should be preferred when the problem can be expressed clearly as a sequence of transformations and selections using functions such as `map()`, `filter()`, comprehensions, and other higher-order functions.

It is especially useful when:

- The operations are simple and independent.
- We want concise data transformations.
- We want to avoid unnecessary mutable state.
- We are processing collections of data.
- We want to compose multiple operations into a pipeline.

### Functional style:

```python
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)
```

### Procedural style:

```python
numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)
```

Both approaches are correct.

However, **functional programming is not always better**. A procedural `for` loop is often more readable when the logic contains multiple steps, complex conditions, error handling, or side effects.

### In simple terms:

```text
Functional style   → Prefer for simple transformations and pipelines
Procedural style   → Prefer for complex, step-by-step logic
```

The best approach in Python is the one that makes the code **clear, readable, maintainable, and easy to understand**.
```