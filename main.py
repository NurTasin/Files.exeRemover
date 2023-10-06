import os
import time
import sys
import random

def timer(func):
	def wrapper(*args,**kwargs):
		before = time.time()
		var=func(*args,**kwargs)
		print('The virus removing proccess took {0} seconds to execute'.format(str(time.time()-before).replace('e','x10^')))
		return var
	return wrapper

python_version=int(sys.version[0])
checking_path=str(input("Enter the path to check: "))

@timer
def scanFiles_exe(path):
	virusFound=[]
	for root, directory,files in os.walk(path):
		for i in directory:
			print(os.path.join(root,i))
			if os.path.exists(os.path.join(root,i,f"{i} .exe")):
				virusFound.append(os.path.join(root,i,f"{i} .exe"))

	return virusFound

def virus_found(lst):
	for i in lst:
		print("Virus found at {}".format(i))
	
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
