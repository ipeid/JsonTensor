from treelib import Tree, Node

class Nodex(object):
    def __init__(self, num):
        self.num = num

tree = Tree()
tree.create_node('Root', 'root', data = Nodex({"k1":"v1"}))
tree.create_node('Child1', 'child1', parent = 'root', data =Nodex({"k2":"v2"}))
tree.create_node('Child2', 'child2', parent = 'child1')
tree.nodes['child2'].data = Nodex({"k3":"v3"})

tree.show()
tree.show(data_property='num')