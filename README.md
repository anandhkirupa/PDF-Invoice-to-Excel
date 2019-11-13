A Simple program which converts a PDF (Invoice format) into Image, and OCR has been applied to read the text in that image.

The PDF consists of scanned images.

The converted images from the pdf's are pre-processed and read it in column manner through Pytesseract and saved it in text, later all recognized text is feeded into the Excel file for later use.


Pre-requisites:

pip install opencv-python

pip install pytesseract

pip install image

pip install pdf2image

pip install math

pip install xlwt

pip install glob

pip install os

pip install pytest-shutil
