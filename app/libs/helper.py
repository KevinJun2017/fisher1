'''
isbn十位，包含部分'-'，或者13位纯数字
:param q:
:param page:
:return:
'''


def isbn_or_key(q):
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = "isbn"
    short_q = q.replace('-', '')
    if '-' in q and short_q.isdigit() and len(short_q) <= 10:
        isbn_or_key = "isbn"
    print(isbn_or_key)
    return isbn_or_key
