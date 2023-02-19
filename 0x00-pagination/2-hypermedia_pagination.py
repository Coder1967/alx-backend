#!/usr/bin/env python3
import csv
import math
from typing import List, Tuple, Dict
"""
Hypermedia Pagination
"""


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
        """
        takes page and page_size as arguments and return data
        from a csv file matching those specifications
        """
        assert type(page).__name__ == "int" and page > 0
        assert type(page_size).__name__ == "int" and page_size > 0
        index: Tuple[int, int] = index_range(page, page_size)
        data: List = self.dataset()

        if index[0] <= len(data):
            return self.__dataset[index[0]:index[1]]
        else:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        takes page and page_size as arguments and return data
        from a csv file matching those specifications in dict form
        """
        data: List[List] = self.dataset()
        total_pages: int = math.floor(len(data) / page_size)
        prev_page: int = page - 1
        next_page: int = page + 1
        values: List[List] = self.get_page(page, page_size)

        if page - 1 == 0:
            prev_page = None
        if total_pages < page * page_size:
            next_page = None

        return {'page_size': len(values), 'page': page, 'data': values,
                'next_page': next_page, 'prev_page': prev_page,
                'total_pages': total_pages
                }


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function should return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters
    """
    start_index: int = (page * page_size) - page_size
    return (start_index, page * page_size)
