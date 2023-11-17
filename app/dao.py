from app.models import Category, Product
def load_categories():
    #tương đuong như câu lệnh trong SQL: SELECT * FROM CATEGORY
    return Category.query.all()


def load_products(kw):
    products=Product.query

    if kw:
        products = products.filter(Product.name.contains(kw))

    return products.all()