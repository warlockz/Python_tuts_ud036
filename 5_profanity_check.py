import urllib


def read_text():
	filetext = open("/home/yoge/git/Python_tuts_ud036/test/a.txt")
	contents_of_file = filetext.read()
	filetext.close()
	check_profanity(contents_of_file)

def check_profanity(text):
	connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=fuck"+text)
	output_response = connection.read()
	connection.close()
	#print(output_response)
	if "true" in output_response:
		print("Alert Bad words exists")
	elif "false" in output_response:
		print("No curse words found")
	else:
		print("Error in reading doc")
read_text()