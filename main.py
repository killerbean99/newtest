from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

from math_logic import generate_new_math

class MathQuizApp(App):
    def build(self):
        self.score = 0

        self.layout = BoxLayout(orientation='vertical')

        self.problem_label = Label(text='Press "Next" to start the quiz')
        self.layout.add_widget(self.problem_label)

        self.user_input = TextInput(hint_text='Enter your answer here')
        self.layout.add_widget(self.user_input)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        self.next_button = Button(text='Next', on_press=self.next_problem)
        self.layout.add_widget(self.next_button)

        self.submit_button = Button(text='Submit', on_press=self.check_answer)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def next_problem(self, instance):
        self.problem, self.problem_type, self.solution = generate_new_math()
        self.problem_label.text = self.problem
        self.result_label.text = ''
        self.user_input.text = ''

    def check_answer(self, instance):
        if self.user_input.text == str(self.solution):
            self.result_label.text = 'Дұрыс'
            self.score += 1
        else:
            self.result_label.text = 'Қәте'
        self.problem_label.text += f'\nScore: {self.score}'

if __name__ == '__main__':
    MathQuizApp().run()