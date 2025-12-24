package log

import (
    "fmt"
    "os"
    "time"
)

// Logger структура для логирования
type Logger struct {
    filePath string
}

// NewLogger создаёт новый логгер
func NewLogger(filePath string) *Logger {
    return &Logger{filePath: filePath}
}

// Log записывает операцию в лог-файл
func (l *Logger) Log(operation string) {
    f, err := os.OpenFile(l.filePath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
    if err != nil {
        fmt.Println("Ошибка при открытии файла лога:", err)
        return
    }
    defer f.Close()

    logEntry := fmt.Sprintf("[%s] %s\n", time.Now().Format("2006-01-02 15:04:05"), operation)
    _, err = f.WriteString(logEntry)
    if err != nil {
        fmt.Println("Ошибка при записи в лог-файл:", err)
    }
}
