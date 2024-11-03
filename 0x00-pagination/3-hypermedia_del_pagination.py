#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


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
                i: dataset[i]
                for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a hypermedia pagination dictionary.
  
        Parameters:
        index (int): The starting index for pagination (default is None).
        page_size (int): The number of items to return (default is 10).

        Returns:
        Dict: A dictionary containing the index,
        page_size, data, and next_index.

        Raises:
        AssertionError: If index is out of range.
        """
        assert index >= 0 and index < len(self.__indexed_dataset), \
            "Index out of range"

        indexed_data = self.indexed_dataset()

        result = {
            'index': index,
            'data': [],
            'page_size': page_size,
            'next_index': index + page_size
        }

        for i in range(page_size):
            if index + i in indexed_data:
                result['data'].append(indexed_data[index + i])

        return result
