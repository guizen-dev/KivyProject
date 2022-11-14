from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager

from PaginaPrincipal.PaginaPrincipal import PaginaPrincipal
from EscolherIdioma.EscolherIdioma import EscolherIdioma
from EscolherPais.EscolherPais import EscolherPais
from Quiz.Quiz import Quiz


class WindowManager(ScreenManager):
    pass

sm = WindowManager()

screens = [EscolherIdioma(name="EscolherIdioma"), PaginaPrincipal(name="PaginaPrincipal"), EscolherPais(name="EscolherPais"), Quiz(name="Quiz")]  # setting an array of lists


#def __init__(self, **kwargs):
#    super().__init__(**kwargs)


for screen in screens:  # going through all of the screens
    sm.add_widget(screen)  # adding the screen widget to each

sm.current = "EscolherIdioma"  # setting current window to EscolherIdioma


class MainApp(MDApp):
    def build(self):
        Window.size = (360, 600)
        return sm


if __name__ == '__main__':
    EscolherIdioma = EscolherIdioma()
    EscolherIdioma.run()
