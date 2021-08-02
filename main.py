import httpx
import PySimpleGUI as sg


def is_game_over():
    txt = window['txtCurr'].DisplayText
    for el in txt:
        if el == '_':
            return False
    return True


def find_letter(txt, txt_find):
    global text_current
    text_current_tmp = list(text_current)
    tmp = window['txtCurr'].DisplayText
    tmp = list(tmp)
    match = False

    for i in range(0, len(tmp)):
        if txt_find[i] == txt.lower():
            tmp[i] = txt
            text_current_tmp[i] = txt
            match = True

    tmp = "".join(tmp)
    window['txtCurr'].update(value=tmp)
    text_current = text_current_tmp
    window[txt].Update(visible=False)

    if not match:
        return False
    return True


def redraw_picture(fail_count):
    window['img'].update(filename=r'img/' + str(fail_count) + '.png')


if __name__ == '__main__':
    r = httpx.get('https://random-word-api.herokuapp.com/word?number=1&swear=0')
    offset = 2
    game_over = False
    fail_count = 0

    text_goal = r.text[offset:len(r.text) - offset:]
    text_current = '_' * len(text_goal)
    # todo implement retry and fix wrong display of guessing text.
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
             'V', 'W', 'X', 'Y', 'Z']

    layout = [[sg.T(text=text_current, key='txtCurr', size=(40, 10), pad=(600, 0))], [sg.T("")],
              [sg.Button('A', size=(4, 2)), sg.Button('B', size=(4, 2)), sg.Button('C', size=(4, 2)),
               sg.Button('D', size=(4, 2)), sg.Button('E', size=(4, 2)), sg.Button('F', size=(4, 2)),
               sg.Button('G', size=(4, 2)), sg.Button('H', size=(4, 2)), sg.Button('I', size=(4, 2)),
               sg.Button('J', size=(4, 2)), sg.Button('K', size=(4, 2)), sg.Button('L', size=(4, 2)),
               sg.Button('M', size=(4, 2)), sg.Button('N', size=(4, 2)), sg.Button('O', size=(4, 2)),
               sg.Button('P', size=(4, 2)), sg.Button('Q', size=(4, 2)), sg.Button('R', size=(4, 2)),
               sg.Button('S', size=(4, 2)), sg.Button('T', size=(4, 2)), sg.Button('U', size=(4, 2)),
               sg.Button('V', size=(4, 2)), sg.Button('W', size=(4, 2)), sg.Button('X', size=(4, 2)),
               sg.Button('Y', size=(4, 2)), sg.Button('Z', size=(4, 2)), ],
              [sg.Image(r'img/0.png', size=(550, 550), key='img')]]
    window = sg.Window('Hangman', layout, size=(1320, 800))

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in alphabet:
            match = find_letter(event, text_goal)
            if not match:
                fail_count = fail_count + 1
                try:
                    redraw_picture(fail_count)
                except:
                    sg.Popup('Game over, right answer was:' + text_goal, keep_on_top=True)

            game_over = is_game_over()

        if game_over:
            sg.Popup('You won!', keep_on_top=True)
