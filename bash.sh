#!/bin/bash

echo "Чтобы начать деанон Алексея, введите 1"
read input

if [ "$input" == "1" ]; then
    echo "Начинаю процесс..."
    for i in {1..100}
    do
        echo "Осталось: $((100-i))%"
        sleep 0.1
    done
    echo "Деанон и сват сделан успешно 😈😈😈"
else
    echo "Неверный ввод. Попробуйте снова."
fi
