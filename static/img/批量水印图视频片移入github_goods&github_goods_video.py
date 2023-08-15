#叶志豪 1119 1206 1220添加跳过
#批量水印图片移入github_goods，用于上传github作为速卖通图片;批量产品视频移入github_goods_video 添加了支持mov文件和记录型号&判断2-6jpg图片存在
#v1.1
import shutil
import glob
dirs=glob.glob(".\\*[0-9]*\\")
#获取桌面OEM文件夹
import os
if not os.path.exists("D:\\github_goods"):
	os.mkdir("D:\\github_goods")
#创建文件记录编号
if not os.path.exists('dirs.txt'):
	f = open("dirs.txt", "w")
	f.close()
for dir in dirs:
	print(dir)
	print(dir[2:-1]) #15239247暗红 完整OEM
	#写入编号
	f=open("dirs.txt","a")
	f.write(dir[2:-1]+"\n")
	f.close()
	#重赋值dir
	dir=dir[2:-1]
	if os.path.exists(dir+"\\水印\\1.jpg"):
		shutil.copy(dir+"\\水印\\1.jpg","D:\\github_goods\\"+dir+"_1.jpg")
	if os.path.exists(dir + "\\水印\\2.jpg"):
		shutil.copy(dir+"\\水印\\2.jpg","D:\\github_goods\\"+dir+"_2.jpg")
	if os.path.exists(dir + "\\水印\\3.jpg"):
		shutil.copy(dir+"\\水印\\3.jpg","D:\\github_goods\\"+dir+"_3.jpg")
	if os.path.exists(dir + "\\水印\\4.jpg"):
		shutil.copy(dir+"\\水印\\4.jpg","D:\\github_goods\\"+dir+"_4.jpg")
	if os.path.exists(dir + "\\水印\\5.jpg"):
		shutil.copy(dir+"\\水印\\5.jpg","D:\\github_goods\\"+dir+"_5.jpg")
	if os.path.exists(dir + "\\水印\\6.jpg"):
		shutil.copy(dir+"\\水印\\6.jpg","D:\\github_goods\\"+dir+"_6.jpg")
	# shutil.move(r""+pics[1],r".\水印\2.jpg")
	# shutil.move(r""+pics[2],r".\水印\3.jpg")
	# shutil.move(r""+pics[3],r".\水印\4.jpg")
	# shutil.move(r""+pics[4],r".\水印\5.jpg")
	# shutil.move(r""+pics[5],r".\水印\6.jpg")
#移动视频到
if not os.path.exists("D:\\github_goods_video"):
	os.mkdir("D:\\github_goods_video")
for dir in dirs:
	vids = glob.glob(dir + "\\*.mp4")# 获取视频
	#不同格式视频
	if not len(vids)==0:
		vid=glob.glob(dir+"\\*.mp4")[0]#获取视频
		# 复制并重命名为{OE}.mp4
		dir = dir[2:-1]
		shutil.copy(vid, "D:\\github_goods_video\\" + dir + ".mp4")
		print(vid)
	else:
		if len(glob.glob(dir + "\\*.mov"))==0:
			print(dir+"没有视频")
			continue
		vid = glob.glob(dir + "\\*.mov")[0]  # 获取视频
		# 复制并重命名为{OE}.mp4
		dir = dir[2:-1]
		shutil.copy(vid, "D:\\github_goods_video\\" + dir + ".mov")
		print(vid)


input("任意键退出:")