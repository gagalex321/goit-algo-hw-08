# Завдання 2
# Напишіть алгоритм (функцію), який знаходить суму всіх значень у двійковому дереві пошуку або в AVL-дереві. 
# Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sum_tree(root):
    if root is None:
        return 0

    return root.value + sum_tree(root.left) + sum_tree(root.right)


def main():
    # Створення двійкового дерева пошуку
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)

    # Обчислення суми значень
    result = sum_tree(root)

    print(f"Сума всіх значень у дереві: {result}")


if __name__ == "__main__":
    main()

'''
Сума всіх значень у дереві: 42
'''