import re

# Определение словаря для хранения информации о предметах
subjects = {}

# Открытие и чтение файла
with open('classes.txt', 'r') as file:
    for line in file:
        # Извлечение названия предмета и информации о занятиях
        subject, info = line.split(':')
        # Извлечение количества занятий с помощью регулярных выражений
        lectures = sum(int(num) for num in re.findall(r'\d+', info))
        # Добавление информации о предмете в словарь
        subjects[subject] = lectures

# Вывод словаря на экран
for subject, lectures in subjects.items():
    print(f'Предмет: {subject}, Общее количество занятий: {lectures}')
