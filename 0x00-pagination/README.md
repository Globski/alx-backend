# Alx Backend - Pagination

## Description

This project focuses on implementing pagination techniques to handle a dataset of popular baby names using Python. You will learn how to efficiently paginate data using various pagination strategies, including basic pagination such as simple page and page size parameters, hypermedia metadata, and delete-resilient pagination.
Throughout the project, you will deepen your understanding of these pagination techniques in APIs to ensure efficient data retrieval while accommodating changes in the underlying dataset.

## Project Structure

| Task                               | Description                                                                                                                      | Source Code                           |
|------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| 0. Simple helper function          | Write a function named `index_range` that takes two integer arguments `page` and `page_size` and returns a tuple of indexes.   | [0-simple_helper_function.py](0-simple_helper_function.py) |
| 1. Simple pagination               | Implement a `get_page` method that uses `index_range` to paginate the dataset correctly.                                        | [1-simple_pagination.py](1-simple_pagination.py) |
| 2. Hypermedia pagination           | Implement a `get_hyper` method that returns pagination info as a dictionary, reusing `get_page`.                                | [2-hypermedia_pagination.py](2-hypermedia_pagination.py) |
| 3. Deletion-resilient hypermedia pagination | Implement a `get_hyper_index` method that allows for robust pagination even when rows are deleted.                              | [3-hypermedia_del_pagination.py](3-hypermedia_del_pagination.py) |

### Environment

- Ubuntu 18.04 LTS
- Python 3.x
- pycodestyle style (version 2.5.*)

## Requirements

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/env python3
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your functions should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)'
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated.

## Learning Objectives

By the end of this project, you should be able to:

- Explain how to paginate a dataset with simple page and page_size parameters.
- Understand and implement pagination with hypermedia metadata (HATEOAS).
- Create a pagination system that remains resilient to data deletion.

## Prototype Table

| Method Name           | Parameters                                   | Return Type         | Description                                              |
|----------------------|----------------------------------------------|---------------------|----------------------------------------------------------|
| `index_range`        | `page: int, page_size: int`                 | `Tuple[int, int]`   | Returns the start and end index for pagination.          |
| `get_page`           | `page: int=1, page_size: int=10`            | `List[List]`        | Returns the appropriate page of the dataset.             |
| `get_hyper`          | `page: int=1, page_size: int=10`            | `Dict`              | Returns pagination information including the current page.|
| `get_hyper_index`    | `index: int=None, page_size: int=10`        | `Dict`              | Returns robust pagination information with indexed access. |

## How to Use

1. **Clone the Repository**
   ```bash
   git clone [repository_url]
   cd [repository_name]
   ```

2. **Create a Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```You will use the dataset provided in `Popular_Baby_Names.csv`. This file contains information about baby names, including counts and rankings.

## Data Source

The dataset used in this project is the `Popular_Baby_Names.csv`, which contains information about baby names, their counts, and rankings. [use this data file for your project](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/misc/2020/5/7d3576d97e7560ae85135cc214ffe2b3412c51d7.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20241103%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20241103T054907Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=169d41243fb39f3841cea5a9d5dcf26f05e3fccff3cac8d01d2cd8e67e9dc42f)

3. **Run the Test Files**
   You can run the provided test files to check your implementations:
   ```bash
   python3 0-main.py
   python3 1-main.py
   python3 2-main.py
   python3 3-main.py
   ```

- The dataset contains a total of 19,419 rows.

## Additional Notes

- Basic Pagination: This method uses simple page and page size parameters to retrieve specific sections of data.
- Hypermedia Pagination: This technique incorporates hypermedia metadata, allowing clients to navigate through the dataset using links provided in the response.
- Deletion-Resilient Pagination: This approach ensures that data retrieval remains consistent even if items in the dataset are deleted.

### Paginating a Dataset with Simple Page and Page Size Parameters

To paginate a dataset using simple parameters, you typically follow these steps:

1. **Define Parameters**: Use `page` to specify the current page number and `page_size` to define how many items to display per page.
  
2. **Calculate Offsets**: Use the formula `offset = (page - 1) * page_size` to determine where to start retrieving items from the dataset.

3. **Retrieve Data**: Fetch the items from the dataset using the calculated offset and the `page_size`.

4. **Return Response**: Include the current page, total pages, and the paginated data in the response.

### Pagination with Hypermedia Metadata (HATEOAS)

Hypermedia pagination enhances data navigation by providing links in the response:

1. **Embed Links**: Include URLs for the next page, previous page, and potentially other related resources in the response body.

2. **Dynamic Navigation**: Clients can use these links to fetch data, enabling them to navigate through the dataset without needing to know the structure of the API in advance.

3. **Standard Format**: Typically, the response might look like this:
   ```json
   {
       "data": [...],
       "links": {
           "next": "/api/names?page=2&page_size=10",
           "prev": "/api/names?page=1&page_size=10"
       }
   }
   ```

### Deletion-Resilient Pagination

To create a pagination system that remains resilient to data deletion:

1. **Use Unique Identifiers**: Instead of relying solely on page numbers, use unique identifiers (e.g., database IDs) to track items.

2. **Store Cursor Values**: Implement cursor-based pagination where you remember the last seen identifier. This helps fetch the next set of items reliably.

3. **Adjust for Deletions**: When an item is deleted, ensure that the pagination logic accounts for this by skipping over deleted items during retrieval.

4. **Response Example**: A cursor-based response might look like:
   ```json
   {
       "data": [...],
       "next_cursor": "id_10"
   }
   ```

## Tasks

### 0. Simple Helper Function

**Objective:**  
Write a function named `index_range` that takes two integer arguments `page` and `page_size`.  

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.  

Page numbers are 1-indexed, i.e. the first page is page 1.

**Function Signature:**
```python
def index_range(page: int, page_size: int) -> tuple:
```

- **Parameters:**
  - `page`: The current page number (1-indexed).
  - `page_size`: The number of items per page.

- **Returns:** A tuple containing the starting and ending index.

```bash
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```

- Directory: 0x00-pagination
- File: 0-simple_helper_function.py

### 1. Simple Pagination

**Objective:**  
Copy `index_range` from the previous task and the following class into your code.

```python
import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass
```
Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.

You have to use this CSV file (same as the one presented at the top of the project).  
Use `assert` to verify that both arguments are integers greater than 0.  
Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).  
If the input arguments are out of range for the dataset, an empty list should be returned.

**Method Signature:**
```python
def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
```

- **Parameters:**
  - `page`: The page number to retrieve (default is 1).
  - `page_size`: The number of items per page (default is 10).

- **Returns:** The list of rows for the requested page.

- **Requirements:** 
  - Use assertions to validate input.
  - Return an empty list if the parameters are out of range.

```bash
bob@dylan:~$  wc -l Popular_Baby_Names.csv 
19419 Popular_Baby_Names.csv
bob@dylan:~$  
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$
bob@dylan:~$  cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")


