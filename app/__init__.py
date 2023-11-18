from flask import Flask
#dùng thay thế mật khẩu có kí tự đặc biệt và bị trùng
from urllib.parse import quote
#lớp đối tượng
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#trong admin cần có 1 session để gửi qua lại, session nằm ở server nên cần thm 1 secret_key để mã hóa
app.secret_key = 'sdfsjfg38r78436elkfhuiefhjsdbfdf'

app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:%s@localhost/saleappdb?charset=utf8mb4" % quote('Admin123@')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app=app)