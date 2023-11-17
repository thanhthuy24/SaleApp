from flask import Flask
#dùng thay thế mật khẩu có kí tự đặc biệt và bị trùng
from urllib.parse import quote
#lớp đối tượng
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saleappdb?charset=utf8mb4" % quote('Admin123@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)