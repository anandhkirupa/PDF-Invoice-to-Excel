# Write Python code here 
# import the necessary packages 
import cv2 
import pytesseract 
from PIL import Image
import pdf2image
import math
import xlwt
import glob,os
import shutil
import sample
import os.path
import glob
import s
import colf



flag1 = 0
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

src_files = os.listdir('img')
for file_name in src_files:
    full_file_name = os.path.join('img', file_name)
    if os.path.isfile(full_file_name):
        shutil.copy(full_file_name, 'imgs')

dir = 'imgs/'
numImages = len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

os.chdir('imgs/')
allImages = glob.glob('*.jpg')
os.chdir('../')


start1 = [33,715]
end1 = [170,1690]

start2 = [170,715]
end2 = [325,1690]

start3 = [325,715]
end3 = [430,1690]

start4 = [470,715]
end4 = [570,1690]

start6 = [725,715]
end6 = [845,1690]

start7 = [845,715]
end7 = [1120,1690]

start8 = [1150,715]
end8 = [1270,1690]

start9 =[1280,715]
end9 = [1390,1690]

start10 =[1400,715]
end10 = [1525,1690]

start11 =[1610,715]
end11 = [1690,1690]

start12 =[1700,715]
end12 = [1850,1690]

start13 =[1850,715]
end13 = [2050,1690]

start14 =[2100,715]
end14 = [2158,1690]

starts1 = [start1,start2,start3,start4,start6,start7,start8,start9,start10,start11,start12,start13,start14]
ends1 = [end1,end2,end3,end4,end6,end7,end8,end9,end10,end11,end12,end13,end14]

currentIndex = 1

lastFile,numImage = sample.getVal()
print(lastFile, numImage)
	
if numImages == 1 and currentIndex ==1 and numImage == '1':
	for currentImage in allImages:
		img = cv2.imread("imgs/"+currentImage)
		cropped = img[715:1700,0:2200]
		gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
		edges = cv2.Canny(gray, 80, 120)
		lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
		for line in lines[0]:
			pt1 = (line[0],line[1])
			pt2 = (line[2],line[3])
			cv2.line(cropped, pt1, pt2, (0,0,255), 3)
#			print(pt1, pt2)
			
		abcd = img[0:pt1[1]+715,0:2200]
		
		endy = pt1[1]+715

		start1 = [33,715]
		end1 = [170,endy]

		start2 = [170,715]
		end2 = [325,endy]

		start3 = [325,715]
		end3 = [430,endy]

		start4 = [470,715]
		end4 = [570,endy]

		start6 = [725,715]
		end6 = [845,endy]

		start7 = [845,715]
		end7 = [1120,endy]

		start8 = [1150,715]
		end8 = [1270,endy]

		start9 =[1280,715]
		end9 = [1390,endy]

		start10 =[1400,715]
		end10 = [1525,endy]

		start11 =[1610,715]
		end11 = [1690,endy]

		start12 =[1700,715]
		end12 = [1850,endy]

		start13 =[1850,715]
		end13 = [2050,endy]

		start14 =[2100,715]
		end14 = [2158,endy]
		
		starts1 = [start1,start2,start3,start4,start6,start7,start8,start9,start10,start11,start12,start13,start14]
		ends1 = [end1,end2,end3,end4,end6,end7,end8,end9,end10,end11,end12,end13,end14]

		ch='a'
		x = chr(ord(ch))
		for i in range(len(starts1)):
			filename = "out/out_text"+str(currentIndex) +"_"+str(x)+".txt"
			file = open(filename, "a")
			
			cropped = abcd[starts1[i][1]:ends1[i][1],starts1[i][0]:ends1[i][0]]
			gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
			cv2.imwrite("out/out_text"+str(currentIndex) +"_"+str(x)+".png", gray)
			
