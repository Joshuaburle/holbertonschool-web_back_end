#!/usr/bin/env python3
"""
Hypermedia pagination for a baby names dataset
"""

import csv
import math
from typing import List, Tuple, Dict


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        data = self.dataset()

        if start >= len(data):
            return []

        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Return pagination metadata with the page data"""
        data = self.get_page(page, page_size)  # get current page
        total_pages = math.ceil(len(self.dataset()) / page_size)

        # set previous and next pages
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            "page_size": len(data),      # size of returned page
            "page": page,                # current page number
            "data": data,                # page data
            "next_page": next_page,      # next page or None
            "prev_page": prev_page,      # previous page or None
            "total_pages": total_pages   # total number of pages
        }
