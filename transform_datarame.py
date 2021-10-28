import pandas as pd
import json
import re

from create_tensor import create_json_tree
import node

def get_treelib_data(json_data:dict):
    tr = create_json_tree(json_data)
    print (tr.show())
    tr_nodes = tr.nodes
    print (tr_nodes['root'])
    print(type(tr_nodes['root']))
    nodes_list = tr_nodes.keys()
    for each_node in nodes_list:
        # identifier = re.findall("identifier=(.*?),",str(tr_nodes[each_node]),re.S)[0]
        node = tr.get_node(each_node)
        print (each_node, tr.depth(node))
        print ('----------------')
        print (tr.nodes[each_node].data.dataframe)

if __name__=='__main__':
    test_data = {
        'data':
            [
                {'k_11': 'v_11'},
                {'k_12': 'v_12'},
                {'k_13': {
                    'k_21': [
                        {'k_31': 'v_31.1'},
                        {'k_31': 'v_31.2'},
                        {'k_31': 'v_31.3'}
                    ],
                    'k_22': [
                        {'k_32': 'v_32.1'},
                        {'k_32': 'v_32.2'},
                        {'k_32': 'v_32.3'},
                        {'k_32': 'v_32.4'},
                        {'k_32': 'v_32.5'}
                    ],
                    'k_23': 'v_23'
                }
                },
                {'k_14': [
                    {'k_21': 'v_21.1'},
                    {'k_21': 'v_21.2'},
                    {'k_21': 'v_21.3'}
                ]
                }
            ]
    }
    f = open('定期寿险智能问卷.json')
    json_data = json.loads(f.read())
    get_treelib_data(test_data)