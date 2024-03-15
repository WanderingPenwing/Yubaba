#Ceci est un test pour le push
import kivy
kivy.require('1.0.7')
import sys

from temp_editor import Editor
from plyer import filechooser

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def handle_file_open(file_path):
	# pour qu'on gere un seul fichier, en prenant comme argument son path (uniquement) donc a formater en amont
	print("opened with yubaba : " + file_path)


class MainLayout(BoxLayout):
	def open_files (self):
		selected_files = filechooser.open_file(title="Pick a PNG file..",filters=[("PNG", "*.png")], multiple=True)
		
	for file_path in selected_files : # but : executer handle_file_open pour chaque fichier selectionné
		handle_file_open(file_path)
	
	#Editor.write('input_path', str(path))

			
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
		