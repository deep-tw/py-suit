# -*- coding: utf-8-*-
"""
###### Nested Collections #######
## Version 0.1 ##

# ---- List of fuctions -----
# removNestings = sort a nested to single 
"""

from pysuit.interface import PySuit


class NestedCollections(PySuit):

    """
        Nested to single Sort 
    """

    __name__ = "pysuit.NestedCollections()"


    """ 
    created function ===> removNested
    """
    output = []

    sorted_dict = {}

    def removNestings(self,nested_element):

        """
        function used for removing nested
        """

        try:
           
            if type(nested_element) == dict:
                for key,value in nested_element.items():
                    if isinstance(value, dict):

                        self.removNestings(value)
                    else:
                        self.sorted_dict.update({key:value})
                return self.sorted_dict

            elif type(nested_element) == set:
                for element in nested_element:
                    if type(element) in [tuple,frozenset]:

                        self.removNestings(element)
                    else:
                        self.output.append(element)


            else:
                for element in nested_element:
                    if type(element) in [list,tuple,set,dict]:
                        self.removNestings(element)
                        if type(element) == dict:
                            for key, value in element.items():
                                self.output.append(key)
                                if type(value) == list:
                                    self.removNestings(element)
                                else:
                                    self.output.append(value)
                    else:
                        self.output.append(element)

        except Exception as e:

            raise e

        if type(nested_element) is tuple:
            return tuple(self.output)
        elif type(nested_element) is set:
            return set(self.output)
        elif type(nested_element) is dict:
            return self.sorted_dict
        else:
            return self.output
            


            