from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window

class Main(App):
    def build(self):
        return Gerenciador()

class Gerenciador (ScreenManager):
    pass

class Menu(Screen):
    pass

class Tarefas(Screen):

    def __init__(self, tarefas = [], **kwargs):
        super().__init__(**kwargs)
        for tarefa in tarefas:
            self.ids.box.add_widget(Excluir(text = tarefa))

    def on_pre_enter(self, *args):
        Window.bind(on_keyboard = self.voltar)

    def on_pre_leave(self, *args):
        Window.unbind(on_keyboard = self.voltar)

    def voltar(self, window, key, *args):
        if key == 27:
            App.get_running_app().root.current = 'menu'
            return True

    def addWidget(self):
        texto = self.ids.texto.text
        self.ids.box.add_widget(Excluir(text = texto))
        self.ids.texto.text = ''

class Excluir(BoxLayout):
    def __init__(self, text = '', **kwargs):
        super().__init__(**kwargs)
        self.ids.label.text = text

Main().run()