from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

selecting_file = None

class MainScreen(Screen):
    
    def choose_file(self, choosing):
        global selecting_file
        selecting_file = choosing


class FileScreen(Screen):

    def selectFile(self, selectedFile):
        global selecting_file
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'
        if selecting_file == 'input':
            self.manager.get_screen('MainScreen').ids['input_file_text_input'].text = str(selectedFile[0])
        elif selecting_file == 'output':
            self.manager.get_screen('MainScreen').ids['output_file_text_input'].text = str(selectedFile[0])
        elif selecting_file == 'runner':
            self.manager.get_screen('MainScreen').ids['runner_file_text_input'].text = str(selectedFile[0])


class WindowManager(ScreenManager):
    pass


class MyApp(App):

    def build(self):
        return Builder.load_file("styling.kv")


MyApp().run()
