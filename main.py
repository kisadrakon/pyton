summ = 0
for i in range(1, int(input("Введите количество билетов:"))+1):
    age = int(input(f"Сколько лет посесителю {i}:"))
    if 18 <= age < 25:
        summ += 990
    elif age >= 25:
        summ += 1390
if i > 3:
    summ *= 0.9
    print(f"\nCумма к оплате со скидкой:{summ} руб. за {i} чел.")
else:
    print(f"\nCумма к оплате:{summ} руб. за {i} чел.")