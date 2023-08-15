#@author 叶志豪
#@description 在桌面缩放全OEM\\下水印和白底JPG文件到1000*1000
#@date 20221104
#@version 1.0
# #打包原图0.2.py ok
import os,glob,shutil
from PIL import Image

from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
#img=Image.open("")
# files=glob.glob("*[0-9]*\\白底移到*.py")
# for file in files:
# if os.path.isfile(file):
# os.remove(r""+file)

dirs=glob.glob("*.jpg")#获取OEM文件夹
# 输入缩放尺寸
size=input('请输入缩放尺寸:')
size=int(size)
#缩放水印图
for dir in dirs:
	file=dir
	print(dir,"\n")
	# if not os.path.exists(dir+"\\原图\\"):
	# 	os.mkdir(dir+"\\原图\\")#创建原图文件夹
	# 	print(dir+"\\原图\\")
	# files= glob.glob(dir+"\\水印\\*.jpg")#获取所有白底jpg文件
	# files= glob.glob(dir+"\\原图\\*.jpg")#获取所有jpg文件
	# print(files)
	print(file)
	try:
		print("源文件"+file,"目标文件"+dir+"\\原图\\")
		img=Image.open(file)
		img=img.resize((size,size))
		img.save(file)
	except:
		print('异常')
		continue
	# for file in files:
	# 	print(file)
	# 	# shutil.move(file,dir+"\\原图\\")
	# 	print("源文件"+file,"目标文件"+dir+"\\原图\\")
	# 	img=Image.open(file)
	# 	img=img.resize((1000,1000))
	# 	img.save(file)
#os.mkdir(file+r""+"原图")
# if os.path.isfile(file):
# os.remove(r""+file)

# import shutil
# shutil.move(r".\白底\7.jpg",r".\水印\1.jpg")
# shutil.move(r".\白底\8.jpg",r".\水印\2.jpg")
# shutil.move(r".\白底\9.jpg",r".\水印\3.jpg")
# shutil.move(r".\白底\10.jpg",r".\水印\4.jpg")
# shutil.move(r".\白底\11.jpg",r".\水印\5.jpg")
# shutil.move(r".\白底\12.jpg",r".\水印\6.jpg")
# #创建文件夹
# import os,glob
# os.mkdir("原图")
# files=glob.glob(r".\*[0-9]*")
# for file in files:
#  # print(file)
#  shutil.move(r""+file,r".\原图")