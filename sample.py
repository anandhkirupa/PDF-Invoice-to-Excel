import cv2
import pytesseract
from PIL import Image
import pdf2image
import math
import xlwt
import glob,os
import shutil
from pdf2image import convert_from_path
shutil.rmtree('img/')
shutil.rmtree('imgs/')
shutil.rmtree('out/')

os.makedirs('img/')

os.makedirs('imgs/')
os.makedirs('out/')
allImages = pdf2image.convert_from_path('Sunil2/t52.pdf', output_folder='img/', fmt='jpg')
numImages = len(allImages)

os.chdir("img/")

def getMatch(i):
	if numImages >= 10:
		if i<10:
			match = "0"+str(i)
		else:
			match = str(i)
	else:
		match = str(i)
	return match

flag = 0
fileName = "abcd"
print(numImages)
#if numImages <= 2:
#	print("Number of images is less than 2")
#else:
for i in range(numImages , 0 , -1):
	print("jasdfhas")
	for image in glob.glob("*.jpg"):
		if numImages >= 10:
			lastImage = image[len(image)-6:len(image)-4]
		else:
			lastImage = image[len(image)-5]
		match = getMatch(i)
		if lastImage == match:
			print("knasdjfnas")
			img = cv2.imread(image)
			if lastImage == "1":
				cropped = img[715:1700,0:2200]
			else:
				cropped = img[200:1700,0:2200]
			gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
			thresh, blackAndWhiteImage = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
			edges = cv2.Canny(blackAndWhiteImage, 80, 120, thresh)
			lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1)
			try:

				for line in lines[0]:
					pt1 = (line[0],line[1])
					pt2 = (line[2],line[3])
					cv2.line(img, pt1, pt2, (0,0,255), 3)
					print(pt1, pt2)
#				cv2.imwrite("temp2.jpg", img)
				flag = 1
				fileName = image
				print("found if")
				break
			except:
				print("")
	if flag == 1:
		break
os.chdir("../")
def getVal():	
	return fileName, lastImage