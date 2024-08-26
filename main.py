import random

path_ = 'cheat_sheet.txt'

with open(path_, 'r', encoding='utf-8') as file:
    content_list = file.readlines()
    random.shuffle(content_list)


def check_answer(answer, txt):
    flag = False
    while not flag:
        if answer == txt:
            flag = True

            return flag
        elif answer == 'stop':
            return 'stop'
        else:
            answer = input('''\nЭто не верно!
Попробуйте ещё раз или введите "stop" ''')


for content in content_list:
    content = content.replace('\n', '')
    if not content:
        continue
    else:
        line_list = content.split(':')
        print(f'Опиание: {line_list[1]}')
        answer = input('Введите имя метода ".metod()" или функции "fun()" ')
        temp = check_answer(answer, line_list[0])
        if temp == 'stop':
            break
        elif temp:
            print('Верно\n')
