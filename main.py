import requests 
token="e930d8e3a41f8d7cddeb6cb80a110251"

'''response = requests.post('https://api.pokemonbattle.me:9104/trainers/reg', json={
    "trainer_token": token,
    "email": "sabirovaar3011@yandex.ru",
    "password": "Iloveqa1"
}, headers = {"Content-Type":"application/json"}) 
print(response.text)'''

'''response_activation = requests.post('https://api.pokemonbattle.me:9104/trainers/confirm_email', json={
    "trainer_token": token
}, headers = {"Content-Type":"application/json"}) 
print(response_activation.text)'''

'''response_pokemons = requests.post('https://api.pokemonbattle.me:9104/pokemons', json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {"Content-Type":"application/json","trainer_token":token}) 
print(response_pokemons.text)'''

'''response_change = requests.put('https://api.pokemonbattle.me:9104/pokemons', 
                               json={
    "pokemon_id": "11952",
    "name": "New Name",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {"Content-Type":"application/json","trainer_token":token}) 
print(response_change.text)'''

response_pokebal= requests.post('https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                               json={
    "pokemon_id": "11952",
}, headers = {"Content-Type":"application/json","trainer_token":token}) 
print(response_pokebal.text)