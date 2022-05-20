class PageTypeException(Exception):
    pass


class YearTypeException(Exception):
    pass


class AuthorTypeException(Exception):
    pass


class PriceTypeException(Exception):
    pass


class Book:
    def __init__(self, page_count: int, year: int, author: str, price: float):
        if not isinstance(page_count, int):
            raise PageTypeException('Wrong type for attr page_count! Please set int')
        if not isinstance(year, int):
            raise YearTypeException('Wrong type for attr year! Please set int!')
        if not isinstance(author, str):
            raise AuthorTypeException('Wrong type for attr author! Please set str!')
        if not isinstance(price, float):
            raise PriceTypeException('Wrong type for attr price! Please set float')

        self.page_count = page_count
        self.year = year
        self.author = author
        self.price = price


if __name__ == '__main__':
    book = Book(page_count=200, year=1998, author='Sheckspir', price=100.0)
    print(book.page_count, )
