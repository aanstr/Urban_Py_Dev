import tkinter as tk
import sympy as sp
from decimal import Decimal, getcontext

# Устанавливаем контекст для работы с точностью до 50 знаков после запятой
getcontext().prec = 50


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("500x600")
        self.current_expression = ""
        self.result_var = tk.StringVar()

        # Создаем виджеты
        self.create_widgets()

    def create_widgets(self):
        # Экран для вывода
        result_display = tk.Entry(self.root, textvariable=self.result_var, font=("Arial", 24), bd=10, relief="ridge",
                                  justify="right")
        result_display.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Кнопки калькулятора
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('%', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('=', 5, 1), ('^', 5, 2), ('1/x', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
            ('sqrt', 7, 0), ('pi', 7, 1), ('e', 7, 2), ('(', 7, 3),
            (')', 8, 0), ('exp', 8, 1), ('ln', 8, 2), ('x!', 8, 3)
        ]

        # Добавляем кнопки на экран
        for (text, row, col) in buttons:
            self.create_button(text, row, col)

        # Связываем клавиши с кнопками
        self.root.bind("<Key>", self.handle_keypress)

    def create_button(self, text, row, col):
        button = tk.Button(self.root, text=text, font=("Arial", 18), bd=5, height=2, width=5,
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == 'C':
            self.current_expression = ""
        elif char == '=':
            try:
                # Оценка выражения с использованием sympy для сложных выражений
                expression = self.current_expression.replace("^", "**").replace("ln", "log")
                # Преобразуем выражение в символьное выражение
                result = sp.sympify(expression)
                result = Decimal(result.evalf())
                self.current_expression = str(result)
            except Exception as e:
                self.current_expression = "Error"
        elif char == '1/x':
            try:
                num = float(self.current_expression)
                if num != 0:
                    self.current_expression = str(Decimal(1) / Decimal(num))
                else:
                    self.current_expression = "Error"
            except ValueError:
                self.current_expression = "Error"
        elif char == '^':
            self.current_expression += '**'
        elif char == '%':
            try:
                percent_value = float(self.current_expression) / 100
                self.current_expression = str(percent_value)
            except ValueError:
                self.current_expression = "Error"
        elif char == 'sqrt':
            try:
                result = Decimal(self.current_expression) ** 0.5
                self.current_expression = str(result)
            except ValueError:
                self.current_expression = "Error"
        elif char == 'pi':
            self.current_expression += str(sp.pi)
        elif char == 'e':
            self.current_expression += str(sp.E)
        elif char == 'x!':
            try:
                num = int(self.current_expression)
                self.current_expression = str(sp.factorial(num))
            except ValueError:
                self.current_expression = "Error"
        elif char in ['sin', 'cos', 'tan', 'log', 'exp', 'ln']:
                self.current_expression += char + "("
        elif char == '(' or char == ')':
                self.current_expression += char
        else:
                self.current_expression += char

        self.result_var.set(self.current_expression)

    def handle_keypress(self, event):
        # Обработка ввода с клавиатуры
        key = event.char
        if key in '0123456789+-*/.^%()sin costanlogsqrtx!':
            self.on_button_click(key)
        elif key == '\r':  # Enter key
            self.on_button_click('=')
        elif key == '\x08':  # Backspace key
            self.current_expression = self.current_expression[:-1]
            self.result_var.set(self.current_expression)

def main():
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()

if __name__ == "__main__":
        main()
