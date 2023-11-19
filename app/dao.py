from app.models import Category, Product, User
import hashlib
def load_categories():
    #tương đuong như câu lệnh trong SQL: SELECT * FROM CATEGORY
    return Category.query.all()


def load_products(kw):
    products=Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()

def get_user_by_id(user_id):
    return User.query.get(user_id) #câu truy vấn có nghĩa là: SELECT * FROM USER WHERE ID = 'user_id'

#viết hàm truy vấn database
def auth_user(username, password):
    #băm mật khẩu
    password = str(hashlib.md5(password.strip().encoding('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()), #strip() --- cắt bỏ khoảng trắng 2 đầu
                             User.password.__eq__(password)).first()
                        #=> vì username là unique nên kết quả trả ra chỉ có 1, dùng hàm first để lấy thằng đầu tiên
                        #=> nếu tồn tại user -- đối tượng khác null