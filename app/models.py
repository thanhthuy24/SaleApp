#nơi tạo lớp đối tượng - entity class
#lớp entity đại diện cho 1 bảng trên database

from sqlalchemy import Column, Integer, String, Float, ForeignKey
from app import db, app

#class đại diện cho 1 bảng => bảng Category trong database
class Category(db.Model): #db.Model chính là kế thùa
    __tablename__ = 'category' #chỉnh lại tên của bảng

    #mỗi thuộc tính trong lớp là 1 cột trong db
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)

class Product(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False, unique=True)
    price = Column(Float, default=8)
    image = Column(String(100))
    category_id = Column(Integer, ForeignKey(Category.id), nullable=False)

if __name__ == '__main__':
    #phải chạy trong ngữ cảnh của ứng dụng
    with app.app_context():
        # tạo database cho các class đã tạo ở trên
        # db.create_all()

        #tạo dữ liệu category
        # c1 = Category(name='Mobile')
        # c2 = Category(name='Laptop')
        # # session quan trọng trong mô hình ORM
        # # hầu như mọi ngôn ngữ đều dùng, có thể khác cú pháp
        # db.session.add(c1)
        # db.session.add(c2)
        # # #gọi commit => tạo ra 2 câu insert into
        # db.session.commit()

        #tạo dữ liệu product
        p1 = Product(name='iPhone 13', price='20000000', category_id=1,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        p2 = Product(name='SamSung S20FE', price='16000000', category_id=1,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        p3 = Product(name='Laptop Asus Vivobook', price='19000000', category_id=2,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        p4 = Product(name='iPhone 15', price='28000000', category_id=1,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        p5 = Product(name='SamSung Note 21', price='30000000', category_id=1,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        p6 = Product(name='Laptop MSI', price='25000000', category_id=2,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        p7 = Product(name='Laptop Dell', price='20500000', category_id=2,
                     image='https://th.bing.com/th/id/OIP.D2L5Emr_tkvju5Hilr22DgHaHa?rs=1&pid=ImgDetMain')

        db.session.add_all([p1, p2, p3, p4, p5, p6, p7])
        db.session.commit()

#phải chạy create_all trước!!!