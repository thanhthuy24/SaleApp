from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product
from app import db, app

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')

#muốn mở rộng => kế thừa + ghi đè
class MyProductView(ModelView):
    #hiển thị
    column_list = ['id', 'name','price']
    #xuất file excel
    can_export = True
    #tìm kiếm
    column_searchable_list = ['name']
    #bộ lọc => theo giá, tên
    column_filters = ['price', 'name']
    #chỉnh dữ liệu trực tiếp trên web
    column_editable_list = ['name', 'price']
    #edit toàn dữ liệu14
    edit_modal = True

class MyCategoryView(ModelView):
    column_list = ['name', 'products']


class MyStatsView(BaseView):
    #nạp phần domain vô, nối đuôi đường dẫn mới

    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

#tạo view vùng quản trị cho Category
# vì trong thiết kế, db để ở vùng session nên để là db.session
admin.add_view(MyCategoryView(Category, db.session))
#tương tự với Product
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))