package calculator

import "fmt"

// Calculate выполняет математическую операцию
func Calculate(a, b float64, op string) (float64, error) {
    switch op {
    case "+":
        return a + b, nil
    case "-":
        return a - b, nil
    case "*":
        return a * b, nil
    case "/":
        if b == 0 {
            return 0, fmt.Errorf("деление на ноль")
        }
        return a / b, nil
    default:
        return 0, fmt.Errorf("неизвестная операция: %s", op)
    }
}
