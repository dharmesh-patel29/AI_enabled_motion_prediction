
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.widget import Widget
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
import matplotlib.pyplot as plt
from kivymd_extensions.akivymd.uix.charts import AKPieChart
from kivy.metrics import dp







Window.size= (320,500)

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
    items = [{"Python": 40, "Java": 30, "C++": 10, "PHP": 8, "Ruby": 12}]

    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self):
        self.piechart = AKPieChart(
            items=self.items,
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            size_hint=[None, None],
            size=(dp(300), dp(300)),
        )
        self.ids.chart_box.add_widget(self.piechart)

    def update_chart(self):
        self.piechart.items = [{"Python": 70, "Dart": 10, "C#": 10, "Css": 10}]

    def remove_chart(self):
        self.ids.chart_box.remove_widget(self.piechart)


class MonthlyGraph(Screen):
    pass

class YearlyGraph(Screen):
    pass

class Setting(Screen):
    pass

class EditProfile(Screen):
    pass

class Notification(Screen):
    pass

class SystemPermission(Screen):
    pass

class UserData(Screen):
    pass

class ProfileScoller(ScrollView):
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
sm.add_widget(EditProfile(name='profile'))
sm.add_widget(SystemPermission(name='systempermission'))
sm.add_widget(UserData(name='userdata'))

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
