import webbrowser
import time

breaks = 0;

print("This  program is started on : "+time.ctime())
while (breaks < 3):
	time.sleep(5)
	webbrowser.open("https://www.youtube.com/watch?v=w5iOGZ1-oZs")
	breaks = breaks + 1