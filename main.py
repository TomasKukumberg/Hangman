import httpx
import PySimpleGUI as sg
from goto import with_goto


def is_game_over():
    txt = window['txtCurr'].DisplayText
    for el in txt:
        if el == '_':
            return False
    return True

def find_letter(txt, txt_find):
    tmp = window['txtCurr'].DisplayText
    tmp = list(tmp)
    for i in range(0, len(window['txtCurr'].DisplayText)):
        if txt_find[i] == txt.lower():
            tmp[i] = txt
    tmp = "".join(tmp)
    window['txtCurr'].update(value=tmp)
    window[txt].Update(visible=False)

@with_goto
if __name__ == '__main__':
    label.start
    r = httpx.get('https://random-word-api.herokuapp.com/word?number=1&swear=0')
    offset = 2
    game_over = False

    txt_find = r.text[offset:len(r.text) - offset:]
    txt_cur = '_' * len(txt_find)

    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

    layout = [[sg.T(text=txt_cur, key='txtCurr', size=(40, 10), pad=(600, 0))], [sg.T("")], [sg.Button('A', size=(4, 2)), sg.Button('B', size=(4, 2)), sg.Button('C', size=(4, 2)),
                           sg.Button('D', size=(4, 2)), sg.Button('E', size=(4, 2)), sg.Button('F', size=(4, 2)),
                           sg.Button('G', size=(4, 2)), sg.Button('H', size=(4, 2)), sg.Button('I', size=(4, 2)),
                           sg.Button('J', size=(4, 2)), sg.Button('K', size=(4, 2)), sg.Button('L', size=(4, 2)),
                           sg.Button('M', size=(4, 2)), sg.Button('N', size=(4, 2)), sg.Button('O', size=(4, 2)),
                           sg.Button('P', size=(4, 2)), sg.Button('Q', size=(4, 2)), sg.Button('R', size=(4, 2)),
                           sg.Button('S', size=(4, 2)), sg.Button('T', size=(4, 2)), sg.Button('U', size=(4, 2)),
                           sg.Button('V', size=(4, 2)), sg.Button('W', size=(4, 2)), sg.Button('X', size=(4, 2)),
                           sg.Button('Y', size=(4, 2)), sg.Button('Z', size=(4, 2)), ]]
    window = sg.Window('Hangman', layout, size=(1320, 800))

    while True:
        event, values = window.read()
        if event in (None, 'Exit'):
            break
        elif event in alpha:
            find_letter(event, txt_find)

        game_over = is_game_over()

        if game_over:
            window.Close()
            layout = [[sg.T(text=txt_find.upper(), key='txtCurr', pad=(600, 0))], [sg.T("")],
                      [sg.Button('A', size=(4, 2)), sg.Button('B', size=(4, 2)), sg.Button('C', size=(4, 2)),
                       sg.Button('D', size=(4, 2)), sg.Button('E', size=(4, 2)), sg.Button('F', size=(4, 2)),
                       sg.Button('G', size=(4, 2)), sg.Button('H', size=(4, 2)), sg.Button('I', size=(4, 2)),
                       sg.Button('J', size=(4, 2)), sg.Button('K', size=(4, 2)), sg.Button('L', size=(4, 2)),
                       sg.Button('M', size=(4, 2)), sg.Button('N', size=(4, 2)), sg.Button('O', size=(4, 2)),
                       sg.Button('P', size=(4, 2)), sg.Button('Q', size=(4, 2)), sg.Button('R', size=(4, 2)),
                       sg.Button('S', size=(4, 2)), sg.Button('T', size=(4, 2)), sg.Button('U', size=(4, 2)),
                       sg.Button('V', size=(4, 2)), sg.Button('W', size=(4, 2)), sg.Button('X', size=(4, 2)),
                       sg.Button('Y', size=(4, 2)), sg.Button('Z', size=(4, 2)), ],
                      [sg.T(text="You have won!", pad=(600, 0))]]

            window = sg.Window('Hangman', layout, size=(1320, 800))
            event, values = window.read()
            #todo implement goto when button retry is pressed