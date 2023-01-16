'''Задание 3'''
from flask import Flask, render_template, request

app = Flask(__name__)
card_number = None

@app.route('/', methods = ['GET', 'POST'])
def main_page():
    '''Главная страница'''
    global card_number
    if request.method == 'POST':
        card_number = request.form.get('card_number')
        if card_number != '':
            if len(card_number) == 16 and card_number.isdigit():
                for i in range(len(card_number)):
                    if i <= 11:
                        card_number = card_number.replace(card_number[i], '#', 1)
            else:
                card_number = 'Данные карты некорректны'
    return render_template('main_page.html', card_number = card_number)

if __name__ == '__main__':
    app.run()
