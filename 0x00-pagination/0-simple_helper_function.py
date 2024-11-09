#!/usr/bin/env python3
"""
Function to calculate the range of indexes to return in pagination.
"""


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
