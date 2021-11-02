import pandas as pd
import copy

class TD(object):

    def __init__(self):
        self._base_data = []

    def call_append(func):
        def helper(self, x):
            helper.calls.append(x)
            return func(self,x)

        helper.calls = []
        return helper

    @call_append
    def append_result(self, value):
        return value

    def get_start(self, data: dict):
        root_keys = data.keys()
        for each_key in root_keys:
            column = [each_key]
            each_value = data[each_key]

            if type(each_value) == list:
                return self.get_list_recurse(father=each_key, data=each_value, column=[each_key], vector=['list'])


            elif type(each_value) == dict:
                return self.get_dict_recurse(father=each_key, data=each_value, column=[each_key], vector=['dict'])

            else:
                vector = [each_value]
                self.append_result((column, vector))


    def get_list_recurse(self, father: str, data: list, column: list, vector: list):
        print('first list :', column, vector)
        for each_child in data:
            new_column = copy.deepcopy(column)
            new_vector = copy.deepcopy(vector)
            new_column.append(father)

            if type(each_child) == list:
                self.get_list_recurse(father=father, data=each_child, column=column, vector=vector)

            elif type(each_child) == dict:
                self.get_dict_recurse(father=father, data=each_child, column=column, vector=vector)

            else:

                new_vector.append(each_child)
                print(new_column, new_vector)
                self.append_result((new_column, new_vector))

    def get_dict_recurse(self, father: str, data: dict, column: list, vector: list):
        node_keys = data.keys()
        for each_key in node_keys:
            new_father = father + '.' + each_key
            new_column = copy.deepcopy(column)
            new_vector = copy.deepcopy(vector)
            new_column.append(new_father)

            each_value = data[each_key]
            if type(each_value) == list:
                new_vector.append('list')
                self.get_list_recurse(father=new_father, data=each_value, column=new_column, vector=new_vector)

            elif type(each_value) == dict:
                new_vector.append('dict')
                self.get_dict_recurse(father=new_father, data=each_value, column=new_column, vector=new_vector)

            else:
                print('the data now:', column, vector)
                new_vector.append(each_value)
                print(new_column, new_vector)
                self.append_result((new_column, new_vector))

    def to_dataframe(self, data:dict):
        self.get_start(data)


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
                }`
            ]
    }
    td = TD()
    td.get_start(test_data)
    data = td.append_result.calls
    names = locals()
    for i in range(len(data)):
        names['df' + str(i)] = pd.DataFrame([data[i][1]], columns=data[i][0])
        print(names['df' + str(i)])
    #     df = pd.DataFrame(each[1], columns=each[0])
    df = pd.concat([names['df' + str(i)] for i in range(len(data))])
    print (df)