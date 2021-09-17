
# Program developed on the linux mint system

import PySimpleGUI as sg
from os import system

from PySimpleGUI.PySimpleGUI import WIN_CLOSED

sg.theme('Reddit')

layout = [
    [sg.Button('Shutdown', key='-Shutdown-', size=(15,1))],
    [sg.Button('Restart', key='-Restart-', size=(15,1))],
    [sg.Button('Exit', key='-Exit-', size=(15,1))]
]

window = sg.Window('Linux Mint', layout, element_justification='center')

while True:
    event,values = window.read()

    if event == '-Exit-' or event == WIN_CLOSED:
        break
    
    elif event == '-Shutdown-':
        system('halt -p')
    
    elif event == '-Restart-':
        system('halt --reboot')

window.close()

