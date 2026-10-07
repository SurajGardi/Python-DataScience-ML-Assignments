```md
# Assignment 25 — Answers

## Q1. What is Object-Oriented Programming?

**Object-Oriented Programming (OOP)** is a programming approach in which software is designed using **objects and classes**. An object represents a real-world entity and contains both **data (attributes)** and **behavior (methods)**.

For example, a `Student` object can have:

```python
Name
Roll Number
Marks
```

and methods such as:

```python
study()
display_details()
calculate_result()
```

### Example:

```python
class Student:
    def display(self):
        print("Student is studying")


student1 = Student()

student1.display()
```

Here:

- `Student` is a **class**.
- `student1` is an **object**.
- `display()` is a **method**.

OOP helps us organize large programs into reusable, modular, and maintainable components.

---

## Q2. What are the four core characteristics of OOP?

The four core characteristics of Object-Oriented Programming are:

### 1. Encapsulation

Encapsulation means **bundling data and the methods that operate on that data into a single unit**, usually a class.

It also helps control access to the internal data of an object.

### 2. Inheritance

Inheritance allows one class to **acquire the properties and methods of another class**.

It promotes code reuse.

### 3. Polymorphism

Polymorphism means **one interface or method name can have different behaviors** depending on the object or context.

For example, different classes can implement the same method differently.

### 4. Abstraction

Abstraction means **hiding unnecessary implementation details and exposing only the essential functionality**.

### Summary:

| OOP Characteristic | Meaning |
|---|---|
| Encapsulation | Bundling data and methods together |
| Inheritance | Reusing properties and methods of another class |
| Polymorphism | Same interface/method can behave differently |
| Abstraction | Hiding implementation details and showing essentials |

These four concepts help make software more **modular, reusable, maintainable, and flexible**.

---

## Q3. Explain class and object with real-world analogy.

A **class** is a blueprint or template used to create objects. An **object** is an actual instance created from that class.

### Real-world analogy: Car

Think of a **car design/blueprint** as a class.

The blueprint defines properties such as:

```text
Color
Model
Engine
Speed
```

and behaviors such as:

```text
start()
stop()
accelerate()
```

The actual cars manufactured using that blueprint are objects.

```text
Class → Car
       ↓
 ┌─────┼─────┐
 ↓     ↓     ↓
Car1  Car2  Car3
```

### Python example:

```python
class Car:
    def start(self):
        print("Car started")


car1 = Car()
car2 = Car()

car1.start()
car2.start()
```

Here:

- `Car` → Class
- `car1` → Object
- `car2` → Object
- `start()` → Method

A class defines the structure and behavior, while objects represent actual instances of that class.

---

## Q4. What is a constructor in Python? Why is __init__() used?

A **constructor** is a special method that is automatically called when an object is created. In Python, `__init__()` is commonly used for **initializing an object's attributes**.

### Example:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Suraj", 85)

print(student1.name)
print(student1.marks)
```

**Output:**

```text
Suraj
85
```

When this statement executes:

```python
student1 = Student("Suraj", 85)
```

Python creates the object and calls:

```python
__init__("Suraj", 85)
```

The `__init__()` method initializes:

```python
self.name
self.marks
```

### Why is __init__() used?

It is used to:

- Initialize instance variables.
- Set the initial state of an object.
- Perform setup required when an object is created.

In Python terminology, `__init__()` is technically an **initializer**, while object creation itself is handled by `__new__()`. However, `__init__()` is commonly referred to as the constructor in beginner-level Python programming.

---

## Q5. Is constructor mandatory in a class? Explain.

**No, defining `__init__()` is not mandatory in a Python class.**

If we do not define `__init__()`, Python can still create objects using the inherited default initialization behavior.

### Example:

```python
class Student:
    def display(self):
        print("Student details")


student1 = Student()

student1.display()
```

**Output:**

```text
Student details
```

The class works even though it does not explicitly define `__init__()`.

However, if we need to initialize instance variables when an object is created, we usually define `__init__()`.

### Example:

```python
class Student:
    def __init__(self, name):
        self.name = name


student1 = Student("Suraj")

print(student1.name)
```

Here, `__init__()` is useful because it initializes the `name` attribute.

Therefore:

```text
__init__() is optional.
```

It is required only when we need custom initialization logic.

---

## Q6. What is a destructor? When is __del__() called?

A **destructor** is a special method associated with the cleanup of an object. In Python, `__del__()` is the method commonly associated with destructor behavior.

### Example:

```python
class Demo:
    def __init__(self):
        print("Object created")

    def __del__(self):
        print("Object cleanup")


obj = Demo()

del obj
```

Possible output:

```text
Object created
Object cleanup
```

When:

```python
del obj
```

is executed, the reference named `obj` is removed. If that was the object's last reference, the object may become eligible for destruction and `__del__()` may be called.

### Important point

