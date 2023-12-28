
def test_register(client):


    #Create a fake user for test
    fake_user = {
        'username' : 'test_user',
        'email' : 'test@example.com',
        'password' : 'test_password',
        'confirm_password' : 'test_password',
    }
    # Simulate a registration request
    response = client.post('/signup',data = fake_user)

    # Check if the registration was successful
    assert response.status_code == 200 # Assuming a successful registrarion redirects to another page
    assert b'Congratulations, you are now registered user!' in response.data

