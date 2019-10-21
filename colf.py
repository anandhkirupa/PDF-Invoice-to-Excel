import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def getValue(gray):


	outputString = ""

	outList=[]


	#gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  

	#--- performing Otsu threshold ---
	ret,thresh1 = cv2.threshold(gray, 0, 255,cv2.THRESH_OTSU|cv2.THRESH_BINARY_INV)
	#cv2.imshow('thresh1', thresh1)

	#--- choosing the right kernel
	#--- kernel size of 3 rows (to join dots above letters 'i' and 'j')
	#--- and 10 columns to join neighboring letters in words and neighboring words
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	#cv2.imshow('dilation', dilation)

	#---Finding contours ---
	_, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

	im2 = gray.copy()
	for cnt in contours:
			x, y, w, h = cv2.boundingRect(cnt)
			#cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
			mycropped = im2[y:y+h,x:x+w]
			text = str(((pytesseract.image_to_string(mycropped))))
			#outputString+=text+"\n\n\n\n"
			text = text.replace('\n',' ')
			
			outList.append(text)		
	'''
	cv2.imwrite("tttt.png",im2)
	imS = cv2.resize(im2, (960, 540))
	cv2.imshow('final', im2)
	cv2.waitKey(0)
	'''

	outList = outList[::-1]
	for val in outList:
		if val == "":
			outList.remove(val)

	outstring = ""
	for i in range(len(outList)):
		if i != len(outList) - 1:
			outstring+=outList[i]+"\n\n"
		else:
			outstring+=outList[i]
		
	return outstring