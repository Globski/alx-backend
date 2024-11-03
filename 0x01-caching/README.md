# Alx Backend - Caching

## Description

This project focuses on different caching algorithms and their implementation in Python. You will implement different caching algorithms by creating classes that inherit from a base caching class `BaseCaching`. You'll learn how to manage cache data using different strategies such as FIFO, LIFO, LRU, MRU and LFU. You will learn how to choose the appropriate strategy based on your application's performance and memory management requirements.
At the end of this project, you will have a solid understanding of different caching strategies and their use cases.

## Project Structure

| Task                           | Description                                                                                                          | Source Code              |
|--------------------------------|----------------------------------------------------------------------------------------------------------------------|--------------------------|
| **0. Basic dictionary**        | Create a class `BasicCache` that inherits from `BaseCaching` and implements basic caching functionality.            | [0-basic_cache.py](0-basic_cache.py) |
| **1. FIFO caching**            | Create a class `FIFOCache` that inherits from `BaseCaching` and implements FIFO caching.                            | [1-fifo_cache.py](1-fifo_cache.py)   |
| **2. LIFO Caching**            | Create a class `LIFOCache` that inherits from `BaseCaching` and implements LIFO caching.                            | [2-lifo_cache.py](2-lifo_cache.py)    |
| **3. LRU Caching**             | Create a class `LRUCache` that inherits from `BaseCaching` and implements LRU caching.                              | [3-lru_cache.py](3-lru_cache.py)      |
| **4. MRU Caching**             | Create a class `MRUCache` that inherits from `BaseCaching` and implements MRU caching.                              | [4-mru_cache.py](4-mru_cache.py)      |
| **5. LFU Caching**             | Create a class `LFUCache` that inherits from `BaseCaching` and implements LFU caching.                              | [100-lfu_cache.py](100-lfu_cache.py)   |

## Environment
- Ubuntu 18.04 LTS
- Python 3.7
- pycodestyle style (version 2.5)

## Learning Objectives

By completing this project, you should be able to explain:

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

## Prototype Table

| Class Name    | Method Name | Description                                             |
|---------------|-------------|---------------------------------------------------------|
| `BaseCaching` | `put`       | Add an item to the cache.                               |
| `BaseCaching` | `get`       | Retrieve an item from the cache by key.                |
| `BasicCache`  | `put`       | Implemented for basic caching without limits.          |
| `BasicCache`  | `get`       | Retrieve items without limitations.                     |
| `FIFOCache`   | `put`       | Implement FIFO cache; discard the first added item.    |
| `FIFOCache`   | `get`       | Retrieve items using FIFO logic.                        |
| `LIFOCache`   | `put`       | Implement LIFO cache; discard the last added item.     |
| `LIFOCache`   | `get`       | Retrieve items using LIFO logic.                        |
| `LRUCache`    | `put`       | Implement LRU cache; discard the least recently used item. |
| `LRUCache`    | `get`       | Retrieve items using LRU logic.                         |
| `MRUCache`    | `put`       | Implement MRU cache; discard the most recently used item. |
| `MRUCache`    | `get`       | Retrieve items using MRU logic.                         |
| `LFUCache`    | `put`       | Implement LFU cache; discard the least frequently used item. |
| `LFUCache`    | `get`       | Retrieve items using LFU logic.                         |

## How to Use

### Step 1: Implement Caching Classes
You need to implement the following caching classes according to the specifications provided:

#### Caching Algorithms

1. **FIFO (First In, First Out)**
2. **LIFO (Last In, First Out)**
3. **LRU (Least Recently Used)**
4. **MRU (Most Recently Used)**
5. **LFU (Least Frequently Used)**

Each class should inherit from the provided `BaseCaching` class and implement the `put` and `get` methods according to the specified caching strategy.

### Step 2: Testing Your Implementations
You will find several main files for testing each caching algorithm. Each main file provides a series of test cases to demonstrate how the caching algorithms behave.

1. **Navigate to the Project Directory**:
   Open your terminal and navigate to the directory where you have saved the project files.

2. **Run the Test Files**:
   Execute each main file using Python. For example:
   ```bash
   ./0-main.py  # For BasicCache
   ./1-main.py  # For FIFOCache
   ./2-main.py  # For LIFOCache
   ./3-main.py  # For LRUCache
   ./4-main.py  # For MRUCache
   ./100-main.py  # For LFUCache
   ```

   Each script will instantiate the corresponding caching class and run a series of tests to demonstrate how items are added to the cache and how the cache behaves when it exceeds its capacity.

## BaseCaching Class

