from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen

Window.size = (360, 600)


class PaginaPrincipal(Screen):
    kv = Builder.load_file('PaginaPrincipal/paginaPrincipal.kv')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


#class PaginaPrincipal(MDApp):
#    def build(self):
#        self.theme_cls.primary_palette = "Indigo"
#        return MyScreen()


#PaginaPrincipal().run()
