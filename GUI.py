import PySimpleGUI as pg
import build_tree as bt


pg.theme('System Default 1') # Default 1, System Default 1, DarkTanBlue ...

def GUI():
    layout = [  
                [pg.InputText('C:/dev/build_tree/PROVING GROUND',key='path_to_folder',size=(80,1)), 
                 pg.FolderBrowse('Open folder',size=(len('Open folder') + 2,1)), 
                 pg.Spin([i for i in range(255)],key='depth',initial_value=1,size=(5,2)), 
                 pg.Button('Build',key='build_tree',size=(len('Build') + 3,1))],

                [pg.Multiline(key='paper',size=(115,25))]
             ]

    window = pg.Window('Build tree', layout)

    counter = 1

    while True:
        event, values = window.read()
        if event == pg.WIN_CLOSED:
            break
        if event == 'build_tree':
            cur_path = values['path_to_folder']
            depth = values['depth']
            tree = bt.get_tree(cur_path, depth)
            print(tree)
            Mtext = bt.print_tree(tree)
            
            Mtext = ''.join(['Result ', str(counter), '\n--------------------------------------\n', Mtext, '--------------------------------------\n'])
            counter += 1
            window['paper'].print(Mtext)

    window.close()


if __name__ == '__main__':
    GUI()
