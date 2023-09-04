# Objeto de primeira classe -> Em Python tudo é objeto, dessa forma funções também são objetos o que as tornam objetos de primeira classe. Com isso podemos atribuir funções a variáveis, passá-las como parâmetros para funções, usá-las como valores em estruturas de dados (listas, tuplas, dicionários e etc) e usar como valor de retorno para uma função (closures). 

def somar(a, b):
    return a + b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")

exibir_resultado(10, 10, somar)

# Perceba que não executamos a função abrindo e fechando parênteses (). 