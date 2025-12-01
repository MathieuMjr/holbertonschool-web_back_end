#!/usr/bin/env python3
"""
This module contains a class Server that access
a csv
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple with that start index and end index
    of element to display in pagination
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


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
        Function that get datas in a csv at given
        index
        """
        assert (isinstance(page, int) and isinstance(page_size, int)
                ), "Page and/or page_size are not ints"
        assert page > 0 and page_size > 0, "Page or page_size not positive"
        indexs = index_range(page, page_size)
        self.__dataset = self.dataset()
        return self.__dataset[indexs[0]:indexs[1]]

    def get_hyper(
            self,
            page: int = 1,
            page_size: int = 0
            ) -> List[List]:
        datas = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        if page >= total_pages:
            next_page = None
        else:
            next_page = page + 1
        if page > 1:
            previous_page = page - 1
        else:
            previous_page = None
        if not datas:
            page_size = 0
        return {
            'page_size': page_size,
            'page': page,
            'data': datas,
            'next_page': next_page,
            'previous_page': previous_page,
            'total_pages': total_pages
        }
