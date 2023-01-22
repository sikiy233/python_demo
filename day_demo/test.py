# 导入OS模块
import os

# 待搜索的目录路径
path = r"E:\新建文件夹\《百家讲坛》 20220516 大明帝陵 3 北卜天寿建长陵"
# 待搜索的名称
filename = ""
# 定义保存结果的数组
result = []


def findfiles(path):
    # 首先遍历当前目录所有文件及文件夹
    file_list = os.listdir(path)
    # 循环判断每个元素是否是文件夹还是文件，是文件夹的话，递归
    for file in file_list:
        # 利用os.path.join()方法取得路径全名，并存入cur_path变量，否则每次只能遍历一层目录
        cur_path = os.path.join(path, file)

        # 判断是否是文件夹
        if os.path.isdir(cur_path):
            findfiles(cur_path)
        else:
            # 判断是否是特定文件名称


            print(cur_path.replace('\\','\\\\'))
            # print(cur_path.split('\\')[2].replace(' ',''))
            # with open(cur_path.split('\\')[2].replace(' ','')+'1.txt','a+',encoding='utf8')as file:
            #     file.write('file '+"'"+str(cur_path)+"'"+'\n')
            # print(cur_path.split('\\')[2].replace(' ',''))

if __name__ == '__main__':
    findfiles(path)
