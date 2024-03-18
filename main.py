# Standard library imports
import sys

# Third-party imports
from plyer import filechooser
import plyer

# Kivy imports
import kivy
from kivy.app import App
from kivy.clock import Clock
from kivy.lang import Builder
from kivy.properties import BooleanProperty, ListProperty
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleview.layout import LayoutSelectionBehavior
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.widget import Widget

# Our other files
import convert

# Local imports
from temp_editor import Editor

# Kivy version requirement
kivy.require('1.0.7')


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

    def apply_selection(self, file_list, index, is_selected):
        # Respond to the selection of items in the view. 
        self.selected = is_selected
        #print(str(index) + '/' + str(is_selected))
        file_list.data[index]['selected'] = is_selected


class FileList(RecycleView):
    def __init__(self, **kwargs):
        super(FileList, self).__init__(**kwargs)
        self.data = []

        
class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        super(MainLayout, self).__init__(**kwargs)
        self.file_list = self.ids.file_list
        self.files_to_convert = []
        self.output_folder = ""

    def open_files(self):
        selected_files = filechooser.open_file(title="Pick a file..", filters=[("PNG", "*.png")], multiple=True)

        for file_path in selected_files:
            self.handle_file_open(file_path)
            Editor.write('input_path' + str(selected_files.index(file_path) + 1), str(file_path))

    def handle_file_open(self, file_path):
        print("opened with yubaba : " + file_path)
        parent, name, extension = convert.find_file_name(file_path)
        
        if self.output_folder == "" :
            self.output_folder = parent
            print(parent)

        file = {
            "path": file_path,
            "name": name,
            "parent": parent,
            "extension": extension
        }

        self.files_to_convert.append(file)
        self.file_list.data = [{'text': file['name'] + '.' + file['extension'], 'selected' : False} for file in self.files_to_convert]

    def open_folder(self):
        selected_folder = filechooser.open_file(title="Pick a folder...", dirselect=True, filters=[("PNG", "*.dqzd")])

    def remove_selected(self):
        self.files_to_convert = [self.files_to_convert[file_index] for file_index in range(len(self.file_list.data)) if not(self.file_list.data[file_index]['selected'])]
        self.file_list.data = [{'text': file['name'] + '.' + file['extension'], 'selected' : False} for file in self.files_to_convert]

        # Does not work : after all items are deselected, they are selected back again by an unkown function

        # children = self.file_list.children[0].children
        # for index in range(len(self.file_list.data)):
        #     print(index)
        #     if isinstance(children[index], FileLabel):
        #         print('!')
        #         children[index].apply_selection(self.file_list, index, False)
    

class YubabaApp(App):  # load the yubaba.kv file
    def build(self):
        self.file_paths_to_open = sys.argv[1:]
        Clock.schedule_once(self.handle_start_open, 0)
        return MainLayout()

    def handle_start_open(self, dt):
        for file_path in self.file_paths_to_open:
            self.root.handle_file_open(file_path)


if __name__ == '__main__':
    YubabaApp().run()
