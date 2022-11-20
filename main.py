import re
from element_node import ElementNode as e_node

def get_body(file):

    body_flag = False
    parent_node = None
    element_list = []

    with open(file) as f:
        for line in f.readlines():
            if re.search('.*?(?=<body.*?>).*?', line):
                body_flag = not body_flag

            if body_flag == True:
                for node in find_nodes(line):
                    element_list.append(re.sub('<', '', node.rstrip(node[-1])).split()[0])

            if re.search('.*?(?=</body.*?>).*?', line):
                body_flag = not body_flag

        print (element_list)
        tree = make_graph(element_list)
        tree.print_tree()

    f.close()


def find_nodes(line):

    node_strings = re.findall('<[^\!].*?>.*?' , line.strip(' '))
    return node_strings

def closing_flag(element):
    return re.search('/.*?', element)


def make_graph(elements, parent = None, level = 0):

    if not elements:
        return parent

    if not closing_flag(elements[0]):
        print('element: ' + elements[0])
        node = e_node(elements[0], parent, level)
        if parent != None:
            parent.add_child(node)
            print('parent: '  +  parent.element_type)
        if node.empty_flag:
            return make_graph(elements[1:], parent, level)
        return make_graph(elements[1:], node, level + 1)
    else:
        if parent.parent != None:
            return make_graph(elements[1:], parent.parent, level - 1)
        return parent



if __name__ == '__main__':
    get_body('test1.html')
