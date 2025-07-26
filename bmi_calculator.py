# Project: BodyMassIndex Calculator
# Versão 1.2.1

# Calculation basis
def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)    
    return bmi

# Rating weights
def bmi_range(bmi):
    if bmi < 18.5:
        return "Cê tá magrin de mais!"
    elif bmi < 25:
        return "Ó, ta bem alimentado viu?"
    elif bmi < 30:
        return "Vejamos... excedeu um pouco na hora de comer hein..."
    else:
        return "Cê cresceu demais pros lados, é bom dar um jeito nisso, pro seu próprio bem :D"
      # \('-')/ Havia me esquecido do 'Return' 
        
# Loop
while True:
    print("¨¨¨¨ CALCULADORA IMC ¨¨¨¨")

    # Try and Except for a clen loop
    # Wheight
    while True:
        try:
            height = float(input("Ei gigante! Me diz ai sua altura (m): \n"))
            break
        except ValueError:
            print("\nHmmm... Acho que cê digitou errado sua altura.\n")
    
    # Height
    while True:
        try:
            weight = float(input("\nSó não vale mentir hein? Me diz ai seu peso atual (kg): \n"))
            break
        except ValueError:
            print("\nHmmm... Acho que cê digitou errado seu peso.\n")

    # Calculation variables
    your_bmi = bmi_calculator(weight, height)
    bmi_range = bmi_range(your_bmi)

    print(f"\nMeu nobre, seu IMC é: {your_bmi:.2f}")
    print("Vejamos...", bmi_range)
    
    # Loop opcional
    restart = input("\nCamarada, quer calcular outro IMC (S/N)? ").strip().lower()
    if restart != "s":
        print("\nTamo junto manin, até a próxima!")
        break