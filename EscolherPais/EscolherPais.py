from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.screen import Screen

Window.size = (360, 600)

#Builder.load_file('EscolherPais/escolherPais.kv')


class MyScreen(Screen):
    kv = Builder.load_file('EscolherPais/escolherPais.kv')


class EscolherPais(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return MyScreen()


#EscolherPais().run()
