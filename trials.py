"""Python functions for JavaScript Trials 1."""


from operator import add


def output_all_items(items):
    for item in items:
        print(item)


def get_all_evens(nums):
    evens = []

    for num in nums:
        if num % 2 == 0:
            evens.append(num)

    return evens


def get_odd_indices(items):
    result = []

    for ind in range(len(items)):
        if ind % 2 != 0:
            result.append(items[ind])

    return result


def print_as_numbered_list(items):

    i = 1

    for item in items:
        print(f"{i}. {item}")
        i += 1


def get_range(start, stop):
    num_range = []

    for n in range(start, stop):
        num_range.append(n)

    return num_range


def censor_vowels(word):
    censored_word = ''
    for letter in word:
        if letter in ['a', 'e', 'i', 'o', 'u']:
            censored_word += '*'
        else:
            censored_word += letter

    return censored_word

def snake_to_camel(string):
    words = string.split('_')

    camel = ''

    for i, word in enumerate(words):
        if i == 0:
            camel  += word
        else:
            camel += word.capitalize()

    return camel


def longest_word_length(words):

    max_chars = 0

    for word in words:
        if len(word) > max_chars:
            max_chars = len(word)

    return max_chars


def truncate(string):

    trunc_string = ''

    for i, char in enumerate(string):
        if i == len(string) - 1 or char != string[i + 1]:
            trunc_string += char

    return trunc_string


def has_balanced_parens(string):
    parens = 0

    for c in string:
        if c == '(':
            parens += 1
        elif c == ')':
            parens -= 1

#          ((This) (is) (good))
#   open:F TT    F
# closed:T FF

    return parens == 0


def compress(string):

    compressed = ''

    curr_char = None
    curr_count = 0

    def add_char(char, n, char_str):
        if char:
            char_str += char
        if n > 1:
            char_str += str(n)

        return char_str

    for c in string:
        if c == curr_char:
            curr_count += 1
        else:
            compressed = add_char(curr_char, curr_count, compressed)
            curr_char = c
            curr_count = 1

    compressed = add_char(curr_char, curr_count, compressed)

    return compressed



# output_all_items([1, 'hello', True])
# print('\n')
# print(get_all_evens([7, 8, 10, 1, 2, 2]))
# print('\n')
# print(get_odd_indices([1, 'hello', True, 500]))
# print('\n')
# print_as_numbered_list([1, 'hello', True])
# print('\n')
# print(get_range(0, 5))
# print('\n')
# print(censor_vowels('hello world'))
# print('\n')
# print(snake_to_camel('hello_world_in_python'))
# print('\n')
# print(longest_word_length(['jellyfish', 'zebra']))
# print('\n')
# print(truncate('hi***!!!! wooow'))
# print('\n')
# print( truncate('aaaabbbbcccca'))
# print('\n')
# print(has_balanced_parens('((This) (is) (good))'))
# print('\n')
# print(has_balanced_parens('(Oh no!)('))
# print('\n')
# print(compress('aabbaabb'))
# print('\n')
# print(compress('abc'))
