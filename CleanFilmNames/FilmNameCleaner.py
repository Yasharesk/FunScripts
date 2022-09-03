import PySimpleGUI as sg
import Cleaner

INITIAL_DIR = 'D:/Downloads/'
DONE = 'Done!'

# sg.theme('DarkTeal')   # Add a touch of color
layout = [  [sg.Text('Add any extra words you want removed:'), sg.InputText(size=(25,3), tooltip='Separate words with a comma, no special characters', key='-WORDS-')],
            [sg.FolderBrowse('Select a folder', key='-FOLDER-', initial_folder=INITIAL_DIR), sg.Text('', key='selected_dir') ],
            [sg.Button('Ok', disabled=False, key='ok_btn'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if event == '-FOLDER-':
        window['selected_dir'].update(values['-FOLDER-'])
    if len(values['-FOLDER-']) != 0:
        # Cleaner.clean_directory(values['FOLDER'])
        window['selected_dir'].update(DONE)
        window['-FOLDER-'].update('')
    else:
        window['selected_dir'].update('First select a folder!')

window.close()