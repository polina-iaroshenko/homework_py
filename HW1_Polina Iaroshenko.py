#!/usr/bin/env python
# coding: utf-8

# In[7]:


# задача про коктейли

import random

cocktails = [
    ["мартини","грейпфрутовый сок","жасмин","тоник","лосось"],
    ["клубника","какао","мята","марсала"],
    ["водка","томатный сок","лимонный сок","вустерширский соус","черный перец","сельдерей","лосось"],
    ["джин","вермут","ликер мараскино","апельсины","коктейльная вишня","лосось"],
    ["ром","авокадо","сахарный сироп","сливки","лимонный сок","лед"],
    ["красный вермут","тоник","апельсины","лосось"],
    ["только чай"]
        ]

random_cocktail = random.choice(cocktails)
for i in random_cocktail:
  if i == "лосось":
    random_cocktail.remove(i)

print(random_cocktail)


# In[11]:


# определитель уровня тревожности

b = input('Оцените силу вашей тревожности по шкале от 0 до 10: ')
a = None
try:
  a = float(b)
except:
  print('Недопустимые символы. Введите число от 0 до 10.') # добавила этот пункт, чтобы программа работала и в том случае, когда пользователь вводит ошибочное значение (например, буквы)
if a != None:
    if a == 0:
        print('Вы спокойны.')
    elif 0 < a <= 2:
        print('Кажется, вы испытываете легкую тревогу. Как молодой учёный перед встречей с научным руководителем.')
    elif 2 < a <= 5:
        print('Вы встревожены, как молодой учёный перед заседанием кафедры.')
    elif 5 < a <= 7.5:
        print('Вы испытываете достаточно сильную тревогу, как молодой учёный перед началом своего доклада. ')
    elif 7.5 < a <= 9.5:
        print('Уровень тревожности очень высок. Ваша тревога сопоставима с тревогой молодого учёного, которому пришло письмо от научного руководителя с пометкой "СРОЧНО".')
    elif 9.5 < a <= 10:
        print('Уровень тревоги предельно высокий. У Вас сегодня защита кандидатской диссертации?')
    else:
        print ('Введите число в пределах оценочной шкалы от 0 до 10.')


# In[10]:


#задача про открытки
postcards = {
    "Maria": "London",
    "Lorenzo": "Milan",
    "Oleg": "Canberra",
    "Hans": "Calgary",
    "Mark": "Milan",
    "Alex": "Krakow",
    "Julia": "Murmansk"
}
#добавим недостающие открытки
postcards["Petra"] = "Paris"
postcards["Ivan"] = "Moscow"
print(postcards) 

#исправим город для Олега
postcards["Oleg"] = "Sydney"
print(postcards) 

#выведем названия городов
res = set(dict.values(postcards))
print(res)
len(res)


# In[ ]:





# In[ ]:




