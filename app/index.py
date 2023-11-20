import math

from flask import render_template, request, redirect #chuyển giữa các man hình khác nhau
import dao
from app import app, login
from flask_login import login_user

@app.route('/')
def index():
    kw = request.args.get('kw')
    cate_id = request.args.get('cate_id')
    page = request.args.get('page')

    cates = dao.load_categories()
    prods = dao.load_products(kw, cate_id, page)

    num = dao.count_product()

    return render_template('index.html',categories=cates, products=prods,
                           pages=math.ceil(num/app.config['PAGESIZE']))

@app.route('/admin/login', methods=['post'])
def admin_login():
    username = request.args.get('username')
    password = request.args.get('password')

    user = dao.auth_user(username=username, password=password)
    if user: #bước này user đã khác null, đã đăng nhập thành công
        login_user(user=user)

    return redirect('/admin')

@login.user_loader
def get_user(user_id):
    return dao.get_user_by_id(user_id)

if __name__ == '__main__':
    #import để lúc chạy thì chạy luôn cái module nay
    from app import admin
    app.run(debug=True)