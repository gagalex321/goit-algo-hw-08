# Завдання 3
# Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
# Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
# Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.

import heapq


def min_cost(cables):
    if len(cables) <= 1:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)

        new_cable = cable1 + cable2
        total_cost += new_cable

        heapq.heappush(cables, new_cable)

        print(f"Об'єднання: {cable1} + {cable2} = {new_cable}")

    return total_cost


def main():
    cables = [4, 3, 2, 6]

    print(f"Довжини кабелів: {cables}")
    cost = min_cost(cables)

    print(f"Мінімальні загальні витрати: {cost}")


if __name__ == "__main__":
    main()

'''
Довжини кабелів: [4, 3, 2, 6]
Об'єднання: 2 + 3 = 5
Об'єднання: 4 + 5 = 9
Об'єднання: 6 + 9 = 15
Мінімальні загальні витрати: 29
'''