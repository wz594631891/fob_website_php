# 1210下载图片整合文件夹
#v1.0
from selenium import webdriver
from time import sleep as slp
import time
from exsql import execute
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
#下载图片参数 pic链接 型号 序号
def download_image(url,model,i):
    #请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
    }

    response = requests.get(url,headers=headers)
    with open(model+'\\水印\\'+i+".jpg", 'wb') as f:
        f.write(response.content)
    print(url)
    return model+'\\水印\\'+i+".jpg"#返回文件路径
    # print(response.status_code)
    # print(response.content)
#导入数据到数据库
#根据model创建文件夹
for id in range(1,314):
    id=str(id)
    model=execute("select model from wk.aliexpress_goods where id="+id+";")#获取型号
    model=model[0][0]
    print(model)
    if not os.path.exists(model+"\\水印"):
        #创建文件夹
        os.makedirs(model+"\\水印")
    # if not os.path.exists(model + "\\水印\\"+id+".jpg"):
    #     f=open(model + "\\水印\\"+id+".jpg","wb")
    #     f.close()
    #根据pic1-6下载图片
    #下载pic1
    pic1=execute("select pic1 from wk.aliexpress_goods where id="+id+";")[0][0]
    path=download_image(pic1, model, "1")
   # print(path)
    path=os.path.abspath(path).replace('\\',r'\\') #获取绝对路径 斜杠替换为双斜杠(不换会被mysql替换"")
    print(path)
    #

    #存储绝对路径到数据库
    execute("update wk.aliexpress_goods set pic1_loc='"+path+"' where id="+id+";")
    # 下载pic2
    pic2 = execute("select pic2 from wk.aliexpress_goods where id=" + id + ";")[0][0]
    if not pic2=='':
        path =download_image(pic2, model, "2")
        path=os.path.abspath(path).replace('\\',r'\\') #获取绝对路径 斜杠替换为双斜杠(不换会被mysql替换"")
        print(path)
        # 存储绝对路径到数据库
        execute("update wk.aliexpress_goods set pic2_loc='" + path + "' where id="+id+";")
    # 下载pic3
    pic3 = execute("select pic3 from wk.aliexpress_goods where id=" + id + ";")[0][0]
    if not pic3 == '':
        path = download_image(pic3, model, "3")
        path=os.path.abspath(path).replace('\\',r'\\') #获取绝对路径 斜杠替换为双斜杠(不换会被mysql替换"")
        print(path)
        # 存储绝对路径到数据库
        execute("update wk.aliexpress_goods set pic3_loc='" + path + "' where id="+id+";")
    # 下载pic4
    pic4 = execute("select pic4 from wk.aliexpress_goods where id=" + id + ";")[0][0]
    if not pic4 == '':
        path =download_image(pic4, model, "4")
        path=os.path.abspath(path).replace('\\',r'\\') #获取绝对路径 斜杠替换为双斜杠(不换会被mysql替换"")
        print(path)
        # 存储绝对路径到数据库
        execute("update wk.aliexpress_goods set pic4_loc='" + path + "' where id="+id+";")
    # 下载pic5
    pic5 = execute("select pic5 from wk.aliexpress_goods where id=" + id + ";")[0][0]
    if not pic5 == '':
        path =download_image(pic5, model, "5")
        path=os.path.abspath(path).replace('\\',r'\\') #获取绝对路径 斜杠替换为双斜杠(不换会被mysql替换"")
        print(path)
        # 存储绝对路径到数据库
        execute("update wk.aliexpress_goods set pic5_loc='" + path + "' where id="+id+";")
    # 下载pic6
    pic6 = execute("select pic6 from wk.aliexpress_goods where id=" + id + ";")[0][0]
    if not pic6 == '':
        path =download_image(pic6, model, "6")
        path=os.path.abspath(path).replace('\\',r'\\') #获取绝对路径 斜杠替换为双斜杠(不换会被mysql替换"")
        print(path)
        # 存储绝对路径到数据库
        execute("update wk.aliexpress_goods set pic6_loc='" + path + "' where id="+id+";")
        #
    #
    #



