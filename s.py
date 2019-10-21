import pytesseract 
import PIL
from PIL import Image
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


#im = cv2.imread("temp2.png")

#text = str(((pytesseract.image_to_string(im)))) 

def getVal(im):
	text = str(((pytesseract.image_to_string(im))))

	yinc = 72
	cury = 0

	emptyPositions = []
	cellindex = 0

	while cury+yinc < im.shape[0]:


		img = im[cury:cury+yinc,0:150]
#		grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		grayImage = img
		(thresh, bw) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
		
		flag = 0

		for row in bw:
			for col in row:
					if col != 255:
						flag = 1

		if flag == 0:
			emptyPositions.append(cellindex)
			
		cury += yinc
		cellindex += 1
		

	toInsert = "null"

	splitted = text.split('\n')
	for ele in splitted:
		if ele == '':
			splitted.remove(ele)
			
	for ele in emptyPositions:
		splitted.insert(ele,toInsert)
		
	str1 = ""
	for i in range(len(splitted)):
		if i != len(splitted) - 1:
			str1+=splitted[i]+"\n\n"
		else:
			str1+=splitted[i]
			
#	print(str1)
	return str1





