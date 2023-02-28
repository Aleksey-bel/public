number_of_tickets = int(input("Введите количество билетов:"))
age = []
total_cost = 0
if number_of_tickets > 10:
    print("К сожалению, Вы не можете приобрести более 10 билетов в одном заказе!")
    print("------")
    print("Попробуйте снова=)")
else:
    for i in range(0, number_of_tickets):
        age = int(input(f"Введите возраст посетителя #{i+1}:"))

        if age < 18:
            print("Вход бесплатный!")
        elif 18 <= age < 25:
            total_cost += 990
        else:
            total_cost += 1390
    if number_of_tickets > 3:
        total_cost = total_cost * 0.9
        print('Итого со скидкой 10% к оплате:', total_cost)
    else:
        print('Итого к оплате:', total_cost)
