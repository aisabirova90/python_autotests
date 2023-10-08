import requests 
import pytest
token="e930d8e3a41f8d7cddeb6cb80a110251"


def test_status_code():
    response=requests.get(f'https://api.pokemonbattle.me:9104/trainers',params={'trainer_id':2466})
    assert response.status_code==200
  
def test_s():
    response=requests.get(f'https://api.pokemonbattle.me:9104/trainers',params={'trainer_id':2466})
    assert response.json()["trainer_name"]=="Noname"  