def sequencia_fibonacci(limit):
    sequencia = [0, 1]
    while sequencia[-1] < limit:
        next_value = sequencia[-1] + sequencia[-2]
        sequencia.append(next_value)
    return sequencia

def is_fibonacci(number):
    sequencia = sequencia_fibonacci(number)
    if number in sequencia:
        return f"O número {number} pertence à sequência de Fibonacci."
    else:
        return f"O número {number} NÃO pertence à sequência de Fibonacci."


num = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))
result = is_fibonacci(num)
print(result)
