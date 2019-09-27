import os

def data_dir(data=None,filename=None):
    '''查找文件的路径'''
    return os.path.join(os.path.dirname(os.path.dirname(__file__)),data,filename)


#print(data_dir('data','data.xls'))