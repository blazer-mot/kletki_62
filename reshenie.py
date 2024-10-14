input_data = open('input.txt', 'r',) # ВАЖНО!!!  не забыть создать файл; открытие файла ввода
data = input_data.read()
a = data[0]
b = int(data[1])
if a == 'A' or a == 'C' or a == 'E' or a == 'G':
    a1 = 1
if a == 'B' or a == 'D' or a == 'F' or a == 'H':
    a1 = 2
if a1 % 2 == 0 or b % 2 == 0:
    out = 'WHITE'
if a1 % 2 != 0 or b % 2 != 0:
    out = 'BLACK'
output_data = open('output.txt', 'w') # созпдние и открытие файла для вывода ответа
output_data.write(str(out)) # преобразование числа в строку при выводе и сам вывод
input_data.close() # закрытие файла считывания 
output_data.close() # закрытия файла вывода