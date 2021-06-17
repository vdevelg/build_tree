import os



def dir_content(path):
    """ Формирует куст формата ({dir_name: None, ...}, [file_name, ...])
    """
    dict_of_dirs = {}
    list_of_files = []
    for name in os.listdir(path):
        if os.path.isdir(os.path.join(path, name)):
            dict_of_dirs[name] = None
        if os.path.isfile(os.path.join(path, name)):
            list_of_files.append(name)
    shrub = (dict_of_dirs, list_of_files)
    return shrub


def build_tree(path, tree, depth):
    """ Строит дерево каталогов формата ({dir_name: ({...},[]), ...}, [file_name, ...]).
        Функция рекурсивная, каждый экземпляр выстраивает свой слой.
        path - путь до tree
        tree - построенная часть дерева
        depth - глубина построения дерева
    """
    if depth:
        depth -= 1
        for dir_name in tree[0]:
            new_path = os.path.join(path, dir_name)
            slice = dir_content(new_path)
            tree[0][dir_name] = build_tree(new_path, slice, depth)
        return tree
    else:
        return None


def get_tree(path, depth):
    shrub = dir_content(path)
    tree = build_tree(path, shrub, depth)
    return tree


def print_tree(tree, counter=0):
    """ Печатает дерево из формата ({dir_name: ({...},[]), ...}, [file_name, ...])
    """
    string = ''
    indent = 4 * ' ' * counter
    if tree is not None:
        for name_dir in tree[0]:
            string = ''.join([string, indent, name_dir, '\n'])
            # print(indent, name_dir, sep='')
            string = ''.join([string, print_tree(tree[0][name_dir], counter + 1)])
        for name_file in tree[1]:
            string = ''.join([string, indent, name_file, '\n'])
            # print(indent, name_file, sep='')
    return string


def main():
    cur_path = os.getcwd()
    depth = 3
    tree = get_tree(cur_path, depth)
    string = print_tree(tree)
    print(string)


if __name__ == '__main__':
    main()
