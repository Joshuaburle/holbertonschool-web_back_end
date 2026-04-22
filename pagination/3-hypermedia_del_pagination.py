#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Initialize dataset and indexed dataset cache"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Load and cache dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # remove header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Create dataset indexed by position"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }

        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a deletion-resilient page of data"""
        data = self.indexed_dataset()

        # use 0 if index is None
        if index is None:
            index = 0

        # check that index is valid
        assert isinstance(index, int) and index >= 0 and index < len(self.dataset())
        assert isinstance(page_size, int) and page_size > 0

        page_data = []
        current_index = index

        # collect page_size items, skipping deleted indexes
        while len(page_data) < page_size and current_index in range(len(self.dataset())):
            if current_index in data:
                page_data.append(data[current_index])
            current_index += 1

        return {
            "index": index,                 # starting index of the page
            "data": page_data,              # page data
            "page_size": len(page_data),    # actual page size
            "next_index": current_index     # next index to query
        }
