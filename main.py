from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from random import randint

def generate_new_math():
    num1 = randint(0, 4)
    num2 = randint(0, 10)
    problem = 'Есепті шығар:\n'
    problem += str(int(num1)) + '*' + str(int(num2)) + '='
    solution = int(num1 * num2)

    return problem, solution


class MathQuizApp(App):
    def build(self):
        self.score = 0

        self.layout = BoxLayout(orientation='vertical')

        self.problem_label = Label(text='Жалғастыру үшін "Келесі" батырмасын басыңыз.')
        self.layout.add_widget(self.problem_label)

        self.user_input = TextInput(hint_text='Жауабын осында жазыңыз:')
        self.layout.add_widget(self.user_input)

        self.result_label = Label(text='')
        self.layout.add_widget(self.result_label)

        self.next_button = Button(text='Келесі', on_press=self.next_problem)
        self.layout.add_widget(self.next_button)

        self.submit_button = Button(text='Жіберу', on_press=self.check_answer)
        self.layout.add_widget(self.submit_button)

        return self.layout

    def next_problem(self, instance):
        self.problem, self.solution = generate_new_math()
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
