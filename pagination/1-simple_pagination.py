#!/usr/bin/env python3
"""
Simple pagination of a baby names dataset
"""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Compute start and end indexes for a given page"""
    start = (page - 1) * page_size  # start index
    end = page * page_size          # end index
    return (start, end)


class Server:
    """Class to paginate a CSV dataset"""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize dataset cache"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                data = [row for row in reader]
            self.__dataset = data[1:]  # remove header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a page of data"""

        # check valid inputs
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # get slice indexes
        start, end = index_range(page, page_size)

        data = self.dataset()

        # out of range → return empty list
        if start >= len(data):
            return []

        # return requested slice
        return data[start:end]
