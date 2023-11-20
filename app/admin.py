from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app.models import Category, Product, UserRoleEnum
from app import db, app
from flask_login import logout_user, current_user
from flask import redirect

admin = Admin(app=app, name='Quản trị bán hàng', template_mode='bootstrap4')

class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRoleEnum.ADMIN

class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated

#muốn mở rộng => kế thừa + ghi đè
class MyProductView(AuthenticatedAdmin):
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

    #hàm cho ai cũng có quyền đăng nhập


class MyCategoryView(AuthenticatedAdmin):
    column_list = ['name', 'products']


class MyStatsView(AuthenticatedUser):
    #nạp phần domain vô, nối đuôi đường dẫn mới

    @expose("/")
    def index(self):
        return self.render('admin/stats.html')

class MyLogoutView(AuthenticatedUser):
    #nạp phần domain vô, nối đuôi đường dẫn mới

    @expose("/")
    def index(self):
        logout_user()
        return redirect('/admin')

#tạo view vùng quản trị cho Category
# vì trong thiết kế, db để ở vùng session nên để là db.session
admin.add_view(MyCategoryView(Category, db.session))
#tương tự với Product
admin.add_view(MyProductView(Product, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
admin.add_view(MyLogoutView(name='Đăng xuất'))