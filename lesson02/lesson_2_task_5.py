def month_to_season(month):
   
    if month in (12, 1, 2):
        return "Зима"
    elif month in (3, 4, 5):
        return "Весна"
    elif month in (6, 7, 8):
        return "Лето"
    elif month in (9, 10, 11):
        return "Осень"
    else:
        return "Ошибка: укажите номер месяца от 1 до 12"

# Примеры вызова функции с разными номерами месяцев
print(f"Месяц 2: {month_to_season(2)}")   # Зима
print(f"Месяц 5: {month_to_season(5)}")   # Весна
print(f"Месяц 8: {month_to_season(8)}")   # Лето
print(f"Месяц 11: {month_to_season(11)}") # Осень
print(f"Месяц 15: {month_to_season(15)}") # Ошибка