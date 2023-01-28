from . models import AUM
import requests


def get_ultra_user_curr_val():
    url = 'http://192.168.100.54:8888/ords/BPT/uc_client_val/current_value'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if AUM.objects.filter(user_id=data['id'],period=data['period']).exists():
            AUM.objects.filter(user_id=data['id'],period=data['period']).update(value=data['value_as_at'])
            print ('updated')
        else:
            AUM.objects.create(user_id=data['id'],period=data['period'], value=data['value_as_at'])
            print('Created')
