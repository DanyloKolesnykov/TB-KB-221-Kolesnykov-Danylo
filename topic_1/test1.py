str = "abcdefg123"


def option_1_slices(str):
    reversed_str = str[::-1]
    print(reversed_str)
    return reversed_str
option_1_slices(str)


def option_2_cycle(str):
    reversed_str = " "
    for char in str:
        reversed_str = char + reversed_str
    print(reversed_str)
    return 0
option_2_cycle(str)


def option_3_reversedtext(str):
    reversed_str = ''.join(reversed(str))
    print(reversed_str)
    return 0
option_3_reversedtext(str)

