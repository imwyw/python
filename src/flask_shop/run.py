from flask import Flask  # 导入Flask模块
from flask import render_template, request, redirect, url_for, session  # 模板渲染
from MySQLManage import MysqlManage

manage = MysqlManage()

app = Flask(__name__)
app.secret_key = "some_secret"


@app.route("/")  # http://127.0.0.1:5000,映射关系，把url和功能函数相关联
def main():
    mygoods = manage.get_goods_from_mysql()
    return render_template("main.html", goods=mygoods)


@app.route("/students")  # http://127.0.0.1:5000/students
def get_students():
    students = [
        {"name": "张三", "age": 25, "jiguan": "遵义"},
        {"name": "李四", "age": 22, "jiguan": "上海"},
        {"name": "tom", "age": 18, "jiguan": "澳大利亚"}
    ]
    name = "cathy"
    return render_template("students.html", students=students, name=name)


@app.route("/content/<id>")
def show_content(id):
    if 'user' not in session:  # 未登录
        return render_template("login.html")

    good = manage.get_goods_from_mysql(int(id))
    # 告诉我，你选中的是哪个商品
    return render_template("content.html", good=good)


@app.route("/login", methods=["GET", "POST"])
def login():  # 通过url访问，即请求页面时，返回登录页面
    if request.method == "GET":
        return render_template("login.html")
    else:
        # 1.获取表单数据
        user = request.form["myName"]  # 用户名
        psd = request.form["myPsd"]  # 密码
        result = manage.login(user, psd)
        if result == 1:  # 登陆成功
            session["user"] = user
            session["psd"] = psd
            return redirect(url_for("main"))  # url_for:根据函数得到URL地址

        else:  # 登陆失败
            message = "用户名或密码错误，请重新输入。"
            return render_template("login.html", msg=message)


# 注册页面
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":  # 从登陆页面跳转过来的
        return render_template("register.html")
    else:  # 用于实现注册功能（POST)
        # 1.获取表单数据
        user = request.form["myName"]  # 用户名
        psd = request.form["myPsd"]  # 密码
        country = request.form["country"]  # 国籍
        sex = request.form["sex"]  # 性别
        like = request.form.getlist("like")  # 爱好，列表的形式
        like = ",".join(like)
        login_info = {"user": user,
                      "psd": psd,
                      "country": country,
                      "sex": sex,
                      "like": like}

        # 2.将数据保存到数据库中
        result = manage.insert_to_db(login_info)
        if result == -1:  # 用户已存在
            message = "用户已存在，请重新选择！"
            return render_template("register.html", msg=message)
        elif result == 1:  # 注册成功
            return render_template("login.html")
        else:
            message = "注册失败！"
            return render_template("register.html", msg=message)


if __name__ == "__main__":
    app.run(host="127.0.0.1", debug=True)
