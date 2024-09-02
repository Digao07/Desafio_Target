def count_a_in_string(input_string):
    input_string_lower = input_string.lower()
    count = input_string_lower.count('a')
    
    if count > 0:
        return f"A letra 'a' aparece {count} vezes na string."
    else:
        return "A letra 'a' não aparece na string."


string = input("Informe uma string: ")
result = count_a_in_string(string)
print(result)
