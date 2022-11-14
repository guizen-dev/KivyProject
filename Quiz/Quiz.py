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


class MyScreen(Screen):
    import QuizData
    import random

    NumeroAleatorio = random.randint(1, 50)

    DicasRestantes = 5
    RespostasCorretas = 0
    BarraTopo = 1
    NovaPergunta = True
    dialog = None
    Pergunta = QuizData.PerguntaBRPT[NumeroAleatorio]
    Resposta = QuizData.RespotaBRPT[NumeroAleatorio]
    print(Resposta)

    # Card de pular questão
    def PularQuestao(self):
        self.dialog = MDDialog(
            title="Pular pergunta?",
            buttons=[
                MDFlatButton(
                    text="Sim",
                    on_release=MyScreen.PerguntaAleatoria
                ),
                MDFlatButton(
                    text="Não",
                    on_release=self.fechar_dialog
                ),
            ],
            radius=[20, 7, 20, 7]
        )
        self.dialog.open()

    # Gerar Pergunta Aleatória e instanciar nos texts
    def PerguntaAleatoria(self):
        MyScreen.NumeroAleatorio = MyScreen.random.randint(1, 50)
        MyScreen.Resposta = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        MyScreen.Pergunta = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        self.ids.pergunta_principal.text = MyScreen.Pergunta
        self.ids.resposta_a.text = MyScreen.Resposta[0]
        self.ids.resposta_b.text = MyScreen.Resposta[1]
        self.ids.resposta_c.text = MyScreen.Resposta[2]
        self.ids.resposta_d.text = MyScreen.Resposta[3]

    # Gerar Pergunta Aleatória ao pular a questão

    def Pulou(self, inst):
        MyScreen.NumeroAleatorio = MyScreen.random.randint(1, 50)
        MyScreen.Resposta = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        MyScreen.Pergunta = MyScreen.QuizData.PerguntaBRPT[MyScreen.NumeroAleatorio]
        self.ids.pergunta_principal.text = MyScreen.Pergunta
        self.ids.resposta_a.text = MyScreen.Resposta[0]
        self.ids.resposta_b.text = MyScreen.Resposta[1]
        self.ids.resposta_c.text = MyScreen.Resposta[2]
        self.ids.resposta_d.text = MyScreen.Resposta[3]
        self.dialog.dismiss()

    # Card de dicas
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

    # Fechar cards
    def fechar_dialog(self, inst):
        self.dialog.dismiss()

    # Análise de Respostas
    def resposta(self, botao):

        if botao.text == MyScreen.QuizData.RespotaBRPT[MyScreen.NumeroAleatorio][4]:
            botao.line_color = (46 / 255.0, 212 / 255.0, 0, 1)
            botao.icon = "checkbox-marked-circle"
            botao.icon_color = (46 / 255.0, 212 / 255.0, 0, 1)
            botao.text_color = (46 / 255.0, 212 / 255.0, 0, 1)
            self.ids.BotaoInferior.text = "Próxima"
            self.ids.BotaoInferior.on_release = self.PerguntaAleatoria
            MyScreen.RespostasCorretas = MyScreen.RespostasCorretas + 1

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
