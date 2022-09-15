# -*- coding: utf-8 -*-
"""
main file containes the module
"""


class PySuit:
    '''
    sort dict by keys and values
    '''
    def __init__(self):
        pass

    def dictsort(self, dictionary, flag):
        """
        Sorting dict by keys or values
        """
        try:
            sortedDict = {}
            if flag.lower() == "values":
                # Sorting dict by values
                sorted_dict = sorted(list(dictionary.values()), key=lambda x: (len(str(x)), str(x)))
                for value in sorted_dict:
                    key_result = [key for key in dictionary if dictionary[key] == value]
                    sortedDict[key_result[0]] = value
            else:
                # Sorting dict by keys
                sorted_dict = sorted(list(dictionary.keys()), key=lambda x: (len(str(x)), str(x)))
                sortedDict = {key: dictionary[key] for key in sorted_dict}

            return sortedDict
            
        except Exception as e:
            raise e
            

if __name__ == '__main__':
    pysuit = PySuit()
