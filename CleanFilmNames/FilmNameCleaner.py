import PySimpleGUI as sg
from Cleaner import DirCleaner

INITIAL_DIR = 'D:/Downloads/'
WORD_LIST_FILE = 'word_list.txt'

DONE = 'Done!'
NOT_SELECTED = 'Select a folder'


with open(WORD_LIST_FILE) as f:
    remove_list = f.readline()

# sg.theme('DarkTeal')
layout = [  [sg.Text('Add any extra words you want removed:'), sg.InputText(size=(25,3), tooltip='Separate words with a comma, spaces are ignored', key='-WORDS-')],
            [sg.FolderBrowse(key='-FOLDER-', size=6, initial_folder=INITIAL_DIR, target='-SELECTED_DIR-'), 
                sg.InputText(NOT_SELECTED, size=51 , key='-SELECTED_DIR-', readonly=True, disabled_readonly_background_color='#64778D', disabled_readonly_text_color='#FFFFFF') ],
            [sg.Button('Ok', size=6, disabled=False, key='-OK-'), sg.Button('Cancel', size=6)] ]

window = sg.Window('Clean Film Names', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break
    if (values['-SELECTED_DIR-'] == NOT_SELECTED) or (values['-SELECTED_DIR-'] == DONE):
        window['-SELECTED_DIR-'].update(NOT_SELECTED)
    else:
        dir_cleaner = DirCleaner(values['-FOLDER-'], remove_list)
        if values['-WORDS-'] != '':
            dir_cleaner.add_words(values['-WORDS-'])
        dir_cleaner.clean_directory()
        window['-SELECTED_DIR-'].update(DONE)
        
window.close()