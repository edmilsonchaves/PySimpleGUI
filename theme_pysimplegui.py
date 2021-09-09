
# Theme's PySimpleGUI

import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WIN_CLOSED, Listbox, Window

sg.theme('DarkGrey11')

layout =[
    [sg.Text("Theme's PySimpleGUI")],
    [sg.Text('Choose the theme to view:')],
    [sg.Listbox(values=sg.theme_list(), key='-LIST-', size=(20,12), enable_events=True)],
    [sg.Button('Exit', key='-EXIT-', size=(20,1))]
    ]

window = sg.Window('PySimpleGUI', layout, element_justification='c')

while True:
    eventos, valores = window.read()
    if eventos == '-EXIT-' or eventos == WIN_CLOSED:
        break
    sg.theme(valores['-LIST-'][0])
    sg.popup_get_text('This is {}'.format(valores['-LIST-'][0].title()))
window.close()
