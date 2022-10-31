# -*- coding: utf-8-*-
"""
###### Dict Collections #######
## Version 0.1 ##

# ---- List of fuctions -----
# dictsort = dict by keys and values are sorted
"""
import logging
from pysuit.interface import PySuit


class DictCollections(PySuit):
    """
    List of dict collections
    """

    __name__ = "pysuit.DictCollections()"

    def dictsort(self, dictionary, flag='keys'):
        """
        Sorting dict by keys or values
        """
        try:
            final_dict = {}
            # Sorting dict by values
            if flag.lower() == "values":
                sorted_dict = sorted(
                    list(dictionary.values()),
                    key=lambda x: (len(str(x)), str(x))
                )
                for value in sorted_dict:
                    key_result = [
                        key for key in dictionary if dictionary[key] == value
                    ]
                    final_dict[key_result[0]] = value
            # Sorting dict by keys
            else:
                sorted_dict = sorted(
                    list(dictionary.keys()),
                    key=lambda x: (len(str(x)), str(x))
                )
                final_dict = {key: dictionary[key] for key in sorted_dict}

            return final_dict

        except Exception as errors:
            logging.exception(f"error while accessing the dict: {errors}")
            raise errors

    def dict_key_searching(self, dictionary, key):
        """
        Returns a tuple containing the values of the specified key
        """
        try:
            if key:
                if type(dictionary) == dict:
                    if dictionary:
                        empty_list = []
                        # Match specified key with outer keys
                        outer_key = dictionary.get(key, False)
                        if outer_key:
                            empty_list.append(outer_key)
                        for value in dictionary.values():
                            if type(value) == dict:
                                inner_key = self.dict_key_searching(value, key)
                                # Extend the empty_list with inner keys after match with specified key
                                empty_list.extend(inner_key)
                        return empty_list
                else:
                    raise AttributeError('Only dict type of data is allowed')
            else:
                raise TypeError("Key not specified")
        except Exception as errors:
            logging.exception(f"error while accessing the dict: {errors}")
            raise errors
