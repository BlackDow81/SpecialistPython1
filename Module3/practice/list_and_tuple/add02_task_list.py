# Пользователь вводит на экран дату в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.

# Подсказка: создайте списки с названием дней и названиями месяцев
# Примечание: для экономии времени, можно ограничить номер дня десятью.
# Примечание: склонениями названий можно принебречь

days = [" ", "первое", "второе", "третье", "четвертое", "пятое",
        "шестое", "седьмое", "восьмое", "девятое", "десятое",
        "одиннадцатое", "двенадцатое", "тринадцатое", "четырнадцатое",
        "пятнадцатое", "шестнадцатое", "семнадцатое", "восемнадцатое","девятнадцатое",
        "двадцатое", "двадцать первое", "двадцать второе", "двадцать третье",
        "двадцать четвертое", "двадцать пятое", "двадцать шестое", "двадцать седьмое",
        "двадцать восьмое", "двадцать девятое", "тридцатое", "тридцать первое"]
months = [" ", "января", "февраля", "марта", "апреля", "мая", "июня",
          "июля", "августа", "сентября", "октября", "ноября", "декабря"]
date = input("please enter a date in format dd.mm.yyyy : ")
splitted_date = date.split(".")
required_format = []
for element in splitted_date:
        required_format.append(int(element))
print(days[required_format[0]], months[required_format[1]], required_format[2], "года")
