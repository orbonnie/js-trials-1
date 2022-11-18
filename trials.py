"""Python functions for JavaScript Trials 1."""


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
    pass  # TODO: replace this line with your code


def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
