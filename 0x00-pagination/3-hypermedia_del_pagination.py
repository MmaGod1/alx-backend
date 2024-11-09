#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header row
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dictionary containing pagination data and handles deletions"""
        assert isinstance(index, int) and index >= 0, "index must be a non-negative integer"
        
        # Get the indexed dataset
        indexed_dataset = self.indexed_dataset()
        
        # Assert index is within valid range
        assert 0 <= index < len(indexed_dataset), "index out of range"

        # Initialize the page and next_index
        data = []
        current_index = index
        
        # Retrieve the requested page
        while len(data) < page_size:
            if current_index in indexed_dataset:
                data.append(indexed_dataset[current_index])
            current_index += 1
        
        # Calculate next_index: the index after the last item on the current page
        next_index = current_index if current_index < len(indexed_dataset) else None
        
        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
