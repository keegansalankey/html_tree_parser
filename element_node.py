def is_empty(element_type):
    if element_type == 'br':
        return True
    if element_type == 'img':
        return True
    if element_type == 'area':
        return True
    if element_type == 'base':
        return True
    if element_type == 'col':
        return True
    if element_type == 'embed':
        return True
    if element_type == 'hr':
        return True
    if element_type == 'input':
        return True
    if element_type == 'link':
        return True
    if element_type == 'meta':
        return True
    if element_type == 'param':
        return True
    if element_type == 'source':
        return True
    if element_type == 'track':
        return True
    if element_type == 'wbr':
        return True
    else:
        return False

class ElementNode:



    def __init__(self, element_type, parent, level, content='', element_class=''):
        self.element_type = element_type
        self.children = []
        self.parent = parent
        self.level = level
        self.content = content
        self.element_class = element_class
        self.empty_flag = is_empty(element_type)

    def add_child(self, child):
        self.children.append(child)

    def print_tree(self):
        level_string = ''
        for i in range(0, self.level):
            level_string += '-'

        print(level_string + self.element_type)
        for child in self.children:
            child.print_tree()
