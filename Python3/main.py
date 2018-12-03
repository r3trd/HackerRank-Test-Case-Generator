import os
import random
import sys
import zipfile
import math
import time
import shutil

try:
	os.mkdir('input')
	os.mkdir('output')
except OSError:
	pass

file_name = input("Enter the name of the file (e.g. logic.py) : ").strip()
ext = file_name.split('.')

exe1 = ' '
exe2 = ' '
req = 1

if (ext[-1]=='py') :
    req = 0
	exe2 = 'python '+ file_name +' < input/input%02d.txt > output/output%02d.txt'
elif (ext[-1] == 'java') :
	exe1 = 'javac ' + file_name
	exe2 = 'java '+ ext[0] +' < input/input%02d.txt > output/output%02d.txt'
elif (ext[-1] == 'cpp') :
	exe1 = 'g++ -o ' + ext[0] + ' ' + file_name
	exe2 = './' + ext[0] +' < input/input%02d.txt > output/output%02d.txt'
elif (ext[-1] == 'c') :
	exe1 = 'gcc -o ' + ext[0] + ' ' + file_name
	exe2 = './' + ext[0] +' < input/input%02d.txt > output/output%02d.txt'
else :
	print("Sorry! The extension is not supported.\n")
	exit(0) 

pwr = math.pow
rint = random.randint

tf = 10 # number of test files, change it according to you.


for i in range(0, tf + 1):
	print ('Generating:', i, file=sys.stderr)
	sys.stdout = open('input/input%02d.txt' % i, 'w')
	
	'''
	Input area will start here,
	everything that you print out here will be taken as input in your logic file.
	You can set difficulty of test cases all by you.
	'''

	### Input File Printing Start
	x = rint(1, 100) # number of test cases in (1,100)
	print(x) # Prints x into input file
	for z in range (x):
		print(rint(1, 100000)) 
	sys.stdout.close()
	### Input File Printing Ends


with zipfile.ZipFile('test-cases.zip', 'w', zipfile.ZIP_DEFLATED) as zf:
	for i in range(0, tf + 1):
		print('Zipping:', i, file=sys.stderr)
		start = time.time()
		if (req):
			os.system(exe1)
		os.system(exe2 % (i, i))
		end = time.time()
		print('Time taken to execute this TC %02f' %(end - start), file=sys.stderr)
		zf.write('input/input%02d.txt' % i)
		zf.write('output/output%02d.txt' % i)

shutil.rmtree('input')
shutil.rmtree('output')