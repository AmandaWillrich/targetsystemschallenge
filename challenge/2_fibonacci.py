# Fibonacci Sequence

number = int(input('Digite um número: '))

a, b = 0, 1

while a < number:
    a, b = b, a + b

if a == number:
    print('O número digitado está presente na Sequência Fibonacci')
else:
    print('O número digitado não está presente na Sequência Fibonacci')
