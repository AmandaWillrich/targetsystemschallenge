user_input = input('Digite uma frase para invertê-la: ')


def reverse_string(user_input):
    new_string = ''
    index = len(user_input)
    for i in range(index - 1, -1, -1):
        new_string += user_input[i]
    return new_string


print(reverse_string(user_input))