#			text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png"))))) 
			if str(x) == "b" or str(x) == "f" or str(x) == "k":
				if str(x) == "b":
					text = s.getVal(gray)
					print(text)
				else:
					text = colf.getValue(gray)
			else:
				text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png")))))
			file.write(text)
			file.close()
			x = chr(ord(x) + 1)
			
	currentIndex+=1
		
	os.chdir("out/")
		
	base = "out_text"

	ch = 'a'
	x = chr(ord(ch))

	filenames = []

	for j in range(13):
		single = []
		for i in range(1,numImages+1):
		
			filename = base+str(i)+"_"+str(x)+".txt"
			single.append(filename)
			
		x = chr(ord(x)+1)
		filenames.append(single)

	ch = 'a'
	x = chr(ord(ch))


	for filelist in filenames:
		outfile = "outputfile"+str(x)+".txt"
		file = open(outfile,"a")
		
		for individual in filelist:
			input = open(individual,"r")
			allLines = input.readlines()
			
			for line in allLines:
				file.write(str(line))
			input.close()
			file.write("\n\n")
		file.close()
		x = chr(ord(x)+1)
				




	tochange = "outputfilec.txt"
	file = open(tochange,"r")

	cleanedText = ""

	allLines = file.readlines()

	for line in allLines:
		if line != "\n":
			cleanedText+=line

	file.close()

	file = open(tochange,"w")
	file.write(cleanedText)
	file.close()


	file = open(tochange,"r")
	outfile = open('bbbb.txt',"a")

	allLines = file.readlines()

	value = ""
	counter = 1
	for i in allLines:
		value += i.replace('\n',',')
	#	print(i)
		if counter == 3:
			value = value[:-1]
			outfile.write(value + "\n\n")
			value = ""
			counter = 1
		else:
			counter+=1

	file.close()
	outfile.close()

	with open("bbbb.txt") as f:
		with open("outputfilec.txt", "w") as f1:
			for line in f:
				f1.write(line)

				

		

	file = open('outputfilef.txt',"r")
	outfile = open('aaaa.txt',"a")

	cleanedText = ""

	allLines = file.readlines()

	cleanValue = ""

	prev = 0

	for i in range(len(allLines)):

		thisLine = allLines[i]
		if thisLine == "\n":
			outfile.write(cleanValue+"\n\n")
			cleanValue = ""
		else:
			cleanLine = thisLine.replace("\n"," ")
			cleanValue += cleanLine
		
	file.close()

	outfile.close()


	with open("aaaa.txt") as f:
		with open("outputfilef.txt", "w") as f1:
			for line in f:
				f1.write(line)


	mergedfilenames = []

	ch = 'a'
	x = chr(ord(ch))

	for j in range(13):

		filename = "outputfile"+str(x)+".txt"
		mergedfilenames.append(filename)
			
		x = chr(ord(x)+1)
		
	for tochange in mergedfilenames:
		file = open(tochange,"r")

		cleanedText = ""

		allLines = file.readlines()

		for line in allLines:
			if line != "\n":
				cleanedText+=line

		file.close()

		file = open(tochange,"w")
		file.write(cleanedText)
		file.close()


	book = xlwt.Workbook()
	ws = book.add_sheet('First Sheet')

	headers = ["Work Order ID", "Reference Doc","Applicable Rate of Tax", "HSN","Original Reference Number", "Period End Date", "Description", "Taxable Amount", "Central Tax", "State Tax", "Integrated Tax", "Total GST Amount", "Amount Including GST", "Currency"]

	for i in range(len(headers)):
		ws.write(0, i, headers[i])


	verticalIndex = 1
	horizontalIndex = 0
	#a b d e g h i j k l m

	easyfiles= ["outputfilea.txt","outputfileb.txt","outputfilec.txt","outputfiled.txt","outputfilee.txt","outputfilef.txt","outputfileg.txt","outputfileh.txt","outputfilei.txt","outputfilej.txt","outputfilek.txt","outputfilel.txt","outputfilem.txt"]

	easycolNums = [0,1,2,3,5,6,7,8,9,10,11,12,13]

	#for tre in range(len(easycolNums)):
	#	easycolNums[tre]+=1

	vert = 1
	totalrows = 0
	for tt in range (len(easyfiles)):
		curfile = easyfiles[tt]
		file = open(curfile,"r")
		allLines = file.readlines()
		
		for j in range(len(allLines)):
			if(allLines[j] != "\n"):
				if curfile == "outputfilem.txt":
					totalrows+=1
				ws.write(vert,easycolNums[tt], allLines[j])
				#print(easycolNums[tt])
				vert+=1
		vert=1
		

	vert = 1
	for ss in range (math.floor(totalrows)):
		ws.write(vert,4, "null")
		vert+=1
		
	book.save('../Excelfile' + '.xls')
	
