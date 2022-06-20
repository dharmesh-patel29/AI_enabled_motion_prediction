# Creating App
from cProfile import Profile
from calendar import c
from unicodedata import name
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.widget import Widget
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivymd.uix.behaviors import RoundedRectangularElevationBehavior
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.menu import MDDropdownMenu
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

import test # importing self made

from kivymd.uix.list import OneLineIconListItem

Window.size= (320,510)

class MDScreen(Screen):
    pass

class LoginScreen(Screen):
    pass

class SignupScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class ActivityGraphScreen(Screen):
    pass

class DailyGraph(Screen):
    pass

class MonthlyGraph(Screen):
    pass

class YearlyGraph(Screen):
    pass

class Setting(Screen):
    pass

class Profile(Screen):
    pass

class Notification(Screen):
    pass

class ProfileScoller(ScrollView):
    pass

class MDCard1(MDCard):
    pass


sm = ScreenManager()
sm.add_widget(LoginScreen(name='login screen'))
sm.add_widget(SignupScreen(name='signup-screen'))
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(ActivityGraphScreen(name="activitiygraphscreen"))
sm.add_widget(DailyGraph(name='dailygraph'))
sm.add_widget(MonthlyGraph(name='monthlygraph'))
sm.add_widget(YearlyGraph(name='yearlygraph'))
sm.add_widget(Setting(name='setting'))
sm.add_widget(Profile(name='profile'))

class ProfileCard(MDFloatLayout, FakeRectangularElevationBehavior):
    pass

class UserCard(MDCard):
    pass

class MovementAnalysisCard(ProfileCard):
    pass

class MotivationTaskCard(ProfileCard):
    pass
class ButtonCard(ProfileCard):
    pass

class SettingsCard(ProfileCard):
    pass

class Layout_(FloatLayout):
    pass


class MyApp(MDApp):
    

    def build(self):
        
        self.theme_cls.theme_style = "Light"
        return Builder.load_file('myapp.kv')




       
if __name__ == "__main__":
    MyApp().run()
