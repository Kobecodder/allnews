__author__ = 'giasuddin'


def pager(total_row=None, item_per_page=None):
    pages = {}
    total_page = total_row/item_per_page

    if total_row % item_per_page != 0 and total_page > 1:
        total_page += 1
    for page in range(1, int(total_page) + 1):
        m = page - 1
        pages[page] = item_per_page * m
    return pages