else:
	lastFile,numImage = sample.getVal()
	print(lastFile, numImage)
	print(type(numImage))
	
	for currentImage in allImages:
		print(currentImage)
		img = cv2.imread("imgs/"+currentImage)
		if currentImage == lastFile:
			flag1 = 1
			print(currentImage)
			if numImage == "1":
				print("first image")
				cropped = img[715:1700,0:2200]
			else:
				cropped = img[181:1700,0:2200]
			cv2.imwrite("cropped.png",cropped)

			print("Cropped")
			img1 = cv2.imread("cropped.png")
			gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
			edges = cv2.Canny(gray, 80, 120)
			lines = cv2.HoughLinesP(edges, 1, math.pi/2, 2, None, 30, 1);
			for line in lines[0]:
				pt1 = (line[0],line[1])
				pt2 = (line[2],line[3])
				cv2.line(img1, pt1, pt2, (0,0,255), 3)
				print(pt1, pt2)
			cv2.imwrite("temp2.jpg",img1)
			if numImage == "1":
				abcd = img[0:pt1[1]+715,0:2200]
				
				endy = pt1[1]+715

				start1 = [33,715]
				end1 = [170,endy]

				start2 = [170,715]
				end2 = [325,endy]

				start3 = [325,715]
				end3 = [430,endy]

				start4 = [470,715]
				end4 = [570,endy]

				start6 = [725,715]
				end6 = [845,endy]

				start7 = [845,715]
				end7 = [1120,endy]

				start8 = [1150,715]
				end8 = [1270,endy]

				start9 =[1280,715]
				end9 = [1390,endy]

				start10 =[1400,715]
				end10 = [1525,endy]

				start11 =[1610,715]
				end11 = [1690,endy]

				start12 =[1700,715]
				end12 = [1850,endy]

				start13 =[1850,715]
				end13 = [2050,endy]

				start14 =[2100,715]
				end14 = [2158,endy]
			else:
				abcd = img[0:pt1[1]+180,0:2200]
			
				endy = pt1[1]+180

				start1 =[33,180]
				end1 = [170,endy]

				start2 =[150,180]
				end2 = [320,endy]

				start3 =[330,180]
				end3 = [450,endy]

				start4 =[460,180]
				end4 = [560,endy]

				start6 =[720,180]
				end6 = [840,endy]

				start7 =[850,180]
				end7 = [1090,endy]

				start8 =[1130,180]
				end8 = [1280,endy]

				start9 =[1300,180]
				end9 = [1400,endy]

				start10 =[1420,180]
				end10 = [1550,endy]

				start11 =[1580,180]
				end11 = [1680,endy]

				start12 =[1720,180]
				end12 = [1830,endy]

				start13 =[1890,180]
				end13 = [2050,endy]

				start14 =[2090,180]
				end14 = [2160,endy]
			
			starts1 = [start1,start2,start3,start4,start6,start7,start8,start9,start10,start11,start12,start13,start14]
			ends1 = [end1,end2,end3,end4,end6,end7,end8,end9,end10,end11,end12,end13,end14]

			ch='a'
			x = chr(ord(ch))
			for i in range(len(starts1)):
				filename = "out/out_text"+str(currentIndex) +"_"+str(x)+".txt"
				file = open(filename, "a")
				
				cropped = abcd[starts1[i][1]:ends1[i][1],starts1[i][0]:ends1[i][0]]
				gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
				cv2.imwrite("out/out_text"+str(currentIndex) +"_"+str(x)+".png", gray)
				
