#Ceci est un test pour le push
import kivy
kivy.require('1.0.7')
import sys

from kivy.app import App
from kivy.uix.widget import Widget

def handle_file_open(file_path):
    # Your code to handle the opened file
	print("opened with yubaba : " + file_path)

class FileLayout(Widget):
	pass

class FileLayoutTest(Widget):
	pass

class YubabaApp(App): #load the yubaba.kv file
	pass


if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_path = sys.argv[1]
		handle_file_open(file_path)
	else:
		YubabaApp().run()