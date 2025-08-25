from flask_babel import _

# Main function to calculate the BMI
def calculate_bmi(weight: float, height: float) -> float:
    return weight / (height ** 2)

# Function to comparate the result
def bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return _("Abaixo do peso")
    elif bmi < 25:
        return _("Peso normal")
    elif bmi < 30:
        return _("Sobrepeso")
    else:
        return _("Obesidade")