# Creating App

from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.utils import get_color_from_hex
from kivy.core.text import LabelBase
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.widget import Widget

    

from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.card import MDCard

Window.size= (310,580)



class LoginScreen(Screen):
    pass


class SignupScreen(Screen):
    pass


class MainScreen(Screen):
    
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login screen'))
sm.add_widget(SignupScreen(name='signup-screen'))
sm.add_widget(MainScreen(name='mainscreen'))

class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    
    pass

class Separator(Widget):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('myapp.kv')


        


if __name__ == "__main__":
    MyApp().run()
