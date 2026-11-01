 import itertools

# ==========================================
# Завдання 1
# f(1110 1100 1111 1001)
# ==========================================
print("Завдання 1.1")

f_vec = "1110110011111001"
def f_1(x, y, z, w):
    return int(f_vec[(x << 3) | (y << 2) | (z << 1) | w])

pdnf = []
pknf = []
var_4 = ['x', 'y', 'z', 'w']

print("x | y | z | w | f")
for x, y, z, w in itertools.product([0, 1], repeat=4):
    val = f_1(x, y, z, w)
    print(f"{x} | {y} | {z} | {w} | {val}")

    term = (x, y, z, w)
    if val == 1:
        pdnf.append(term)
    else:
        pknf.append(term)

print("-" * 40)

# ДДНФ
dnf_parts = []
for t in pdnf:
    literals = [v if b == 1 else "¬" + v for v, b in zip(var_4, t)]
    dnf_parts.append("(" + "·".join(literals) + ")")
dnf = " + ".join(dnf_parts)
print("\nДДНФ:\n", dnf)

# ДКНФ
knf_parts = []
for t in pknf:
    literals = [v if b == 0 else "¬" + v for v, b in zip(var_4, t)]
    knf_parts.append("(" + " + ".join(literals) + ")")
knf = " · ".join(knf_parts)
print("\nДКНФ:\n", knf)


# ==========================================
# Завдання 3
# ==========================================
print("\n" + "="*40)
print("Завдання 3")

fvec = "01110101"
gvec = "1100000011101101"
hvec = "10111111110101111110111001110001"

def f_3(x, y, z):
    return int(fvec[(x << 2) | (y << 1) | z])

def g(x, y, z, w):
    return int(gvec[(x << 3) | (y << 2) | (z << 1) | w])

def h(x, y, z, w, v):
    return int(hvec[(x << 4) | (y << 3) | (z << 2) | (w << 1) | v])

# --- Функція f ---
pdnf_f = []
print("\nx | y | z | f")
for x, y, z in itertools.product([0, 1], repeat=3):
    val_f = f_3(x, y, z)
    print(f"{x} | {y} | {z} | {val_f}")
    if val_f == 1:
        pdnf_f.append((x, y, z))

dnf_f_parts = []
for t in pdnf_f:
    literals = [v if b == 1 else "¬" + v for v, b in zip(['x', 'y', 'z'], t)]
    dnf_f_parts.append("(" + "·".join(literals) + ")")
print("\nДДНФ - f:\n", " + ".join(dnf_f_parts))
print("-" * 40)

# --- Функція g ---
pdnf_g = []
print("\nx | y | z | w | g")
for x, y, z, w in itertools.product([0, 1], repeat=4):
    val_g = g(x, y, z, w)
    print(f"{x} | {y} | {z} | {w} | {val_g}")
    if val_g == 1:
        pdnf_g.append((x, y, z, w))

dnf_g_parts = []
for t in pdnf_g:
    literals = [v if b == 1 else "¬" + v for v, b in zip(['x', 'y', 'z', 'w'], t)]
    dnf_g_parts.append("(" + "·".join(literals) + ")")
print("\nДДНФ - g:\n", " + ".join(dnf_g_parts))
print("-" * 40)

# --- Функція h ---
pdnf_h = []
print("\nx | y | z | w | v | h")
for x, y, z, w, v in itertools.product([0, 1], repeat=5):
    val_h = h(x, y, z, w, v)
    print(f"{x} | {y} | {z} | {w} | {v} | {val_h}")
    if val_h == 1:
        pdnf_h.append((x, y, z, w, v))

dnf_h_parts = []
for t in pdnf_h:
    literals = [v if b == 1 else "¬" + v for v, b in zip(['x', 'y', 'z', 'w', 'v'], t)]
    dnf_h_parts.append("(" + "·".join(literals) + ")")
print("\nДДНФ - h:\n", " + ".join(dnf_h_parts))
print("-" * 40)


# ==========================================
# Завдання 4
# ==========================================
print("\n" + "="*40)
print("Завдання 4")

task4_set = [0, 2, 4, 6, 8, 10, 12, 14]
task4_vars = ['x', 'y', 'z', 't']

def f_task4(indices, var):
    pdnf_4 = []
    pknf_4 = []
    
    print("\nx | y | z | t | f")
    for term in itertools.product([0, 1], repeat=4):
        index = int("".join(map(str, term)), 2)
        val = 1 if index in indices else 0
        print(f"{' | '.join(map(str, term))} | {val}")

        if val == 1:
            pdnf_4.append(term)
        else:
            pknf_4.append(term)
    print("-" * 40)

    # ДДНФ
    dnf4_parts = []
    for t in pdnf_4:
        literals = [v if b == 1 else "¬" + v for v, b in zip(var, t)]
        dnf4_parts.append("(" + "·".join(literals) + ")")
    dnf4 = " + ".join(dnf4_parts)

    # ДКНФ
    knf4_parts = []
    for t in pknf_4:
        literals = [v if b == 0 else "¬" + v for v, b in zip(var, t)]
        knf4_parts.append("(" + " + ".join(literals) + ")")
    knf4 = " · ".join(knf4_parts)

    return dnf4, knf4

dnf4, knf4 = f_task4(task4_set, task4_vars)

print("\nДДНФ (Завдання 4):\n", dnf4)
print("\nДКНФ (Завдання 4):\n", knf4)
print("-" * 40)
