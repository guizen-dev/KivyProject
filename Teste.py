from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.uix.button import MDFlatButton
from kivymd.uix.label import MDLabel
from kivymd.uix.screen import Screen
from kivymd.uix.dialog import MDDialog


Window.size = (360, 600)


# Builder.load_file('Quiz/quiz.kv')


class MyScreen(Screen):
    import QuizData
    import random

    DicasRestantes = 5
    RespostasCorretas = 0
    BarraTopo = 1
    NovaPergunta = True

    while NovaPergunta == True:
        NumeroAleatorio = random.randint(1, 50)
        pergunta = QuizData.PerguntaBRPT[NumeroAleatorio]
        resposta = QuizData.RespotaBRPT[NumeroAleatorio]
        NovaPergunta = False

    dialog = None

    #def on_enter(self, *args):
    #    MyScreen.NumeroAleatorio = MyScreen.random.randint(1, 50)
    #    pergunta = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
    #    self.ids.pergunta_principal.text = pergunta

    # Card de pular questão
    def PularQuestao(self):
        self.dialog = MDDialog(
            title="Proxíma Questão?",
            buttons=[
                MDFlatButton(
                    text="Sim",
                    on_release=self.Pulou
                ),
                MDFlatButton(
                    text="Não",
                    on_release=self.fechar_dialog
                ),
            ],
            radius=[20, 7, 20, 7]
        )
        self.dialog.open()

    def PerguntaAleatoria(self):
        MyScreen.NumeroAleatorio = MyScreen.random.randint(1, 50)
        # self.ids.pergunta_principal.text = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        # self.ids.resposta_a.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][1]
        # self.ids.resposta_a.icon = "alpha-d-circle"
        ##self.ids.resposta_a.primary_palette = "Indigo"
        # self.ids.resposta_b.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][2]
        # self.ids.resposta_b.icon = "alpha-d-circle"
        ##self.ids.resposta_b.primary_palette = "Indigo"
        # self.ids.resposta_c.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][3]
        # self.ids.resposta_c.icon = "alpha-d-circle"
        ##self.ids.resposta_c.primary_palette = "Indigo"
        # self.ids.resposta_d.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]
        # self.ids.resposta_d.icon = "alpha-d-circle"
        pergunta = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        self.ids.pergunta_principal.text = pergunta

        # self.ids.resposta_d.primary_palette = "Indigo"

    def Pulou(self, inst):
        MyScreen.NumeroAleatorio = MyScreen.random.randint(1, 50)
        self.ids.pergunta_principal.text = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        self.ids.resposta_a.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][1]
        self.ids.resposta_a.icon = "alpha-a-circle"
        # self.ids.resposta_d.line_color = Quiz.theme_cls.primary_color
        self.ids.resposta_b.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][2]
        self.ids.resposta_b.icon = "alpha-b-circle"
        # self.ids.resposta_d.line_color = Quiz.theme_cls.primary_color
        self.ids.resposta_c.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][3]
        self.ids.resposta_c.icon = "alpha-c-circle"
        # self.ids.resposta_d.line_color = Quiz.theme_cls.primary_color
        self.ids.resposta_d.text = MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]
        # self.ids.app.theme_cls.primary_light = app.theme_cls.primary_color
        self.ids.resposta_d.line_color = Quiz.theme_cls.primary_color
        self.dialog.dismiss()

    def abrir_dica(self):
        MyScreen.DicasRestantes = MyScreen.DicasRestantes - 1
        if MyScreen.DicasRestantes != 0:
            self.dialog = MDDialog(
                title="Dicas disponíveis: " + str(MyScreen.DicasRestantes),
                text=MyScreen.QuizData.DicaBR[MyScreen.NumeroAleatorio],
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.fechar_dialog
                    ),
                ],
                radius=[20, 7, 20, 7]
            )
            self.dialog.open()
        if MyScreen.DicasRestantes == 0:
            self.dialog = MDDialog(
                title="Dicas disponíveis: " + str(MyScreen.DicasRestantes),
                text="Você não possui mais dicas",
                buttons=[
                    MDFlatButton(
                        text="OK",
                        on_release=self.fechar_dialog
                    ),
                ],
                radius=[20, 7, 20, 7]
            )
            self.dialog.open()

    def fechar_dialog(self, inst):
        self.dialog.dismiss()

    def resposta(self, numero, botao):
        # if MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][numero] == \
        #        MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]:

        if botao.text == MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]:
            botao.line_color = (46 / 255.0, 212 / 255.0, 0, 1)
            botao.icon = "checkbox-marked-circle"
            botao.icon_color = (46 / 255.0, 212 / 255.0, 0, 1)
            botao.text_color = (46 / 255.0, 212 / 255.0, 0, 1)
            self.ids.BotaoInferior.text = "Próxima"

            MyScreen.RespostasCorretas = MyScreen.RespostasCorretas + 1
        # if MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][numero] != \
        #        MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]:

        if botao.text != MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]:
            botao.line_color = (237 / 255.0, 2 / 255.0, 2 / 255.0, 1)
            botao.icon = "alpha-x-circle"
            botao.icon_color = (237 / 255.0, 2 / 255.0, 2 / 255.0, 1)
            botao.text_color = (237 / 255.0, 2 / 255.0, 2 / 255.0, 1)
            self.ids.BotaoInferior.text = "Próxima"


class Quiz(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        return MyScreen()


Quiz().run()
