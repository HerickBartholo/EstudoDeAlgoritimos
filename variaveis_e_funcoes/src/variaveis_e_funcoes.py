# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

if __name__ == "__main__":
    print("Hello World")


var_inteiro = 6
#print(type(var_inteiro))

var_string = 'texto'
#print(type(var_string))

var_float = 10.0
#print(type(var_float))


var_tupla_variaveis = (var_inteiro, var_float, var_string)
#print(type(var_tupla_variaveis))

var_lista_variaveis = [var_inteiro, var_float, var_string]

var_lista_variaveis += [123]

for valor in var_lista_variaveis:
    print(type(valor))
    
    