"""
Programa Hello
Descrição: imprima na tela a frase ”Hello, World!”
Autor: Natane Fraga Lopes
Data: 27/02/2025
Versão: 0.0.4
Novidades da versão:

27/02/2025
1. Nesta versão, o usuário poderá entrar com seu nome para ser cumprimentando pelo programa.
2. Utilizamos f-strings para escrever um código mais limpo.
"""

# Alocação de memória

nome_usuario = ""
frase = ""

# Entrada de dados

nome_usuario = input("Qual o seu nome: ")

# Processamento de dados

frase = f"Hello, {nome_usuario}"

# Saída de dados

print(frase)