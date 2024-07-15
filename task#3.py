def hanoi(n, source, target, auxiliary, state):
    if n == 1:
        state[target].append(state[source].pop())
        print(f"Перемістити диск з {source} на {target}")
        print_state(state)
        return
    hanoi(n-1, source, auxiliary, target, state)
    state[target].append(state[source].pop())
    print(f"Перемістити диск з {source} на {target}")
    print_state(state)
    hanoi(n-1, auxiliary, target, source, state)

def print_state(state):
    for peg in state:
        print(f"{peg}: {state[peg]}")
    print()

if __name__ == "__main__":
    n = int(input("Введіть кількість дисків: "))
    state = {
        'A': list(range(n, 0, -1)),  
        'B': [],
        'C': []
    }
    print("Початковий стан:")
    print_state(state)
    hanoi(n, 'A', 'C', 'B', state)
    print("Кінцевий стан:")
    print_state(state)

