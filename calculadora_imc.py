# Projeto Simples de uma Calculadora de IMC
# Variáveis: peso (em Kg), altura(em m), imc(variável local),
# seu_imc(Chama função do calculo), faixa(Calcula a classificação)
# Versão 1.0.0

# Definindo base de calculo da calculadora
def calculadora_imc(peso, altura):
    imc = peso / (altura ** 2)    
    return imc

# Definindo a classificação dos pesos
def faixa_imc(imc):
    if imc < 18.5:
        return "Cê tá magrin de mais!"
    elif imc < 25:
        return "Ó, ta bem alimentado viu?"
    elif imc < 30:
        return "Vejamos... excedeu um pouco na hora de comer hein..."
    else:
        "Cê cresceu demais pros lados, é bom dar um jeito nisso, pro seu próprio bem :D"
        
# Início do programa em si com inputs, mas pode ser carregado de outro arquivo (só importar)
# Vou adicionar um cabeçalho pra deixar mais bonitinho.
print("¨¨¨¨ CALCULADORA IMC ¨¨¨¨")
altura = float(input("Ei gigante! Me diz ai sua altura (m): "))
peso = float(input("Só não vale mentir hein? Me diz ai seu peso atual (kg): "))

seu_imc = calculadora_imc(peso, altura)
faixa = faixa_imc(seu_imc)

print(f"Meu nobre, seu IMC é: {seu_imc:.2f}")
print("Vejamos...", faixa)