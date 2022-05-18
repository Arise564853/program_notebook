file_name = input("输入文件名：")
point = file_name.rfind('.')
new_name = file_name[:point] + '备份' + file_name[point:]
file = open(file_name, 'rb',)
new_file = open(new_name, 'wb')
while True:
    contain = file.read(1024)
    if len(contain) == 0:
        break
    new_file.write(contain)
file.close()
new_file.close()
