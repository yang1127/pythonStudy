# -*-coding:utf-8-*-
import pymysql
from pymysql.cursors import DictCursor
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("upgrade.html")


@app.route("/find", methods=['GET', 'POST'])
def find():
    while True:
        # sn = input("输入要查询的sn：")
        # version_id = input("输入要查询的版本号：")

        sn = request.args.get("sn")
        version_id = request.args.get("version_id")

        # 连接
        conn = pymysql.connect(host='10.90.73.43', port=4700, user='sys_manage_rw', password='tQnrd6Kz0lKB7OY_', database="sys_manage")
        # 获取游标
        cursor = conn.cursor(cursor=DictCursor)

        # 查询
        sql1 = "select * from cm_os_upgrade where sn=%s and version_id=%s"
        cursor.execute(sql1, [sn, version_id])

        # 获取查询结果
        result = cursor.fetchone()
        # 取upgrade_status字段-字典类型
        res_status = result.get('upgrade_status')

        # 判断是否升级成功
        if res_status == 1:
            print("sn升级成功!")
        else:
            print("sn升级失败!")

        # 关闭游标
        cursor.close()

        # 关闭连接
        conn.close()


if __name__ == '__main__':
    app.run()