#				text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png"))))) 
				if str(x) == "b" or str(x) == "f" or str(x) == "k":
					if str(x) == "b":
						text = s.getVal(gray)
						print(text)
					else:
						text = colf.getValue(gray)
				else:
					text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png")))))
					
				file.write(text)
				file.close()
				x = chr(ord(x) + 1)
			os.chdir("out/")
		
			base = "out_text"

			ch = 'a'
			x = chr(ord(ch))

			filenames = []

			for j in range(13):
				single = []
				for i in range(1,int(numImage)+1):
					filename = base+str(i)+"_"+str(x)+".txt"
					single.append(filename)
				x = chr(ord(x)+1)
				filenames.append(single)

			ch = 'a'
			x = chr(ord(ch))


			for filelist in filenames:
				outfile = "outputfile"+str(x)+".txt"
				file = open(outfile,"a")
				
				for individual in filelist:
					input = open(individual,"r")
					allLines = input.readlines()
					
					for line in allLines:
						file.write(str(line))
					input.close()
					file.write("\n\n")
				file.close()
				x = chr(ord(x)+1)
						




			tochange = "outputfilec.txt"
			file = open(tochange,"r")

			cleanedText = ""

			allLines = file.readlines()

			for line in allLines:
				if line != "\n":
					cleanedText+=line

			file.close()

			file = open(tochange,"w")
			file.write(cleanedText)
			file.close()


			file = open(tochange,"r")
			outfile = open('bbbb.txt',"a")

			allLines = file.readlines()

			value = ""
			counter = 1
			for i in allLines:
				value += i.replace('\n',',')
			#	print(i)
				if counter == 3:
					value = value[:-1]
					outfile.write(value + "\n\n")
					value = ""
					counter = 1
				else:
					counter+=1

			file.close()
			outfile.close()

			with open("bbbb.txt") as f:
				with open("outputfilec.txt", "w") as f1:
					for line in f:
						f1.write(line)

						

			mergedfilenames = []

			ch = 'a'
			x = chr(ord(ch))

			for j in range(13):

				filename = "outputfile"+str(x)+".txt"
				mergedfilenames.append(filename)
					
				x = chr(ord(x)+1)
				
			for tochange in mergedfilenames:
				file = open(tochange,"r")

				cleanedText = ""

				allLines = file.readlines()

				for line in allLines:
					if line != "\n":
						cleanedText+=line

				file.close()

				file = open(tochange,"w")
				file.write(cleanedText)
				file.close()


			book = xlwt.Workbook()
			ws = book.add_sheet('First Sheet')

			headers = ["Work Order ID", "Reference Doc","Applicable Rate of Tax", "HSN","Original Reference Number", "Period End Date", "Description", "Taxable Amount", "Central Tax", "State Tax", "Integrated Tax", "Total GST Amount", "Amount Including GST", "Currency"]

			for i in range(len(headers)):
				ws.write(0, i, headers[i])


			verticalIndex = 1
			horizontalIndex = 0
			#a b d e g h i j k l m

			easyfiles= ["outputfilea.txt","outputfileb.txt","outputfilec.txt","outputfiled.txt","outputfilee.txt","outputfilef.txt","outputfileg.txt","outputfileh.txt","outputfilei.txt","outputfilej.txt","outputfilek.txt","outputfilel.txt","outputfilem.txt"]

			easycolNums = [0,1,2,3,5,6,7,8,9,10,11,12,13]

			#for tre in range(len(easycolNums)):
			#	easycolNums[tre]+=1

			vert = 1
			totalrows = 0
			for tt in range (len(easyfiles)):
				curfile = easyfiles[tt]
				file = open(curfile,"r")
				allLines = file.readlines()
				
				for j in range(len(allLines)):
					if(allLines[j] != "\n"):
						if curfile == "outputfilem.txt":
							totalrows+=1
						ws.write(vert,easycolNums[tt], allLines[j])
						#print(easycolNums[tt])
						vert+=1
				vert=1
				

			vert = 1
			for ss in range (math.floor(totalrows)):
				ws.write(vert,4, "null")
				vert+=1
				
			book.save('../Excelfile' + '.xls')
			if flag1 == 1:
				break
		elif currentIndex == 1:
			ch = 'a'
			x = chr(ord(ch))
			for i in range(len(starts1)):
				filename = "out/out_text"+str(currentIndex) +"_"+str(x)+".txt"
				file = open(filename, "a")
				
				cropped = img[starts1[i][1]:ends1[i][1],starts1[i][0]:ends1[i][0]]
				gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
				cv2.imwrite("out/out_text"+str(currentIndex) +"_"+str(x)+".png", gray)

#				text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png"))))) 
				if str(x) == "b" or str(x) == "f" or str(x) == "k":
					if str(x) == "b":
						text = s.getVal(gray)
						print(text)
					else:
						text = colf.getValue(gray)
				else:
					text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png")))))
				file.write(text)
				file.close()
				x = chr(ord(x)+1)
				
				
		else:
			for k in range(len(starts1)):
				starts1[k][1] = 180
			ch = 'a'
			x = chr(ord(ch))
			for i in range(len(starts1)):
			
				filename = "out/out_text"+str(currentIndex) +"_"+str(x)+".txt"
				file = open(filename, "a")
				
				cropped = img[starts1[i][1]:ends1[i][1],starts1[i][0]:ends1[i][0]]
				gray = cv2.cvtColor(cropped, cv2.COLOR_BGR2GRAY)
				cv2.imwrite("out/out_text"+str(currentIndex) +"_"+str(x)+".png", gray)

