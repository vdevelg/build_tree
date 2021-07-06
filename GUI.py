import os

import PySimpleGUI as pg
import build_tree as bt



pg.theme('System Default 1') # Default 1, System Default 1, DarkTanBlue ...
dictionary = {'openFolder':         {'ENG':'open folder',           'RUS':'открыть папку'},
              'depth':              {'ENG':'folder nesting depth',  'RUS':'олубина вложенности папок'},

              'build':              {'ENG':'build',                 'RUS':'построить'},
              'copy':               {'ENG':'copy last result',      'RUS':'копировать последний результат'},
              'clear':              {'ENG':'clear output field',    'RUS':'очистить поле вывода'},
              'toLANG':             {'ENG':'на Русский',    'RUS':'to English'}
             }
start_language = 'ENG'
LANG = start_language


def GUI():
    global LANG
    default_path = os.getcwd()
    layout = [
                [pg.InputText(default_path,key='path_to_folder',size=(100,1)),
                 pg.FolderBrowse(dictionary['openFolder'][LANG].title(),size=(len(dictionary['openFolder'][LANG]) + 3,1))],

                [pg.Text(dictionary['depth'][LANG].capitalize()+':'), pg.Spin([i for i in range(255)],key='depth',initial_value=1,size=(5,2))],

                [pg.Multiline(key='paper',size=(115,25))],

                [pg.Button(dictionary['build'][LANG].title(),key='build',size=(len(dictionary['build'][LANG]) + 3,1)),
                 pg.Button(dictionary['copy'][LANG].title(),key='copy_last',size=(len(dictionary['copy'][LANG]) + 3,1)),
                 pg.Button(dictionary['clear'][LANG].title(),key='clear',size=(len(dictionary['clear'][LANG]) + 3,1)),
                 pg.Button(dictionary['toLANG'][LANG].title(),key='toLANG',size=(len(dictionary['copy'][LANG]) + 3,1)),]
             ]

    window = pg.Window('Build tree', layout, icon='tree.ico') # source: https://ru.seaicons.com/71661/

    counter_of_results = 1

    while True:
        event, values = window.read()
        if event == pg.WIN_CLOSED:
            break
        if event == 'build':
            cur_path = values['path_to_folder']
            depth = values['depth']
            tree = bt.get_tree(cur_path, depth)
            Mtext = bt.tree_dumps(tree)

            long_sep =  '----------------------------------------------------------------------------------------------------\n'
            short_sep = '--------------------------------------------------\n'
            Mtext_sepd = ''.join(['Result ', str(counter_of_results), '\n',
                            long_sep,
                            Mtext,
                            short_sep])
            counter_of_results += 1

            window['paper'].print(Mtext_sepd)
        if event == 'copy':
            pass
        if event == 'clear':
            pass
        if event == 'toLANG':
            if LANG == 'ENG':
                LANG = 'RUS'
            elif LANG == 'RUS':
                LANG = 'ENG'
            print(LANG)
            for key in window:
                window[key].update()

    window.close()



if __name__ == '__main__':
    GUI()
