# Created by Leon Hunter at 3:57 PM 10/23/2020
class StringManipulator(object):
    def get_hello_world(self):
        return "Hello World"  # TODO - Implement solution

    def concatenate(self, value_to_be_added_to, value_to_add):
        a = str(value_to_be_added_to) + str(value_to_add)
        return a # TODO - Implement solution

    def substring_inclusive(self, string_to_fetch_from, starting_index, ending_index):
        b = string_to_fetch_from[starting_index:ending_index+1]
        return b  # TODO - Implement solution

    def substring_exclusive(self, string_to_fetch_from, starting_index, ending_index):
        c = string_to_fetch_from[starting_index+1:ending_index]
        return c # TODO - Implement solution

    def compare(self, first_value, second_value):
        return first_value == second_value  # TODO - Implement solution

    def get_middle_character(self, string_to_fetch_from):
        d= len(string_to_fetch_from)//2  # TODO - Implement solution
        return d
    def get_first_word(self, string_to_fetch_from):
        return string_to_fetch_from.split()[0]  # TODO - Implement solution

    def get_second_word(self, string_to_fetch_from):
        return string_to_fetch_from[1]  # TODO - Implement solution

    def reverse(self, string_to_be_reversed):
        return string_to_be_reversed[::-1]  # TODO - Implement solution
