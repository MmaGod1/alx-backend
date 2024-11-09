#!/usr/bin/env python3
"""Hypermedia pagination"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Returns a tuple containing the start and end index for pagination.

    Arguments:
    page -- The page number (1-indexed).
    page_size -- The number of items per page.

    Returns:
    A tuple (start_index, end_index).
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns the page of data corresponding to
        the given page number and page size."""
        assert isinstance(page, int) and page > 0, (
                "page must be a positive integer"
                )
        assert isinstance(page_size, int) and page_size > 0, (
                "page_size must be a positive integer"
                )

        # Get the full dataset
        dataset = self.dataset()

        # Use index_range to calculate the start and end index for pagination
        start_idx, end_idx = index_range(page, page_size)

        # If the indices are out of range, return an empty list
        if start_idx >= len(dataset):
            return []

        # Return the correct page slice
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Returns a dictionary containing pagination
        data, including metadata."""
        # Get the current page data using get_page
        data = self.get_page(page, page_size)

        # Calculate the total number of pages
        total_data = len(self.dataset())
        total_pages = math.ceil(total_data / page_size)

        # Determine the previous and next pages
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        # Return a dictionary with pagination metadata
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