print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$   
```

- Directory: 0x00-pagination
- File: 1-simple_pagination.py

### 2. Hypermedia Pagination

**Objective:**  
Replicate code from the previous task.

Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:

- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page (equivalent to return from previous task)
- `next_page`: number of the next page, None if no next page
- `prev_page`: number of the previous page, None if no previous page
- `total_pages`: the total number of pages in the dataset as an integer

Make sure to reuse `get_page` in your implementation.

You can use the math module if necessary.

**Method Signature:**
```python
def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
```

- **Returns:** A dictionary containing:
  - `page_size`: Length of the current dataset page.
  - `page`: Current page number.
  - `data`: The actual dataset page.
  - `next_page`: Next page number (None if no next page).
  - `prev_page`: Previous page number (None if no previous page).
  - `total_pages`: Total number of pages in the dataset.

```bash
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))

bob@dylan:~$ 
bob@dylan:~$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
--- 
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page': 3, 'prev_page': 1, 'total_pages': 9709}
--- 
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Londyn', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'Amirah', '14', '39'], ['2016', 'FEMALE', 'BLACK NON HISPANIC', 'McKenzie', '14', '39']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6473}
--- 
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
bob@dylan:~$ 
```

- Directory: 0x00-pagination
- File: 2-hypermedia_pagination.py


### 3. Deletion-Resilient Hypermedia Pagination

**Objective:**  
The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from the dataset when changing page.

Start `3-hypermedia_del_pagination.py` with this code:

```python
#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
            pass
```

Implement a `get_hyper_index` method with two integer arguments: `index` with a None default value and `page_size` with default value of 10.

The method should return a dictionary with the following key-value pairs:
- `index`: the current start index of the return page. That is the index of the first item in the current page. For example if requesting page 3 with page_size 20, and no data was removed from the dataset, the current index should be 60.
- `next_index`: the next index to query with. That should be the index

 of the first item after the last item on the current page.
- `page_size`: the current page size
- `data`: the actual page of the dataset

**Requirements/Behavior:**
- Use `assert` to verify that index is in a valid range.
- If the user queries index 0, page_size 10, they will get rows indexed 0 to 9 included.
- If they request the next index (10) with page_size 10, but rows 3, 6 and 7 were deleted, the user should still receive rows indexed 10 to 19 included.

**Method Signature:**
```python
def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
```

- **Parameters:**
  - `index`: The starting index for the page (default is None).
  - `page_size`: The number of items to retrieve (default is 10).

- **Returns:** A dictionary containing:
  - `index`: Current start index of the return page.
  - `next_index`: The next index to query.
  - `page_size`: Current page size.
  - `data`: The actual page of the dataset.

```bash
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.indexed_dataset()

try:
    server.get_hyper_index(300000, 100)
except AssertionError:
    print("AssertionError raised when out of range")        

index = 3
page_size = 2

print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 1- request first index
res = server.get_hyper_index(index, page_size)
print(res)

# 2- request next index
print(server.get_hyper_index(res.get('next_index'), page_size))

# 3- remove the first index
del server._Server__indexed_dataset[res.get('index')]
print("Nb items: {}".format(len(server._Server__indexed_dataset)))

# 4- request again the initial index -> the first data retrieves is not the same as the first request
print(server.get_hyper_index(index, page_size))

# 5- request again initial next index -> same data page as the request 2-
print(server.get_hyper_index(res.get('next_index'), page_size))

bob@dylan:~$ 
bob@dylan:~$ ./3-main.py
AssertionError raised when out of range
Nb items: 19418
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4']], 'page_size': 2, 'next_index': 5}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
Nb items: 19417
{'index': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']], 'page_size': 2, 'next_index': 6}
{'index': 5, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6']], 'page_size': 2, 'next_index': 7}
bob@dylan:~$ 
```

- Directory: 0x00-pagination
- File: 3-hypermedia_del_pagination.py


