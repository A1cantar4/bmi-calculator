# Projeto Simples de uma Calculadora de IMC
# Variáveis: 'peso'(em Kg), 'altura'(em m), 'imc'(variável local),
# 'seu_imc'(Chama função do calculo), 'faixa'(Calcula a classificação)
# 'reiniciar'(Variável Opcional)
# Versão 1.2.0

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
        return "Cê cresceu demais pros lados, é bom dar um jeito nisso, pro seu próprio bem :D"
      # \('-')/ Havia me esquecido do 'Return' 
        
# Loop geral para que o usuário possa reiniciar quantas vezes desejar ao final do uso.
while True:
    # Vou adicionar um cabeçalho pra deixar mais bonitinho.
    print("¨¨¨¨ CALCULADORA IMC ¨¨¨¨")

    # Adicionado um Try/Except individual para evitar recomeçar sem armazenar informação do input anterior.
    # Loop 'Altura'
    while True:
        try:
            altura = float(input("Ei gigante! Me diz ai sua altura (m): \n"))
            break
        except ValueError:
            print("\nHmmm... Acho que cê digitou errado sua altura.\n")
    
    # Loop 'Peso'
    while True:
        try:
            peso = float(input("\nSó não vale mentir hein? Me diz ai seu peso atual (kg): \n"))
            break
        except ValueError:
            print("\nHmmm... Acho que cê digitou errado seu peso.\n")

    # Caso o loop dê certo, ai calcula e mostra o resultado do imc
    seu_imc = calculadora_imc(peso, altura)
    faixa = faixa_imc(seu_imc)

    print(f"\nMeu nobre, seu IMC é: {seu_imc:.2f}")
    print("Vejamos...", faixa)
    
    # Repetição opcional do usuário
    reiniciar = input("\nCamarada, quer calcular outro IMC (S/N)? ").strip().lower()
    if reiniciar != "s":
        print("\nTamo junto manin, até a próxima!")
        break