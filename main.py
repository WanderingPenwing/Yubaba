#Ceci est un test pour le push
import kivy
kivy.require('1.0.7')
import sys

import tkinter
from tkinter import filedialog

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def handle_file_open(file_path):
    # Your code to handle the opened file
	print("opened with yubaba : " + file_path)

class MainLayout(BoxLayout):
	def open_files (self):
		tkinter.Tk().withdraw() # prevents an empty tkinter window from appearing
		folder_path = filedialog.askdirectory()

			
class YubabaApp(App): #load the yubaba.kv file
	def build(self):
		return MainLayout()
	pass
    


if __name__ == '__main__':
	if len(sys.argv) > 1:
		file_path = sys.argv[1]
		handle_file_open(file_path)
	else:
		YubabaApp().run()
		