#				text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png"))))) 
				
				if str(x) == "b" or str(x) == "f" or str(x) == "k":
					if str(x) == "b":
						text = s.getVal(gray)
						print(text)
					else:
						text = colf.getValue(gray)
				else:
					text = str(((pytesseract.image_to_string(Image.open("out/out_text"+str(currentIndex) +"_"+str(x)+".png")))))
				
				file.write(text)
				file.close()	
				x = chr(ord(x)+1)
			
		currentIndex+=1
'''

			
	os.chdir("out/")
		
	base = "out_text"

	ch = 'a'
	x = chr(ord(ch))

	filenames = []

	for j in range(13):
		single = []
		for i in range(1,numImages+1):
			filename = base+str(i)+"_"+str(x)+".txt"
			single.append(filename)
		x = chr(ord(x)+1)
		filenames.append(single)

	ch = 'a'
	x = chr(ord(ch))


	for filelist in filenames:
		outfile = "outputfile"+str(x)+".txt"
		file = open(outfile,"a")
		
		for individual in filelist:
			input = open(individual,"r")
			allLines = input.readlines()
			
			for line in allLines:
				file.write(str(line))
			input.close()
			file.write("\n\n")
		file.close()
		x = chr(ord(x)+1)
				




	tochange = "outputfilec.txt"
	file = open(tochange,"r")

	cleanedText = ""

	allLines = file.readlines()

	for line in allLines:
		if line != "\n":
			cleanedText+=line

	file.close()

	file = open(tochange,"w")
	file.write(cleanedText)
	file.close()


	file = open(tochange,"r")
	outfile = open('bbbb.txt',"a")

	allLines = file.readlines()

	value = ""
	counter = 1
	for i in allLines:
		value += i.replace('\n',',')
	#	print(i)
		if counter == 3:
			value = value[:-1]
			outfile.write(value + "\n\n")
			value = ""
			counter = 1
		else:
			counter+=1

	file.close()
	outfile.close()

	with open("bbbb.txt") as f:
		with open("outputfilec.txt", "w") as f1:
			for line in f:
				f1.write(line)

				

	mergedfilenames = []

	ch = 'a'
	x = chr(ord(ch))

	for j in range(13):

		filename = "outputfile"+str(x)+".txt"
		mergedfilenames.append(filename)
			
		x = chr(ord(x)+1)
		
	for tochange in mergedfilenames:
		file = open(tochange,"r")

		cleanedText = ""

		allLines = file.readlines()

		for line in allLines:
			if line != "\n":
				cleanedText+=line

		file.close()

		file = open(tochange,"w")
		file.write(cleanedText)
		file.close()


	book = xlwt.Workbook()
	ws = book.add_sheet('First Sheet')

	headers = ["Work Order ID", "Reference Doc","Applicable Rate of Tax", "HSN","Original Reference Number", "Period End Date", "Description", "Taxable Amount", "Central Tax", "State Tax", "Integrated Tax", "Total GST Amount", "Amount Including GST", "Currency"]

	for i in range(len(headers)):
		ws.write(0, i, headers[i])


	verticalIndex = 1
	horizontalIndex = 0
	#a b d e g h i j k l m

	easyfiles= ["outputfilea.txt","outputfileb.txt","outputfilec.txt","outputfiled.txt","outputfilee.txt","outputfilef.txt","outputfileg.txt","outputfileh.txt","outputfilei.txt","outputfilej.txt","outputfilek.txt","outputfilel.txt","outputfilem.txt"]

	easycolNums = [0,1,2,3,5,6,7,8,9,10,11,12,13]

	#for tre in range(len(easycolNums)):
	#	easycolNums[tre]+=1

	vert = 1
	totalrows = 0
	for tt in range (len(easyfiles)):
		curfile = easyfiles[tt]
		file = open(curfile,"r")
		allLines = file.readlines()
		
		for j in range(len(allLines)):
			if(allLines[j] != "\n"):
				if curfile == "outputfilem.txt":
					totalrows+=1
				ws.write(vert,easycolNums[tt], allLines[j])
				#print(easycolNums[tt])
				vert+=1
		vert=1
		

	vert = 1
	for ss in range (math.floor(totalrows)):
		ws.write(vert,4, "null")
		vert+=1
		
	book.save('../Excelfile' + '.xls')
	

'''