from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class MainScreen(Screen):
    pass


class FileScreen(Screen):

    def selectFile(self, selectedFile):
        print(selectedFile)
        self.manager.transition.direction = 'right'
        self.manager.current = 'MainScreen'


class WindowManager(ScreenManager):
    pass


class MyApp(App):

    def build(self):
        return Builder.load_file("styling.kv")


MyApp().run()
