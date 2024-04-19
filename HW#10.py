chislo = int(input('Ведіть трицифрове число: '))

dig1 = chislo//100
chislo = chislo - dig1*100
dig2 = chislo//10
dig3 = chislo - dig2 * 10

s = dig1 + dig2 + dig3

print('Сума цифр', s)