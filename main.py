import os
import time
import sys
import random
for i in range(101):
	print("Loading engine: "+str(i)+" %",end="\r")
	time.sleep(random.uniform(0.05,0.1))

def timer(func):
	def wrapper(*args,**kwargs):
		before = time.time()
		var=func(*args,**kwargs)
		print('The virus removing proccess took {0} seconds to execute'.format(str(time.time()-before).replace('e','x10^')))
		return var
	return wrapper

global checking_path

global python_version

python_version=int(sys.version[0])

if python_version==2:
	print("[Warning!!] You are running \"Files.exe remover\" on Python 2. This app will not be developed anymore using Python 2.\n[Sollution!!]Upgrade your Python to Python 3 for staying uppdated")
	checking_path=str(raw_input("\nEnter the path to check: "))
elif python_version==3:
	checking_path=str(input("Enter the path to check: "))

@timer
def scanFiles_exe(path):
	virusFound=[]
	for root, directory,files in os.walk(path):
		for i in directory:
			try:
				file__=open("{}/{}/{}.exe".format(root,i,i),"r")
				file__.close()
				virusFound.append("{}/{}/{}.exe".format(root,i,i))
			except NotADirectoryError:
				pass
			except FileNotFoundError:
				pass
			except FileExistsError:
				pass
	return virusFound

def virus_found(lst):
	for i in lst:
		print("Virus found at {}".format(i))
	choice=""
	if python_version==2:
		choice=raw_input("\n\nDo you want to delete them? [Y/n] ")
	elif python_version==3:
		choice=input("\n\nDo you want to delete them? [Y/n] ")
	return choice.lower()

def removeVirus(lst):
	for i in lst:
		os.remove(i)
virus_list=scanFiles_exe(checking_path)
if(len(virus_list)>0):
	decision=virus_found(virus_list)
if(decision=='y'):
	removeVirus(virus_list)
elif(decision=='n'):
	print("Virus scanned but not deleted!!!")
else:
	print("Wrong choice made!! Terminating.....")


print("\n\nDeveloped by NurTasin. You can get latest update of this tool at https://github.com/NurTasin/Files.exeRemover.git")
print("Feat. Guido van Rossum, father of Python Programming Language.")
print("Special Thanks to Rasidul Islam Sajib for his lazyness to delete these viruses.")
print("\n\nCopyright 2020 Nur Mahmud Ul Alam Tasin.")
