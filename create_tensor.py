import pandas as pd
from treelib import Tree, Node

import node

class Nodex(object):
    def __init__(self, dataframe):
        self.dataframe = dataframe

def create_json_tree(data:dict):
    tree = Tree()

    # create root node
    tree.create_node('Root', 'root')
    root_df = start_node(tree,data)
    # give the root node value by first node dataframe
    tree.nodes['root'].data = Nodex(root_df)
    return tree

def create_node_digui(tree, tag, init_iden,identifier, parent):
    try:
        tree.create_node(tag, identifier, parent)
    # except Tree.exceptions.DuplicatedNodeIdError:
    except Exception:
        if '_' in identifier and identifier != init_iden:
            try:
                nnum=int(identifier.split('_')[-1])
            except:
                identifier = identifier+"_1"
            else:
                identifier = '_'.join(identifier.split('_')[:-1])+'_'+str(nnum+1)
        else:
            identifier = identifier+'_1'
        return create_node_digui(tree, tag, init_iden, identifier, parent)
    else:
        return identifier

def start_node(tree:Tree,data: dict):

    root_keys = data.keys()
    root_data = []
    i = 0
    for each_root_key in root_keys:
        i += 1
        root_value = data[each_root_key]
        # create child node
        identifier = create_node_digui(tree, each_root_key, each_root_key,each_root_key, parent='root')

        if type(root_value) == list:
            node_class = node.Node(child=each_root_key, identifier='root', child_type='list', deep=0)
            print(node_class)

            root_data.append(node_class)
            # root_data.append('child1-' + str(i) + '_list')

            # tree.create_node(each_root_key, each_root_key, parent='root')
            node_df = list_node_digui(tree,identifier, root_value)
            # give the node value by next node dataframe
            tree.nodes[identifier].data = Nodex(node_df)

        elif type(root_value) == dict:
            node_class = node.Node(child=each_root_key, identifier='root', child_type='dict', deep=0)
            root_data.append(node_class)
        #             node_digui_dict(root_value)
        else:
            root_data.append[root_value]
            tree.nodes[identifier].data = Nodex(root_value)

    root_df = pd.DataFrame([root_data], columns=root_keys)

    return root_df


def list_node_digui(tree:Tree,father_key: str, child_value: list, deep=0):
    node_df_list = []
    for each_child in child_value:
        if type(each_child) == list:
            pass
            # node_data.append('child{}-'.format(deep + 1) + str(i + 1) + '_list')
            # deep += 1
            # list_node_digui(each_key, child_dict_value, deep=deep)
        #             list_node_digui(each_child)
        elif type(each_child) == dict:
            child_dict_keys = each_child.keys()
            column_keys = []
            child_dict_data = []
            i = 0
            for each_child_key in child_dict_keys:
                each_key = father_key + "." + each_child_key
                column_keys.append(each_key)
                i += 1
                child_dict_value = each_child[each_child_key]

                # create node tree
                identifier = create_node_digui(tree, each_child_key, each_key, each_key, parent=father_key)
                print('identifier:', identifier)

                if type(child_dict_value) == list:
                    node_class = node.Node(child=identifier, identifier=father_key, child_type='list', deep=deep+1)
                    child_dict_data.append(node_class)
                    deep += 1


                    # tree.create_node(each_child_key, each_key, parent=father_key)

                    # get the next node dataframe by recursive
                    list_node_df = list_node_digui(tree, identifier, child_dict_value, deep=deep)
                    # give the node value by next node dataframe
                    tree.nodes[identifier].data = Nodex(list_node_df)

                #             node_digui_list(root_value)
                elif type(child_dict_value) == dict:
                    node_class = node.Node(child=identifier, identifier=father_key, child_type='dict', deep=deep + 1)
                    child_dict_data.append(node_class)
                    deep += 1

                    # tree.create_node(each_child_key, each_key, parent=father_key)

                    # get the next node dataframe by recursive
                    dict_node_df = dict_node_digui(tree, identifier, child_dict_value, deep=deep)
                    # give the node value by next node dataframe
                    tree.nodes[identifier].data = Nodex(dict_node_df)
                #             node_digui_dict(root_value)
                else:
                    child_dict_data.append(child_dict_value)
                    tree.nodes[identifier].data = Nodex(child_dict_value)
            child_dict_df = pd.DataFrame([child_dict_data], columns=column_keys)
            #             print (child_dict_df)
            node_df_list.append(child_dict_df)
        else:
            #             node_list_data.append(each_childa)
            # tree.nodes[identifier].data = Nodex(root_value)
            pass
    node_df = node_df_list[0]
    for j in range(len(node_df_list) - 1):
        if all(node_df_list[j].columns.values != node_df_list[j + 1].columns.values):
            print("axis=1,", node_df)
            node_df = pd.concat([node_df, node_df_list[j + 1]], axis=1)
        else:
            print("axis=0,", node_df)
            node_df = pd.concat([node_df, node_df_list[j + 1]], axis=0)
    print('node_df:', node_df)
    return node_df


def dict_node_digui(tree:Tree, father_key: str, child_value: dict, deep=0):
    #     print (child_value)
    node_keys = child_value.keys()
    column_keys = []
    node_dict_data = []
    i = 0
    for each_node in node_keys:
        each_key = father_key + "." + each_node
        column_keys.append(each_key)
        i += 1
        node_dict_value = child_value[each_node]

        # create node tree
        identifier = create_node_digui(tree, each_node, each_key, each_key, parent=father_key)
        print('identifier:', identifier)
        if type(node_dict_value) == list:
            node_class = node.Node(child=identifier, identifier=father_key, child_type='list', deep=deep + 1)
            node_dict_data.append(node_class)
            deep += 1

            # tree.create_node(each_node, each_key, parent=father_key)

            # get the next node dataframe by recursive
            list_node_df = list_node_digui(tree, identifier, node_dict_value, deep=deep)
            # give the node value by next node dataframe
            tree.nodes[identifier].data = Nodex(list_node_df)

        elif type(node_dict_value) == dict:
            node_class = node.Node(child=identifier, identifier=father_key, child_type='dict', deep=deep + 1)
            node_dict_data.append(node_class)
            deep += 1

            # get the next node dataframe by recursive
            dict_node_df = dict_node_digui(tree, identifier, node_dict_value, deep=deep)
            # give the node value by next node dataframe
            tree.nodes[identifier].data = Nodex(dict_node_df)

        else:
            node_dict_data.append(node_dict_value)
            tree.nodes[identifier].data = Nodex(node_dict_value)

    #     print (node_dict_data, column_keys)
    node_dict_df = pd.DataFrame([node_dict_data], columns=column_keys)
    print("node_dict_df", node_dict_df)
    return node_dict_df

if __name__=='__main__':

    tr = create_json_tree(test_data)
    tr.show()
    tr.show(data_property='dataframe')
    # print (tr.nodes)
    tr_nodes = tr.nodes
    nodes_list = tr_nodes.keys()
    for each_node in nodes_list:
        print (each_node, str(tr_nodes[each_node]))