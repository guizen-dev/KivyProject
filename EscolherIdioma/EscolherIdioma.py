from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen

Window.size = (360, 600)


# CRIAÇÃO DO ARQUIVO KIVY


class EscolherIdioma(Screen):
    kv = Builder.load_file('EscolherIdioma/escolherIdioma.kv')

    def __init__(self, **kwargs):  # defining an init method
        super().__init__(**kwargs)  # giving the subclass the same parameter signature as the parent


# CLASSE PRINCIPAL DO APLICATIVO
#class EscolherIdioma(MDApp):
#    def build(self):
#        return MyScreen()


#EscolherIdioma().run()