Here’s the provided `BaseCaching` class that you will extend:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```
### Important Notes
- Ensure that you handle cases where the key does not exist in the cache. The `get` method should return `None` in such cases.
- Each class must properly implement its specific caching strategy, particularly regarding the eviction of items when the cache exceeds its maximum capacity defined in `BaseCaching.MAX_ITEMS`.
- Pay attention to the output of the `print_cache()` method to visualize the current state of the cache after various operations.

## Additional Notes
**What is Caching?**  
Caching is a technique used to store frequently accessed data in a way that can be quickly retrieved. This reduces the time it takes to access data, significantly improving performance in applications.

**Why Caching Matters**  
Understanding caching mechanisms is crucial for software development, as it helps enhance application performance and manage memory effectively.

### What a Caching System Is
A caching system stores frequently accessed data in a temporary storage area (the cache) to speed up data retrieval and improve application performance. It reduces the time it takes to access data by keeping a copy close to where it’s needed.

### What FIFO Means
**FIFO** (First In, First Out) is a caching strategy where the oldest data in the cache is removed first when the cache reaches its capacity. It operates like a queue, where the first item added is the first one to be evicted.

### What LIFO Means
**LIFO** (Last In, First Out) is a caching strategy where the most recently added data is removed first. It operates like a stack, meaning the last item added is the first one to be evicted.

### What LRU Means
**LRU** (Least Recently Used) is a caching strategy that evicts the least recently accessed data first. This method is based on the idea that data that hasn't been used in a while is less likely to be needed in the future.

### What MRU Means
**MRU** (Most Recently Used) is a caching strategy that evicts the most recently accessed data first. It assumes that recently accessed items will be less likely to be accessed again soon.

### What LFU Means
**LFU** (Least Frequently Used) is a caching strategy that evicts the data that has been accessed the least often. This strategy tracks how often each item is accessed and removes the least frequently used ones when the cache is full.

### What the Purpose of a Caching System Is
The purpose of a caching system is to enhance application performance by minimizing data access times, reducing load on data sources, and improving overall efficiency by storing and reusing previously fetched data.

### What Limits a Caching System Has
Caching systems have several limitations, including:
- **Memory Constraints:** The cache size is limited, which can lead to data eviction.
- **Staleness:** Cached data can become outdated if not properly managed.
- **Overhead:** Maintaining the cache can introduce additional complexity and overhead.
- **Not Suitable for All Data:** Some data may not benefit from caching due to high variability or infrequent access patterns.

## Tasks

0. **Basic dictionary**  
   Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:
   - You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
   - This caching system doesn’t have limit.
   - `def put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If key or item is `None`, this method should not do anything.
   - `def get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### Class: `BasicCache`

The `BasicCache` class implements a simple caching mechanism without any limits. It allows storing and retrieving items using a dictionary.

#### Methods:

- **`put(key, item)`**: Adds the item to the cache under the specified key. If either key or item is `None`, the method does nothing.
  
- **`get(key)`**: Retrieves the item associated with the specified key. Returns `None` if the key is not found or if the key is `None`.

```python
guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
```

1. **FIFO caching**  
   Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system:
   - You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
   - You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
   - `def put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If key or item is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, you must discard the first item put in cache (FIFO algorithm) and print `DISCARD:` with the key discarded followed by a new line.
   - `def get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### Class: `FIFOCache`

The `FIFOCache` class implements the First In, First Out (FIFO) caching strategy. It automatically discards the oldest item when the cache exceeds its maximum size.

#### Methods:

- **`put(key, item)`**: Adds the item to the cache. If the cache exceeds `MAX_ITEMS`, the oldest item is discarded, and a message is printed.
  
- **`get(key)`**: Retrieves the item associated with the specified key.
```python
guillaume@ubuntu:~/0x01$ cat 1-main.py
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./1-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
DISCARD: B
Current cache:
C: Street
D: School
E: Battery
F: Mission
guillaume@ubuntu:~/0x01$
```
2. **LIFO Caching**  
   Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system:
   - You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
   - You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
   - `def put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If key or item is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, you must discard the last item put in cache (LIFO algorithm) and print `DISCARD:` with the key discarded followed by a new line.
   - `def get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### Class: `LIFOCache`

The `LIFOCache` class implements the Last In, First Out (LIFO) caching strategy. It discards the most recently added item when the cache exceeds its maximum size.

#### Methods:

- **`put(key, item)`**: Adds the item to the cache. If the cache exceeds `MAX_ITEMS`, the most recently added item is discarded, and a message is printed.
  
- **`get(key)`**: Retrieves the item associated with the specified key.
```python
guillaume@ubuntu:~/0x01$ cat 2-main.py
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./2-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
DISCARD: D
Current cache:
A: Hello
B: World
C: Holberton
E: Battery
Current cache:
A: Hello
B: World
C: Street
E: Battery
DISCARD: C
Current cache:
A: Hello
B: World
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
B: World
E: Battery
G: San Francisco
guillaume@ubuntu:~/0x01$
```
3. **LRU Caching**  
   Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system:
   - You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
   - You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
   - `def put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If key or item is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, you must discard the least recently used item (LRU algorithm) and print `DISCARD:` with the key discarded followed by a new line.
   - `def get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### Class: `LRUCache`

The `LRUCache` class implements the Least Recently Used (LRU) caching strategy. It discards the least recently accessed item when the cache exceeds its maximum size.

#### Methods:

- **`put(key, item)`**: Adds the item to the cache. If the cache exceeds `MAX_ITEMS`, the least recently used item is discarded, and a message is printed.
  
- **`get(key)`**: Retrieves the item associated with the specified key.
```python
guillaume@ubuntu:~/0x01$ cat 3-main.py
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./3-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: B
Current cache:
C: Street
F: Mission
G: San Francisco
H: H
DISCARD: C
Current cache:
F: Mission
G: San Francisco
H: H
I: I
DISCARD: F
Current cache:
G: San Francisco
H: H
I: I
J: J
DISCARD: G
Current cache:
H: H
I: I
J: J
K: K
guillaume@ubuntu:~/0x01$
```

4. **MRU Caching**  
   Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system:
   - You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
   - You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
   - `def put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If key or item is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, you must discard the most recently used item (MRU algorithm) and print `DISCARD:` with the key discarded followed by a new line.
   - `def get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### Class: `MRUCache`

The `MRUCache` class implements the Most Recently Used (MRU) caching strategy. It discards the most recently accessed item when the cache exceeds its maximum size.

#### Methods:

- **`put(key, item)`**: Adds the item to the cache. If the cache exceeds `MAX_ITEMS`, the most recently used item is discarded, and a message is printed.
  
- **`get(key)`**: Retrieves the item associated with the specified key.
```python
guillaume@ubuntu:~/0x01$ cat 4-main.py
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./4-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: B
Current cache:
A: Hello
C: Holberton
D: School
E: Battery
Current cache:
A: Hello
C: Street
D: School
E: Battery
Hello
None
Street
DISCARD: C
Current cache:
A: Hello
D: School
E: Battery
F: Mission
DISCARD: F
Current cache:
A: Hello
D: School
E: Battery
G: San Francisco
DISCARD: G
Current cache:
A: Hello
D: School
E: Battery
H: H
DISCARD: H
Current cache:
A: Hello
D: School
E: Battery
I: I
DISCARD: I
Current cache:
A: Hello
D: School
E: Battery
J: J
DISCARD: J
Current cache:
A: Hello
D: School
E: Battery
K: K
guillaume@ubuntu:~/0x01$
```

5. **LFU Caching**  
   Create a class `LFUCache` that inherits from `BaseCaching` and is a caching system:
   - You must use `self.cache_data` - dictionary from the parent class `BaseCaching`.
   - You can overload `def __init__(self):` but don’t forget to call the parent init: `super().__init__()`.
   - `def put(self, key, item)`: Must assign to the dictionary `self.cache_data` the item value for the key `key`. If key or item is `None`, this method should not do anything. If the number of items in `self.cache_data` is higher than `BaseCaching.MAX_ITEMS`, you must discard the least frequently used item (LFU algorithm). If you find more than 1 item to discard, you must use the LRU algorithm to discard only the least recently used, and print `DISCARD:` with the key discarded followed by a new line.
   - `def get(self, key)`: Must return the value in `self.cache_data` linked to `key`. If key is `None` or if the key doesn’t exist in `self.cache_data`, return `None`.

### Class: `LFUCache`

The `LFUCache` class implements the Least Frequently Used (LFU) caching strategy. It discards the least frequently used item when the cache exceeds its maximum size. If multiple items have the same frequency, it uses LRU to decide which one to discard.

#### Methods:

- **`put(key, item)`**: Adds the item to the cache. If the cache exceeds `MAX_ITEMS`, the least frequently used item is discarded based on LFU, and a message is printed.
  
- **`get(key)`**: Retrieves the item associated with the specified key.

```python
guillaume@ubuntu:~/0x01$ cat 100-main.py
#!/usr/bin/python3
""" 100-main """
LFUCache = __import__('100-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
print(my_cache.get("B"))
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "H")
my_cache.print_cache()
my_cache.put("I", "I")
my_cache.print_cache()
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
print(my_cache.get("I"))
print(my_cache.get("H"))
my_cache.put("J", "J")
my_cache.print_cache()
my_cache.put("K", "K")
my_cache.print_cache()
my_cache.put("L", "L")
my_cache.print_cache()
my_cache.put("M", "M")
my_cache.print_cache()

guillaume@ubuntu:~/0x01$ ./100-main.py
Current cache:
A: Hello
B: World
C: Holberton
D: School
World
DISCARD: A
Current cache:
B: World
C: Holberton
D: School
E: Battery
Current cache:
B: World
C: Street
D: School
E: Battery
None
World
Street
DISCARD: D
Current cache:
B: World
C: Street
E: Battery
F: Mission
DISCARD: E
Current cache:
B: World
C: Street
F: Mission
G: San Francisco
DISCARD: F
Current cache:
B: World
C: Street
G: San Francisco
H: H
DISCARD: G
Current cache:
B: World
C: Street
H: H
I: I
I
H
I
H
I
H
DISCARD: B
Current cache:
C: Street
H: H
I: I
J: J
DISCARD: J
Current cache:
C: Street
H: H
I: I
K: K
DISCARD: K
Current cache:
C: Street
H: H
I: I
L: L
DISCARD: L
Current cache:
C: Street
H: H
I: I
M: M
guillaume@ubuntu:~/0x01$
```

---
Happy coding!
