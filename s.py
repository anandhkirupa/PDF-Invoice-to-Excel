import cv2
import pytesseract
import math

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

def getVal(x):	


	outputString = ""

	outList=[]

	yHeight = 72/2

	threshold_for_null = 60

	prevvalueup = 0
	prevvaluedown = 0
	
	img =x
	
	gray = img
	#img = cv2.imread(x)
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

	im2 = img.copy()

	contours=contours[::-1]

	for cnt in contours:
			x, y, w, h = cv2.boundingRect(cnt)
			#cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
			
			mycropped = im2[y:y+h,x:x+w]
			text = str(((pytesseract.image_to_string(mycropped))))
			#print(text)
			if(text != ""):
					
				#print(str(x) +" and " + str(x+w))
				yup = int(y+((h)/2)+yHeight)
				ydown = int(y + ((h)/2) - yHeight)

				#print(" yup: " + str(yup) + " ydown " + str(ydown) + " prevvalueup" + str(prevvalueup) + " prevvaluedown : "+ str(prevvaluedown))
				cv2.rectangle(im2, (x, yup), (x + w, ydown), (0, 255, 0), 2)
				
				diff = ydown - prevvalueup
				
				if diff >= threshold_for_null:
					#print("it is null \n\n")	
					number_of_null = math.floor(diff/threshold_for_null)
					for myi in range(number_of_null):
						outputString += "null\n\n"
				print(text + " diff: " + str(diff))            
				outputString = outputString + text + "\n\n"
					#print(text+"\n\n")
				#print(prevvalueup-ydown)
				#print(text+"\n\n\n"+outputString+"\n\n\n\n\n")
				prevvalueup = yup

				
				#print(outputString)
				#imS = cv2.resize(im2, (960, 540))
				#cv2.imshow('final', imS)
				#cv2.waitKey(0)
				
				#print("GOT it" + text)


				#break
			#outputString+=text+"\n\n\n\n"
			#text = text.replace('\n',' ')
			
			#outList.append(text)

		
	return (outputString)		
