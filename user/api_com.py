from django.contrib.auth.models import User
from . models import Profile, ClientAUM
from dashboard.models import AUM, all_scheme
import requests


def get_ultra_user():
    url = 'http://192.168.100.54:8888/ords/BPT/testuser/usertest'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if User.objects.filter(username=data['accountno']).exists():
            User.objects.filter(username=data['accountno']).update(
                last_name=data['surname'], first_name=data['first_name'], email=data['email'])
            print('updated')
        else:
            User.objects.create(username=data['accountno'], last_name=data['surname'],
                                first_name=data['first_name'], email=data['email'])
            print('Created')


def get_ultra_profile():
    url = 'http://192.168.100.54:8888/ords/BPT/userprofile/profile'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if Profile.objects.filter(user=data['ultra_conetid']).exists():
            Profile.objects.filter(user=data['ultra_conetid']).update(dob=data['dob'], age=data['age'], gender=data['gender'],
                                                                      country=data['nationality'], country_of_birth=data['country_of_birth'],
                                                                      place_of_birth=data['place_of_birth'], phone=data[
                                                                          'phone'], alt_phone=data['alternative_phone'],
                                                                      dig_address=data['digital_address'], postal_address=data[
                                                                          'postal_address'], res_address=data['residential_address'],
                                                                      ssnit=data['ssnit'], national_id=data['id_no'], nok=data[
                                                                          'next_of_kin'], nok_address=data['nok_address'], nok_rel=data['nok_relationship'],
                                                                      nok_phone=data['next_of_kin_tel'], father_name=data['name_of_father'], father_address=data['fathers_address'], mother_name=data['name_of_mother'], mother_address=data['mothers_address'])
            print('updated')
        else:
            print('no existing user found')

    
def all_scheme_aum():
    url = 'http://192.168.100.54:8888/ords/BPT/ultraconet/aum'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if AUM.objects.filter(user=data['id'], period=data['period']).exists():
            AUM.objects.filter(user=data['id'], period=data['period']).update(period=data['period'], value=data['value_as_at'])
            print('updated')
        else:
            AUM.objects.create(user_id=data['id'], period=data['period'], value=data['value_as_at'])
            print('lets create them')


def client_bal():
    url = 'http://192.168.100.54:8888/ords/BPT/ultraconet/client_balance'
    res = requests.get(url)
    data = res.json()['items']
    for data in data:
        if all_scheme.objects.filter(user=data['id']).exists():
            all_scheme.objects.filter(user=data['id']).update(contribution=data['contribution'], interest=data['returns'], withdrawal=data['claims'], balance=data['value'], last_cont_date=data['last_cont_date'])
            print('updated')
        else:

            print('lets create them')
