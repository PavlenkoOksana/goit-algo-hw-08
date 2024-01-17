import heapq

def minimize_cable_costs(cables):
    i = 0
    # Шаг 1: Створюємо купу та додаємо всі кабелі
    heapq.heapify(cables)
    print (f"крок {i}-й, вихідна купа {cables}") 

    # Поки що в купі є більше одного кабелю
    while len(cables) > 1:
        # Крок 2: Вилучаємо два кабелі з мінімальними довжинами
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        # Крок 3: З'єднуємо їх та обчислюємо нову довжину
        new_cable = cable1 + cable2

        # Додаємо новий кабель назад до купи
        heapq.heappush(cables, new_cable)
        i += 1
        print (f"крок {i}-й, купа {cables}") 

    # Коли в купі залишається лише один кабель, це підсумкове об'єднання
    return cables[0]

cable_lengths = [2, 3, 5, 7, 1]
result = minimize_cable_costs(cable_lengths)

print(f"Мінімальні загальні витрати з'єднання всіх кабелів: {result}")