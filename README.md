# Домашня робота №5

Сивоконь Анастасія  
Група: ІК-61  
Варіант: 22  
---

## Завдання 1

**Умова:**

![Умова](https://github.com/user-attachments/assets/b21909a3-fadb-4c24-aebd-83840c4b315e)

**Результат:** вектор значень f = (0101 1001).

Реалізація — у файлі [`hw5.py`](hw5/hw5.py), розділ `# Завдання 1`.

---

## Завдання 2

**Умова:**

![Умова 1](https://github.com/user-attachments/assets/69c85f15-f88e-48ba-9fb5-602ba946ac22)
![Умова 2](https://github.com/user-attachments/assets/2599b348-f37f-429b-8f3d-5cf1c3668d04)
![Умова 3](https://github.com/user-attachments/assets/356c2ea2-ce18-4721-a98a-0d25c49e6e45)
![Умова 4](https://github.com/user-attachments/assets/aa752324-ea85-4fcc-b76f-c0671e69d5af)

**Результат:** h(x, y) = (0111).

Реалізація — у файлі [`hw5.py`](hw5/hw5.py), розділ `# Завдання 2`.

---

## Завдання 3

**Умова:**

![Умова 1](https://github.com/user-attachments/assets/0b98eb5b-37e0-4c8d-bbab-7470cc99731e)
![Умова 2](https://github.com/user-attachments/assets/3c03cf00-7bf0-4999-b409-d2fc454a638a)

**Результат:**
- x — фіктивна
- y — суттєва
- z — фіктивна
- f(y) = y

Реалізація — у файлі [`hw5.py`](hw5/hw5.py), розділ `# Завдання 3`.

---

## Завдання 4 (Таран 4.1, пункти 1, 3, 4, 5)

**Умова:**

![Умова 1](https://github.com/user-attachments/assets/73d304eb-9bae-4de3-b406-b33228dfec4c)
![Умова 2](https://github.com/user-attachments/assets/8e40064c-ea53-430d-a24f-285b900945d1)

**Результат:**
- Відношення нестрогого порядку.
- Найменший елемент: не існує (НСК усіх = 60 не належить до X)
- Найбільший елемент: 1
- Мінімальні елементи: {12, 15}
- Максимальні елементи: {1}

Реалізація — у файлі [`hw5.py`](hw5/hw5.py), розділ `# Завдання 4`.

# Домашня робота №7

Сивоконь Анастасія  
Група: ІК-61  
Варіант: 22  
---

## Завдання 1

**Умова:** 

![Умова 1](https://github.com/user-attachments/assets/c56be562-d5ec-4c7e-90d8-f73b9ec32619)

![Умова 2](https://github.com/user-attachments/assets/7e7f107e-5bfd-47f8-b2b4-3773244415bd)

**Результат:** 

ДДНФ: (¬x·¬y·¬z·¬w) + (¬x·¬y·¬z·w) + (¬x·¬y·z·¬w) + (¬x·y·¬z·¬w) + (¬x·y·¬z·w) + (x·¬y·¬z·¬w) + (x·¬y·¬z·w) + (x·¬y·z·¬w) + (x·¬y·z·w) + (x·y·¬z·¬w) + (x·y·z·w)

ДКНФ: (x + y + ¬z + ¬w) · (x + ¬y + ¬z + w) · (x + ¬y + ¬z + ¬w) · (¬x + ¬y + z + ¬w) · (¬x + ¬y + ¬z + w)

МДНФ: ¬x·¬z + ¬y·¬z + ¬y·¬w + ¬z·¬w + x·z·w


Реалізація — у файлі [`hw7.py`](hw7/hw7.py), розділ `# Завдання 1`.

---

## Завдання 3

**Умова:** 

![Умова 1](https://github.com/user-attachments/assets/5623e82a-17ab-44cd-adfb-143208aabe7c)
![Умова 2](https://github.com/user-attachments/assets/4079d62c-30cf-4e52-ae2b-01a7ba416c35)

**Результат:** 

f:
МДНФ: z + ¬x·y

g:
МДНФ: ¬y·¬z +  x·¬z +  x·¬y·¬w +  x·y·w

h:
МДНФ: ¬y·¬v + ¬x·¬y·w + ¬x·z·v + ¬x·z·w + y·¬z·v + y·w·v + x·¬y·¬w + x·¬z·w·¬v + ¬x·¬z·¬w·¬v

Реалізація — у файлі [`hw7.py`](hw7/hw7.py), розділ `# Завдання 3`.

---

## Завдання 4 (Таран 7.4)

**Умова:**

![Умова 1](https://github.com/user-attachments/assets/7227ca49-7c85-4cfd-a5bd-de708f67c0b1)
![Умова 2](https://github.com/user-attachments/assets/afec9548-01db-4a2a-8fea-38c1b9c2f8e9)


**Результат:**

ДДНФ: (¬x·¬y·¬z·¬t) + (¬x·¬y·z·¬t) + (¬x·y·¬z·¬t) + (¬x·y·z·¬t) + (x·¬y·¬z·¬t) + (x·¬y·z·¬t) + (x·y·¬z·¬t) + (x·y·z·¬t)

ДКНФ: (x + y + z + ¬t) · (x + y + ¬z + ¬t) · (x + ¬y + z + ¬t) · (x + ¬y + ¬z + ¬t) · (¬x + y + z + ¬t) · (¬x + y + ¬z + ¬t) · (¬x + ¬y + z + ¬t) · (¬x + ¬y + ¬z + ¬t)

МДНФ: ¬t

Реалізація — у файлі [`hw7.py`](hw7/hw7.py), розділ `# Завдання 4`.
