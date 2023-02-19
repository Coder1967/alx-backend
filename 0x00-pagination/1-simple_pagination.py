import csv
import math
from typing import List, Tuple
"""
Simple pagination
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
        returns data for that specified page
        """
        assert type(page).__name__ == "int" and page > 0
        assert type(page_size).__name__ == "int" and page_size > 0
        index: Tuple[int, int] = index_range(page, page_size)
        data: List[List] = self.dataset()

        if index[0] <= len(data):
            return self.__dataset[index[0]:index[1]]
        else:
            return []


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    function should return a tuple of size two containing a
    start index and an end index corresponding to the range of
    indexes to return in a list for those particular pagination parameters
    """
    start_index: int = (page * page_size) - page_size
    return (start_index, page * page_size)
