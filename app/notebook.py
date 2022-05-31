import json
import datetime
import PySimpleGUI as sg
import os


def readData():
    with open('userdata.json') as f:
        try:
            dataList = json.load(f)
        except json.decoder.JSONDecodeError:
            dataList = []
        finally:
            return dataList


def writeData(userData):
    with open("userdata.json", "w") as f:
        json.dump(userData, f, ensure_ascii=False)
        sg.popup('账单录入成功！')

def delData():
    """删除数据"""
    pass


def showData():
    data = readData()
    dataLists = []
    for d in data:
        if d["分类"] == "收入":
            dataList = [d["时间"], d["类目"], d["金额"], d["分类"]]
        elif d["分类"] == "支出":
            dataList = [d["时间"], d["类目"], d["金额"] * -1, d["分类"]]
        dataLists.append(dataList)
    return dataLists


def sumin():
    result = 0
    data = readData()
    for d in data:
        if d["分类"] == "收入":
            result += d["金额"]
    return result


def sumout():
    result = 0
    data = readData()
    for d in data:
        if d["分类"] == "支出":
            result += d["金额"]
    return result


def addData(content, amount, cls):
    data = readData()
    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    data.append({"时间": t, "类目": content, "金额": amount, "分类": cls, })
    writeData(data)


def main():
    layout = [
        [sg.T("账目清单：")],
        [sg.Table(showData(), headings=["时间", "类目", "金额", "分类"],
                  key="-show-",
                  justification="c",
                  auto_size_columns=False,
                  def_col_width=20,
                  )],
        [sg.T(f"总收入{str(sumin())}元，总支出{str(sumout())}元，结余{str(sumin()-sumout())}元", key="-text-")],
        [sg.T("请输入账单类目："), sg.In(key="-content-")],
        [sg.T("请输入账单金额："), sg.In(key="-amount-")],
        [sg.T("请选择账单分类：")] + [sg.Radio(i, group_id=1, key=i) for i in ["收入", "支出"]],
        [sg.B("确认提交")]
    ]

    window = sg.Window('记账本', layout)
    while True:
        event, values = window.read()
        if event == "确认提交":
            content = values["-content-"]
            amount = float(values["-amount-"])
            for k, v in values.items():
                if v is True:
                    cla = k
                    addData(content, amount, cla)
                    List = showData()
                    text = f"总收入{str(sumin())}元，总支出{str(sumout())}元，结余{str(sumin()-sumout())}元"
                    window["-show-"].update(values=List)
                    window["-text-"].update(value=text)
                    window["-content-"].update("")
                    window["-amount-"].update("")
        if event is None:
            break
    window.close()


if not os.path.exists("userdata.json"):
    fp = open("userdata.json", "w")
    fp.close()
main()
