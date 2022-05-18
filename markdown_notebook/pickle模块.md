# pickle模块

存放pickling

读取unpickling

>>> 储存
>>>
>>> import pickle
>>> my_list = [123,3.14,'孙兴华',['another list']]
>>> pickle_file = open('my_list.pkl','wb')
>>> pickle.dump(my_list,pickle_file)
>>> pickle_file.close()
>>> 打开
>>> pickle_file = open('my_list.pkl','rb')
>>> my_list2 = pickle.load(pickle_file)
>>> print(my_list2)
>>> [123, 3.14, '孙兴华', ['another list']]
>>>
>>> pickle_file.close()