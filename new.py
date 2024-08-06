from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.lang import Builder

from math_logic import generate_new_math

Builder.load_string('''
<MathQuizLayout>:
    orientation: 'vertical'
    padding: 20
    spacing: 20
    canvas.before:
        Color:
            rgba: 0.95, 0.95, 0.95, 1
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: '150dp'

        Label:
            id: problem_label
            text: 'Press "Next" to start the quiz'
            color: 0.1, 0.1, 0.1, 1
            font_size: 24
            size_hint_y: None
            height: self.texture_size[1]

        TextInput:
            id: user_input
            hint_text: 'Enter your answer here'
            background_color: 1, 1, 1, 1
            foreground_color: 0.1, 0.1, 0.1, 1
            font_size: 24
            size_hint_y: None
            height: 40

    Label:
        id: result_label
        text: ''
        color: 0.1, 0.1, 0.1, 1
        font_size: 18
        size_hint_y: None
        height: self.texture_size[1]

    BoxLayout:
        orientation: 'horizontal'
        spacing: 20
        size_hint_y: None
        height: 40

        Button:
            text: 'Келесі'
            background_color: 0.7, 0.7, 1, 1
            color: 0.1, 0.1, 0.1, 1
            on_press: app.next_problem()

        Button:
            text: 'Жіберу'
            background_color: 0.7, 1, 0.7, 1
            color: 0.1, 0.1, 0.1, 1
            on_press: app.check_answer()

    Widget:
        size_hint_y: None
        height: '50dp'
''')

class MathQuizLayout(BoxLayout):
    pass

class MathQuizApp(App):
    def build(self):
        self.score = 0
        return MathQuizLayout()

    def next_problem(self):
        self.problem, self.problem_type, self.solution = generate_new_math()
        self.root.ids.problem_label.text = self.problem
        self.root.ids.result_label.text = ''
        self.root.ids.user_input.text = ''

    def check_answer(self):
        user_input = self.root.ids.user_input.text
        if user_input == str(self.solution):
            self.root.ids.result_label.text = 'Дұрыс'
            self.score += 1
        else:
            self.root.ids.result_label.text = 'қате'
        self.root.ids.problem_label.text += f'\nScore: {self.score}'

if __name__ == '__main__':
    MathQuizApp().run()
