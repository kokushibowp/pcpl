import sys
import math

def input_float_value(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Ошибка: введите корректное число!")

def solve_biquadratic(A, B, C):
    if A == 0:
        if B == 0:
            return ["Бесконечно много решений"] if C == 0 else []
        else:
            val = -C / B
            if val < 0:
                return []
            elif val == 0:
                return [0.0]
            else:
                sqrt_val = math.sqrt(val)
                return [-sqrt_val, sqrt_val]
    D = B * B - 4 * A * C
    if D < 0:
        return []
    elif D == 0:
        y = -B / (2 * A)
        if y < 0:
            return []
        elif y == 0:
            return [0.0]
        else:
            sqrt_y = math.sqrt(y)
            return [-sqrt_y, sqrt_y]
    else:
        sqrt_D = D ** 0.5
        y1 = (-B + sqrt_D) / (2 * A)
        y2 = (-B - sqrt_D) / (2 * A)
        roots = []
        for y in (y1, y2):
            if y > 0:
                sqrt_y = math.sqrt(y)
                roots.extend([-sqrt_y, sqrt_y])
            elif abs(y) < 1e-15:
                roots.append(0.0)
        return roots

def parse_args():
    coefficients = []
    args = sys.argv[1:]
    for i, arg in enumerate(args[:3]):
        try:
            coefficients.append(float(arg))
        except ValueError:
            print(f"Аргумент {arg} некорректен. Будет запрошен ввод с клавиатуры.")
    while len(coefficients) < 3:
        coefficients.append(input_float_value(f"Введите коэффициент {'ABC'[len(coefficients)]}: "))
    return coefficients

def main():
    A, B, C = parse_args()
    print(f"Решаем уравнение: {A}x^4 + {B}x^2 + {C} = 0")
    roots = solve_biquadratic(A, B, C)
    if len(roots) == 0:
        print("Действительных корней нет.")
    elif len(roots) == 1 and isinstance(roots[0], str):
        print(roots[0])
    else:
        print("Действительные корни уравнения:", sorted(roots))

if __name__ == "__main__":
    main()
