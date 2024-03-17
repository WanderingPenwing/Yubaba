# Ceci est un test pour le push
import kivy
kivy.require('1.0.7')
import sys
import os  # si ca pete votre config enlevez cette ligne et la suivante x)
os.environ["PLYER_PLATFORM"] = "gtk"
import plyer

from temp_editor import Editor
from plyer import filechooser

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.label import Label
from kivy.properties import BooleanProperty
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.properties import ListProperty

import convert

class SelectableRecycleBoxLayout(FocusBehavior, LayoutSelectionBehavior, RecycleBoxLayout):
    # Adds selection and focus behavior to the view. 
    pass


class FileLabel(RecycleDataViewBehavior, Label):
    # Add selection support to the Label
    index = None
    selected = BooleanProperty(False)
    selectable = BooleanProperty(True)

    def refresh_view_attrs(self, rv, index, data):
        # Catch and handle the view changes 
        self.index = index
        return super(FileLabel, self).refresh_view_attrs(
            rv, index, data)

    def on_touch_down(self, touch):
        # Add selection on touch down 
        if super(FileLabel, self).on_touch_down(touch):
            return True
        if self.collide_point(*touch.pos) and self.selectable:
            return self.parent.select_with_touch(self.index, touch)

    def apply_selection(self, rv, index, is_selected):
        # Respond to the selection of items in the view. 
        self.selected = is_selected


class FileList(RecycleView):
    def __init__(self, **kwargs):
        super(FileList, self).__init__(**kwargs)
        self.data = [{'text': 'File ' + str(x)} for x in range(5)]

        
class MainLayout(BoxLayout):
    def open_files(self):
        selected_files = filechooser.open_file(title="Pick a PNG file..", filters=[("PNG", "*.png")], multiple=True)

        for file_path in selected_files:  # but : executer handle_file_open pour chaque fichier selectionné
            App.get_running_app().handle_file_open(file_path)
            Editor.write('input_path' + str(selected_files.index(file_path) + 1), str(file_path))


class YubabaApp(App):  # load the yubaba.kv file
    files_to_convert = ListProperty([])

    def handle_file_open(self, file_path):
        # pour qu'on gere un seul fichier, en prenant comme argument son path (uniquement) donc a formater en amont
        print("opened with yubaba : " + file_path)

        parent, name, extension = convert.find_file_name(file_path)

        file = {
            "path": file_path,
            "name": name,
            "parent": parent,
            "extension": extension
        }
        self.files_to_convert.append(file)
        print("---------------")
        print(self.files_to_convert)

    def build(self):
        return MainLayout()


if __name__ == '__main__':
    app = YubabaApp()
    app.handle_file_open("images/test.webp")
    if len(sys.argv) > 1:
        for file_path in sys.argv[1:]:
            app.handle_file_open(file_path)
    app.run()
