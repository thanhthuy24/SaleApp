from app.models import Category, Product, User
import hashlib
from app import app

def load_categories():
    #tương đuong như câu lệnh trong SQL: SELECT * FROM CATEGORY
    return Category.query.all()


def load_products(kw, cate_id, page=None):
    products=Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    if cate_id:
        products = products.filter(Product.category_id.__eq__(cate_id))

    if page:
        page = int(page)
        page_size = app.config['PAGESIZE']
        start = (page-1)*page_size

        return products.slice(start, start + page_size)

    return products.all()

def count_product():
    return Product.query.count()

def get_user_by_id(user_id):
    return User.query.get(user_id) #câu truy vấn có nghĩa là: SELECT * FROM USER WHERE ID = 'user_id'

#viết hàm truy vấn database
def auth_user(username, password):
    #băm mật khẩu
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()
                        #=> vì username là unique nên kết quả trả ra chỉ có 1, dùng hàm first để lấy thằng đầu tiên
                        #=> nếu tồn tại user -- đối tượng khác null

# from app.models import Category, Product, User
# import hashlib
# from app import app
#
#
# def get_categories():
#     return Category.query.all()
#
#
# def get_products(kw, cate_id, page=None):
#     products = Product.query
#
#     if kw:
#         products = products.filter(Product.name.contains(kw))
#
#     if cate_id:
#         products = products.filter(Product.category_id.__eq__(cate_id))
#
#     if page:
#         page = int(page)
#         page_size = app.config['PAGE_SIZE']
#         start = (page - 1)*page_size
#
#         return products.slice(start, start + page_size)
#
#     return products.all()
#
#
# def count_product():
#     return Product.query.count()
#
#
# def get_user_by_id(user_id):
#     return User.query.get(user_id)
#
#
# def auth_user(username, password):
#     password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
#
#     return User.query.filter(User.username.__eq__(username.strip()),
#                              User.password.__eq__(password)).first()