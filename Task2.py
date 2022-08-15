'''
2.	Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
    для всех значений предикат.
'''

def table(x, y, z):
    print(f"¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z} is {(not (x or y or z)) == (not x and not y and not z)}")
    return (not (x or y or z)) == (not x and not y and not z)

if __name__ == "__main__":
    if (table(0, 0, 0) and table(0, 0, 1) and table(0, 1, 0) and
            table(0, 1, 1) and table(1, 0, 0) and table(1, 0, 1) and
            table(1, 1, 0) and table(1, 1, 1)):
        print("Истинно")
    else:
        print("Ложно")
