import csv
score = 0

print("-------Добро пожаловать на тест по пайтону, надесь вы наберете достаточное количество очков-------")
print()

with open('opros.csv', newline='') as opros:
  reader = csv.reader(opros, delimiter=",")
  for row in reader:
    print(row[0])
    print(row[1], row[2], row[3])
    otv = input("Введите вариант ответа(a, b, c): ")
    
    if otv == 'a':
      if row[1] == row[4]:
        print("Правильно!")
        score += 5
      else:
        print("Неправильно!")
    elif otv == 'b':
      if row[2] == row[4]:
        print("Правильно")
        score += 5
      else:
        print("Неправильно")
    elif otv == 'c':
      if row[3] == row[4]:
        print("Правильно")
        score += 5
      else:
        print("Неправильно")
    else:
      print("Такого ответа не существует!")

print("Заработанные баллы - " + str(score))
print("Спасибо за то, что вы прошли этот тест!")

if score == 100:
  print("Ваша оценка - A")
elif score >= 95:
  print("Ваша оценка - A-")
elif score >= 90:
  print('Ваша оценка - B+')
elif score >= 85:
  print("Ваша оценка - B")
elif score >= 80:
  print('Ваша оценка - B-')
elif score >= 75:
  print("Ваша оценка - C+") 
elif score >= 70:
  print("Ваша оценка - C") 
elif score >= 65:
  print("Ваша оценка - C-")
elif score >= 60:
  print("Ваша оценка - D-")
else:
  print("Ваша оценка - F") 