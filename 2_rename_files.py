import os

def rename_files():
	file_list = os.listdir(r"/home/yoge/git/Python/test")
	c_path = os.getcwd()
	print("Current working dir : "+c_path)
	os.chdir(r"/home/yoge/git/Python/test")

	for file_name in file_list:
		print("Old Name : "+file_name)
		print("New Name : "+file_name.translate(None,"0123456789"))
		os.rename(file_name,file_name.translate(None,"0123456789"))
	os.chdir(c_path)
rename_files()