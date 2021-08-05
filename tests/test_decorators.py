from security.settings import MAX_COUNT

def test_security_many_requests(test_client, event_loop):
    for i in range(0, int(MAX_COUNT)):
        response = test_client.get('/many-requests')
        assert response.status_code == 200
        assert response.json()['ok'] is True

    for i in range(0, int(MAX_COUNT)):
        response = test_client.get('/many-requests')
        assert response.status_code == 200
        assert response.json()['ok'] is False
        assert response.json()['message'] == 'Las credenciales de autenticación no se proveyeron.'


def test_security_brute_force(test_client, event_loop):
    for i in range(0, int(MAX_COUNT)):
        response = test_client.get('/brute-force')
        assert response.status_code == 200
        assert response.json()['ok'] is True

    for i in range(0, int(MAX_COUNT)):
        response = test_client.get('/brute-force')
        assert response.status_code == 200
        assert response.json()['ok'] is False
        assert response.json()['message'] == 'invalid password'

