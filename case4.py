# Написать программу, которая сортирует список строк по длине, 
# сначала по возрастанию, а затем по убыванию.

spicok = ['зуб', 'кресло', 'аэропорт', 'мама', 'любовь', 'ум']

print(sorted(spicok, key=len))
print(sorted(spicok, key=len, reverse=True))
