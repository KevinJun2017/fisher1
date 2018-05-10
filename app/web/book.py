from app.forms.book import SearchForm
from app.libs.helper import isbn_or_key
from app.view_models.book import BookCollection
from yushu_book import YuShuBook
from flask import jsonify
from flask import request
from . import web
import json


# rest形式的请求形式
# @web.route("/book/search/<q>/<page>")

@web.route("/book/search")  # 字典类型的传参形式
def search():
    form = SearchForm(request.args)
    books = BookCollection()
    q = form.q.data.strip()
    page = form.page.data

    if form.validate():
        book = YuShuBook()

        if isbn_or_key(q) == 'isbn':
            book.search_by_isbn(q)
            return jsonify(book)
        else:
            book.search_by_keyword(q, page)

        books.fill(book, q)
        return json.dumps(books, default=lambda o: o.__dict__)
    else:
        return jsonify(form.errors)
