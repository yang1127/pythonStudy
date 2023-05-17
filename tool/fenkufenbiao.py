# -*-coding:utf-8-*-
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("findindex.html")


@app.route("/find", methods=['GET', 'POST'])
def find():
    if request.method == 'GET':
        userid = request.args.get("userid")
        # print(userid)
        # 默认是str，需转换成int
        user_id = int(userid)

        # hash取模，取用户后四位，计算相应规则
        nums = (user_id % 10000) % 1024

        print("库id：")
        db = int(nums // 256)

        print("order-info表编号：")
        orderinfo_table = int(nums % 256 // 64)


        print("order-detail表编号：")
        orderdetail_table = int(nums % 256 // 8)

        return render_template("findindex.html",
                                db=db,
                                orderinfo_table=orderinfo_table,
                                orderdetail_table=orderdetail_table)
    return render_template("findindex.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
