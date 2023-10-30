def count_vowels(string):
    vowels = "aeiou"  # гласные буквы в английском алфавите
    return sum(1 for char in string.lower() if char in vowels)

def find_string_with_most_vowels(strings):
    return max(strings, key=count_vowels)

# Запись данных в файл F1
with open("f1.txt", 'w') as f:
    while True:
        a = input('Введите строку, которую хотите добавить в файл: ')
        if a == "":
            break
        else:
            f.write(a + '\n')  # Добавляем перенос строки после каждой строки

# Чтение данных из файла F1 и запись в файл F2
with open("f1.txt", "r") as f, open("f2.txt", "w") as ff:
    lines = f.readlines()
    max_vowels_line = find_string_with_most_vowels(lines)
    j = 0  # Инициализация счетчика строк
    for i, line in enumerate(lines):
        if line != max_vowels_line:
            ff.write(line)
        else:
            b = i + 1  # Сохраняем номер строки с наибольшим количеством гласных
        j += 1  # Увеличиваем счетчик строк

print(f"Номер строки равен {b}")
