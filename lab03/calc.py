def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

if __name__ == "__main__":
    x = float(input("Первое число: "))
    y = float(input("Второе число: "))
    print("Сумма:", add(x, y))
    print("Разность:", subtract(x, y))
    print("Произведение:", multiply(x, y))
