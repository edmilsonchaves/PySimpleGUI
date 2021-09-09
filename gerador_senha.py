# --------------------------------------------------------------------- #
# Name: "Gerador de senha"
# Version: "1.0.0"
# Description: "Gerar e salvar senhas"
# Author: edmilsonchaves
# Language: pt-br
# --------------------------------------------------------------------- #

import PySimpleGUI as sg
from random import choices
import os


class Gerador_Senha:
    def __init__(self):
        sg.theme('Black')
        layout = [
            [sg.Text('Site / Software  ', font='black'), sg.Input('', font='black', key='-IN-SITE-SOFTWARE-',
             size=(23,1), border_width=2)],
            [sg.Text('E-mail / Usuário', font='black'), sg.Input('', font='black', key='-USUARIO-', size=(23,1), border_width=2) ],
            [sg.Text('Quantida de caracteres na senha?    ', font='black'), sg.Combo(values=list(range(31)),
             key='-TOTAL_CHARS-', default_value=1, size=(3,1))],
            [sg.Output(size=(46,5), key='-LOG_EVENTOS-')],
            [sg.Button('Gerar senha', font='black', size= (10,1)), sg.Text('', size=(0,1)),
            sg.Button('Limpar',font='black', size= (10, 1)), sg.Text('', size=(0,1)), sg.Button('Sair', font='black', size= (10,1))]
        ]
        #janela
        self.window = sg.Window('GERADOR DE SENHA', layout=layout)

    def Iniciar(self):
        while True:
            evento, valores = self.window.read()
            if evento == 'Sair' or evento == sg.WINDOW_CLOSED:
                break
            if evento == 'Limpar':
                self.window.find_element('-LOG_EVENTOS-').update('')
                self.window.find_element('-USUARIO-').update('')
                self.window.find_element('-TOTAL_CHARS-').update(1)
                self.window.find_element('-IN-SITE-SOFTWARE-').update('')
               
            if evento == 'Gerar senha':
                nova_senha = self.gerar_senha(valores)
                print(nova_senha)
                self.salvar_senha(nova_senha, valores)


    def gerar_senha(self, valores):
        char_list = 'ABCDEFGHIJKLMONPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%¨&*'
        chars = choices(char_list, k=int(valores['-TOTAL_CHARS-']))
        new_pass = ''.join(chars)
        return new_pass
    
    def salvar_senha(self, nova_senha, valores):
        with open('senhas.txt', 'a', newline='') as arquivo:
            arquivo.write(f"site: {valores['-IN-SITE-SOFTWARE-']}, usuário: {valores['-USUARIO-']}, nova senha: {nova_senha}\n")

        print('Arquivo salvo')

gs = Gerador_Senha()
gs.Iniciar()





