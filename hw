import itertools

#Завдання 1
print("Завдання 1")
print("x | y | z | x ↓ y | z + y | f")

def not_func(a, b):
    return int(not(a or b))

def sum_func(a, b):
    return a ^ b

def eq_func(a, b):
    return int(a == b)

f1_vec = []
for x, y, z in itertools.product([0, 1], repeat=3):
   res_not = not_func(x, y)
   res_sum = sum_func(z, y)
   res_eq = eq_func(res_not, res_sum)
   f1_vec.append(res_eq)
   print(f"{x} | {y} | {z} |   {res_not}   |   {res_sum}   | {res_eq}")

print("\n Результат f =", "".join(map(str, f1_vec)))



#Завдання 2
#fn(fk(y, y, x), x, y)
print("-" * 35)
print("Завдання 2")
print("x | y | z | f7 | f9")

f7_vec = "10110101"
f9_vec = "10100110"

def f7(x, y, z):
    return int(f7_vec[(x<< 2) | (y << 1) | z])


def f9(x, y ,z):
    return int(f9_vec[(x << 2) | (y << 1) | z])


for x, y, z in itertools.product([0, 1], repeat=3):
    val1 = f7(x, y, z)
    val2 = f9(x, y, z)
    print(f"{x} | {y} | {z} |  {val1} |  {val2}")

print("-" * 40)

h_values = []
print("h | x | y | f7 | f9 | y | y | x | x | y")
for x, y in itertools.product([0, 1], repeat=2):
    num2 = f9(y, y, x)
    num1 = f7(num2, x, y)
    h_values.append(num1)
    print(f"{" "} | {x} | {y} |  {num1} |  {num2} | {y} | {y} | {x} | {x} | {y}")
print("\nh(x, y) =", "".join(map(str, h_values)))

print("-" * 35)



#Завдання 3
#f(x, y, z) = (0011 0011)
print("Завдання 3")

f_vec = "00110011"

print("Фіктивні і суттєві змінні")

def f(x, y ,z):
    return int(f_vec[(x << 2) | (y << 1) | z])

def is_fic(index):
    for x in [0, 1]:
        for y in [0, 1]:
            for z in [0, 1]:
                args0 = [x, y, z]
                args1 = [x, y, z]
                args0[index] = 0
                args1[index] = 1
                if f(*args0) != f(*args1):
                    return False
    return True

names = ["x", "y", "z"]
essential = []

for i, name in enumerate(names):
    if is_fic(i):
        print(f"Зміна {name} - фіктивна")
    else:
        print(f"Зміна {name} - суттєва")
        essential.append(i)

print("\nФункція через істотні змінні")
print("y | f")
for y in [0, 1]:
    print(f"{y} | {f(0, y, 0)}")
print("f(y) = y")

print("-" * 35)

#Завдання 4
#3) на множині {1, 2, 3, 4, 6, 12, 15} задано відношення ρ: xρy ⇔ x/y (x ділиться на y);
#Чи є дане відношення відношенням порядку? Строгого порядку?
# Знайти, де це можливо, найменший і найбільший елементи.
# Знайти мінімальний і максимальний елементи.
# Побудувати матрицю відношення, граф відношення або діаграму Хассе.
print("Завдання 4")
array = [1, 2, 3, 4, 6, 12, 15]
n = len(array)

def rel(x, y):
    return x % y == 0


#Аналіз відношення
print("Аналіз відношення")

is_ref = all(rel(x, x) for x in array)
is_irref = all(not rel(x, x) for x in array)
is_sim = all(rel(x, y) == rel(y, x) for x in array for y in array)
is_antisim = all(
    (
        not rel(x, y)
        and rel(y, x)
    )
    or (x == y) for x in array for y in array
)

is_asim = all(
    not
    (
        rel(x, y) and rel(y, x)
    )
    for x in array for y in array
)
is_trans = all(
    not (
        rel(x, y) and rel(y, z)
    )
    or rel(x, z)
    for x in array for y in array for z in array
)

print(f"Рефлексивне: {is_ref}")
print(f"Антирефлексивне: {is_irref}")
print(f"Симетричне: {is_sim}")
print(f"Антисиметричне: {is_antisim}")
print(f"Асиметричне: {is_asim}")
print(f"Транзитивне: {is_trans}")

if is_irref and is_asim and is_trans:
    print("Відношення строгого порядку")
if is_ref and is_antisim and is_trans:
    print("Відношення нестрого порядку")
else:
    print("Відношення не є відношенням порядку")
print("-" * 35)


#Найбільший та найменший елементи
print("Найбільший та найменший елементи")

smallest = next((s for s in array if all(rel(x, s) for x in array)), None)
largest = next((g for g in array if all(rel(g, x) for x in array)), None)
minimal = [s for s in array if not any(x != s and rel(s, x) for x in array)]
maximal = [g for g in array if not any(x != g and rel(x, g) for x in array)]

print(f"\nНайменший = {smallest if smallest is not None else "Не існує"}")
print(f"Найбільший = {largest if largest is not None else "Не існує"}")
print(f"Мінімальні = {', '.join(map(str, minimal))}")
print(f"Максимальні = {', '.join(map(str, maximal))}")
print("-" * 35)


#Матриця відношення
print("Матриця відношення")

matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if array[i] % array[j] == 0:
            matrix[i][j] = 1

print("    ", " ".join([f"{val:2}" for val in array]))
for i in range(n):
    row = " ".join([f"{val:2}" for val in matrix[i]])
    print(f"{array[i]:2} | {row}")