`__del__()` is **not guaranteed to run at a predictable time**. Python uses garbage collection and reference counting, and the exact timing can depend on the implementation and situation.

Therefore, `__del__()` should generally **not be relied upon for important resource cleanup** such as closing files or database connections. Context managers (`with`) or explicit cleanup methods are preferred for such resources.

---

## Q7. Difference between constructor and destructor.

A constructor/initializer and destructor serve opposite purposes in an object's lifecycle.

| Constructor / Initializer | Destructor |
|---|---|
| Commonly implemented using `__init__()` | Commonly implemented using `__del__()` |
| Initializes an object | Associated with final cleanup of an object |
| Called during object initialization | May be called when the object is about to be destroyed |
| Used to initialize attributes | Can be used for cleanup-related actions |
| Normally executes when an object is created | Execution timing is not deterministic |
| Commonly used in Python programs | Should not be relied upon for critical resource cleanup |

### Example:

```python
class Demo:
    def __init__(self):
        print("Initialization")

    def __del__(self):
        print("Cleanup")


obj = Demo()

del obj
```

Conceptually:

```text
Object creation
       ↓
   __init__()
       ↓
 Object exists
       ↓
Object becomes unreachable
       ↓
   __del__() may run
```

---

## Q8. What are instance variables and class variables?

### Instance Variables

Instance variables are variables that belong to a **specific object**. Each object can have its own value.

They are usually created using `self`.

### Example:

```python
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Suraj", 85)
student2 = Student("Rahul", 90)

print(student1.name)
print(student2.name)
```

Here:

```text
student1.name → Suraj
student2.name → Rahul
```

Each object has its own `name` and `marks`.

### Class Variables

Class variables belong to the **class itself** and are shared by instances unless an instance creates/overrides an attribute with the same name.

### Example:

```python
class Student:
    college = "Fergusson College"

    def __init__(self, name):
        self.name = name


student1 = Student("Suraj")
student2 = Student("Rahul")

print(student1.college)
print(student2.college)
```

Both objects can access the same class variable:

```text
Fergusson College
Fergusson College
```

### Difference:

| Instance Variable | Class Variable |
|---|---|
| Belongs to an individual object | Belongs to the class |
| Usually defined using `self` | Defined directly inside the class |
| Each object can have a different value | Shared by instances by default |
| Example: `self.name` | Example: `college` |

---

## Q9. Explain instance methods, class methods, and static methods.

Python supports three commonly used types of methods:

### 1. Instance Method

An instance method operates on a particular object and receives the object as its first parameter, conventionally named `self`.

```python
class Student:
    def display(self):
        print("Student details")


student1 = Student()
student1.display()
```

Here, `display()` is an instance method.

---

### 2. Class Method

A class method operates on the **class itself** and receives the class as its first parameter, conventionally named `cls`.

It is created using the `@classmethod` decorator.

```python
class Student:
    college = "Fergusson College"

    @classmethod
    def display_college(cls):
        print(cls.college)


Student.display_college()
```

Here, `cls` refers to the `Student` class.

Class methods are commonly used when a method needs to access or modify class-level data.

---

### 3. Static Method

A static method does not automatically receive either the instance (`self`) or the class (`cls`).

It is created using the `@staticmethod` decorator.

```python
class Calculator:

    @staticmethod
    def add(a, b):
        return a + b


print(Calculator.add(10, 20))
```

**Output:**

```text
30
```

The method does not depend on any particular object or class state.

### Comparison:

| Method | First Parameter | Works With | Decorator |
|---|---|---|---|
| Instance Method | `self` | Object/instance data | None |
| Class Method | `cls` | Class data | `@classmethod` |
| Static Method | None | Independent logic | `@staticmethod` |

---

## Q10. Why do we use @classmethod and @staticmethod decorators?

The `@classmethod` and `@staticmethod` decorators tell Python how a method should behave when it is defined inside a class.

### @classmethod

`@classmethod` is used when a method needs to work with **class-level data** or perform an operation related to the class.

It automatically receives the class as `cls`.

### Example:

```python
class Student:
    college = "Fergusson College"

    @classmethod
    def change_college(cls, name):
        cls.college = name


Student.change_college("ABC College")

print(Student.college)
```

**Output:**

```text
ABC College
```

Here, `cls` refers to the `Student` class, so the class variable can be modified.

---

### @staticmethod

`@staticmethod` is used when a method is logically related to a class but **does not need access to instance or class data**.

### Example:

```python
class Calculator:

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.multiply(5, 4))
```

**Output:**

```text
20
```

The method does not require `self` or `cls`.

### In simple terms:

```text
@classmethod
     ↓
Works with class-level data
     ↓
Receives cls

@staticmethod
     ↓
Independent utility logic inside a class
     ↓
Receives neither self nor cls
```

Therefore, these decorators make the **intention and behavior of methods explicit**, improving the organization and readability of object-oriented Python code.
```