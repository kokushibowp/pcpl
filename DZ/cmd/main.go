package main

import (
    "fmt"

    "DZ/calculator"
    mylog "DZ/log"
)

func main() {
    logger := mylog.NewLogger("calculator.log")

    for {
        fmt.Print("Введите операцию (например, 5 + 3) или 'quit' для выхода: ")
        var a float64
        var op string
        var b float64

        _, err := fmt.Scanf("%f %s %f\n", &a, &op, &b)
        if err != nil {
            fmt.Println("Ошибка ввода. Попробуйте снова.")
            continue
        }

        result, err := calculator.Calculate(a, b, op)
        if err != nil {
            fmt.Println("Ошибка:", err)
            continue
        }

        operation := fmt.Sprintf("%f %s %f = %f", a, op, b, result)
        fmt.Println(operation)
        logger.Log(operation)

        if op == "quit" {
            break
        }
    }
    fmt.Println("Программа завершена.")
}
