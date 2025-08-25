def test_index_in_english(client):
    response = client.get("/?lang=en")
    assert b"BMI Calculator" in response.data

def test_index_in_spanish(client):
    response = client.get("/?lang=es")
    assert b"Calculadora de IMC" in response.data or b"Resultado" in response.data

def test_index_in_french(client):
    response = client.get("/?lang=fr")
    assert b"Calculateur IMC" in response.data