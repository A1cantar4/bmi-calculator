def test_index_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"IMC" in response.data

def test_post_valid_data(client):
    response = client.post("/", data={"height": "1.75", "weight": "70"})
    assert response.status_code == 200
    assert b"IMC" in response.data
    assert b"22" in response.data

def test_post_invalid_data(client):
    response = client.post("/", data={"height": "abc", "weight": "70"})
    assert response.status_code == 200
    assert b"Entrada" in response.data