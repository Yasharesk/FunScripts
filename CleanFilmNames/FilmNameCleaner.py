import PySimpleGUI as sg
import Cleaner

INITIAL_DIR = 'D:/Downloads/'
DONE = 'Done!'
NOT_SELECTED = 'Select a folder'

# sg.theme('DarkTeal')
layout = [  [sg.Text('Add any extra words you want removed:'), sg.InputText(size=(25,3), tooltip='Separate words with a comma, no special characters', key='-WORDS-')],
            [sg.FolderBrowse(key='-FOLDER-', initial_folder=INITIAL_DIR, target='-SELECTED_DIR-'), 
                sg.InputText(NOT_SELECTED, key='-SELECTED_DIR-', readonly=True, disabled_readonly_background_color='#64778D', disabled_readonly_text_color='#FFFFFF') ],
            [sg.Button('Ok', disabled=False, key='-OK-'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)

while True:
    event, values = window.read()
    print(f'Events: {event}, Values: {values}')
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if (values['-SELECTED_DIR-'] == NOT_SELECTED) or (values['-SELECTED_DIR-'] == DONE):
        window['-SELECTED_DIR-'].update(NOT_SELECTED)
    else:
        # Cleaner.clean_directory(values['FOLDER'])
        print('Trying to udpate selected folder')
        window['-SELECTED_DIR-'].update(DONE)
        
window.close()