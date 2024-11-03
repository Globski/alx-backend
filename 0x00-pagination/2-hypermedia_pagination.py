#!/usr/bin/env python3
"""
This module provides functionality for paginating a dataset of popular baby names.

It includes a helper function to calculate index ranges for pagination
and a Server class that manages the dataset and provides methods to 
retrieve specific pages of data.

Usage:
    To use this module, create an instance of the Server class and call
    the `get_page` or `get_hyper` method with the desired page number 
    and page size.
"""

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate the start and end indices for pagination.

    Parameters:
    page (int): The page number (1-indexed).
    page_size (int): The number of items per page.

    Returns:
    Tuple[int, int]: A tuple containing the start and end indices for the dataset slice.

    Raises:
    ValueError: If page or page_size is less than 1.
    """
    if page < 1 or page_size < 1:
        raise ValueError("Page and page_size must be greater than 0")
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.

    Attributes:
    DATA_FILE (str): The path to the CSV file containing baby names data.
    __dataset (List[List[str]]): Cached dataset loaded from the CSV file.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance with an empty dataset."""
        self.__dataset = None

    def dataset(self) -> List[List[str]]:
        """Load and cache the dataset from the CSV file.

        Returns:
        List[List[str]]: The dataset containing baby names data.
        If the dataset has not been loaded yet, it reads from the CSV file
        and caches the result for future access.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List[str]]:
        """Return a specific page of the dataset.

        Parameters:
        page (int): The page number (1-indexed, default is 1).
        page_size (int): The number of items per page (default is 10).

        Returns:
        List[List[str]]: A list containing the rows of the dataset for the
                         requested page. Returns an empty list if the page
                         is out of range.

        Raises:
        AssertionError: If page or page_size is not a positive integer.
        """
        assert isinstance(page, int) and page > 0, "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "page_size must be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return a hypermedia pagination dictionary.

        Parameters:
        page (int): The page number (1-indexed, default is 1).
        page_size (int): The number of items per page (default is 10).

        Returns:
        Dict[str, Any]: A dictionary containing pagination information including
                         page size, current page, data, next page, previous page,
                         and total pages.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
