# Завдання 1
# Напишіть алгоритм (функцію), який знаходить найменше значення у двійковому дереві пошуку або в AVL-дереві. 
# Візьміть будь-яку реалізацію дерева з конспекту чи з іншого джерела.


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Для знаходження найменшого значення у двійковому дереві пошуку (BST) 
# потрібно перейти до найлівішого вузла дерева.
def find_min(root):
    if root is None:
        return None

    while root.left is not None:
        root = root.left

    return root.value


# Приклад
def main():
    # Створення двійкового дерева пошуку
    root = Node(8)
    root.left = Node(3)
    root.right = Node(10)
    root.left.left = Node(1)
    root.left.right = Node(6)
    root.right.right = Node(14)

    # Пошук мінімального значення
    result = find_min(root)

    if result is not None:
        print(f"Найменше значення у дереві: {result}")
    else:
        print("Дерево порожнє.")


if __name__ == "__main__":
    main()

'''
Найменше значення у дереві: 1
'''