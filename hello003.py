"""
Programa Hello
Descrição: imprima na tela a frase ”Hello, World!”
Autor: Natane Fraga Lopes
Data: 27/02/2025
Versão: 0.0.3
Novidades da versão:

27/02/2025
Nesta versão, o usuário poderá entrar com seu nome para ser cumprimentando pelo programa.
"""

# Alocação de memória

#frase = "Hello, World!"

nome_usuario = ""
frase = "Hello, "

# Entrada de dados

nome_usuario = input("Qual o seu nome? ")

# Processamento de dados

frase = frase + nome_usuario

# Saída de dados

print(frase)