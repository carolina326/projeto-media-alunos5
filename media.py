# Função para calcular a média dos alunos
def calcular_media():
    # Receber as notas do aluno
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))
    
     # Calcular a média aritmética
    media = (nota1 + nota2 + nota3) / 3
    
    # Exibir a média
    print(f"A média das notas é: {media:.2f}")
    
    # Verificar aprovação
    if media >= 6:
        print("Aprovado")
    elif media >= 5.0:
        print("Recuperação")
    else:
        print("Reprovado")

if __name__ == "__main__":
    calcular_media()