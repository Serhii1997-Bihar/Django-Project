import requests

refresh_url = 'http://127.0.0.1:8000/api/token/refresh/'
refresh_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczMTc0Mjc4MywiaWF0IjoxNzMxNjU2MzgzLCJqdGkiOiI1ZDlhYmE4OTg3NDk0N2E5ODI2OGU5NTgzMzlkNzliZSIsInVzZXJfaWQiOjM5fQ.rP_LREpof-zs2DqZ7MqrDgGODV0uswaXUMrBAAjipyY"
response = requests.post(refresh_url, data={'refresh': refresh_token})

if response.status_code == 200:
    new_access_token = response.json()['access']
    products_url = 'http://127.0.0.1:8000/api/products/'
    headers = {'Authorization': f'Bearer {new_access_token}'}
    products_response = requests.get(products_url, headers=headers)

    if products_response.status_code == 200:
        print("Products:", products_response.json())
    else:
        print("Error:", products_response.status_code, products_response.text)
else:
    print("Error refreshing token:", response.status_code, response.text)

