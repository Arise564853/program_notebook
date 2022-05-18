import pandas as pd
import datetime

def 累加月(日期, 传进来的月份):
    年 = 传进来的月份 // 12
    月 = 日期.month + 传进来的月份 % 12
    if 月 > 12:
        年 = 日期.year + 年 + 1
        月 = 月 - 12
    else:
        年 = 日期.year + 年
    return datetime.date(年, 月, 日期.day)


if __name__ == '__main__':
    start_date = datetime.date(2020, 5, 26)
    path = 'G:/pandas/自动填充.xlsx'
    data = pd.read_excel(path, skiprows=8, usecols='C:F', dtype={'序号': str, '姓名': str, '日期': str, '性别': str, })
    for i in data.index:
        data['序号'].at[i] = i + 1
        data['性别'].at[i] = "男"if i % 2 == 0 else "女"
        # data['日期'].at[i] = start_date + datetime.timedelta(days=i)
        # data['日期'].at[i] = datetime.date(start_date.year + i, start_date.month, start_date.day)
        data['日期'].at[i] = 累加月(start_date, i)
    data.set_index('序号', inplace=True)
    data.to_excel(path)
    print(data)
