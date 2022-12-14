# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z 
# (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

for i in range(8):
    x = bool(i & 1)
    y = bool(i & 2)
    z = bool(i & 4)
    print(x, y, z)
    
    if not (x or y or z) is (not(x) and not(y) and not(z)):
        print('Утверждение истинно')
    else:
        print('Утверждение ложно')