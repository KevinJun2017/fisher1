class BookViewModel:
    def __init__(self, data):
        self.title = data['title']
        self.publisher = data['publisher']
        self.author = '、'.join(data['author'])
        self.image = data['image']
        self.price = data['price']
        self.binding = data['binding']
        self.summary = data['summary']
        self.pages = data['pages']


class BookCollection:
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.books = [BookViewModel(book) for book in yushu_book.books]
        self.keyword = keyword
