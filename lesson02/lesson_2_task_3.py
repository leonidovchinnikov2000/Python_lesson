import math

def square(side):
   
    area = side * side
    return math.ceil(area)

result1 = square(5)      # целая сторона
result2 = square(3.2)   # дробная сторона
result3 = square(4.7)   # ещё один пример дробной стороны

print(f"Площадь квадрата со стороной 5: {result1}")
print(f"Площадь квадрата со стороной 3.2: {result2}")
print(f"Площадь квадрата со стороной 4.7: {result3}")