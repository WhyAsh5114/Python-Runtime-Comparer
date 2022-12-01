from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager

selecting_file = None

class MainScreen(Screen):
    
    def choose_file(self, choosing):
        global selecting_file
        selecting_file = choosing
    
    def update_start_button_text(self):
        if self.ids['input_file_text_input'].text != '' and self.ids['runner_file_text_input'].text != '':
            self.ids['start_button'].text = 'Start plot'
        else:
            self.ids['start_button'].text = 'Select all 2 files to continue'


class FileScreen(Screen):

    def selectFile(self, selectedFile):
        global selecting_file
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'

        selectedFile = len(selectedFile) != 0 and selectedFile[0] or ''
        main_screen = self.manager.get_screen('MainScreen')
        if selecting_file == 'input':
            main_screen.ids['input_file_text_input'].text = selectedFile
        elif selecting_file == 'runner':
            main_screen.ids['runner_file_text_input'].text = selectedFile
        
        main_screen.update_start_button_text()


class WindowManager(ScreenManager):
    pass


class MyApp(App):

    def build(self):
        return Builder.load_file("styling.kv")


MyApp().run()
