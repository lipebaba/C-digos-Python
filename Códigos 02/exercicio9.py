def inverter_string(s):
    return s[::-1]  

string_usuario = input("Digite uma string para inverter: ")

string_invertida = inverter_string(string_usuario)
print(f"A string invertida é: {string_invertida}")
