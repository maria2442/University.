import json
import requests
import pandas as pd

def FF(user_id):
    token = ''
    v = 5.92

    response = requests.get('https://api.vk.com/method/friends.get',
                            params={
                                'access_token': token,
                                'v': v,
                                'user_id': user_id,
                                'fields': 'online'
                            }
                            )

    data = response.json()
    with open('Key.json', 'w') as fl:
        json.dump(data, fl)

def FG(user_id):
    token = ''
    v = 5.92
    global j
    a='description,activity'
    response = requests.get('https://api.vk.com/method/groups.get',
                            params={
                                'access_token': token,
                                'v': v,
                                'user_id': user_id,
                                'extended': 1,
                                'fields': a
                            }
                            )
    data = response.json()
    with open("qwerty.json", 'w') as fl:
        json.dump(data, fl)
    try:
        l = data['response']['count']

        for i in range(0, l - 1):
            w = data['response']['items'][i]['name']
            j.loc[i] = [w, '', '']
            try:
                t = data['response']['items'][i]['activity']
                j.activity[i] =[t]
            except Exception as err:
                print("-")
            print(i)

            try:
                q = data['response']['items'][i]['description']
                j.description[i] =[q]
            except Exception as err:
                print("-")
    except KeyError:
        print("-")
    except IndexError:
        print("+")

def poi(id1):
    global asd
    FG(id1)
    asd = pd.concat([asd, j])
    print(asd.shape)

def om(id):
    FF(id)
    global q
    file = open('Key.json','r')
    text = file.read()
    text = json.loads(text)
    df=text
    l=df['response']['count']
    l=l-1
    q=[]
    for i in range(0,l):
        m=df['response']['items'][i]["id"]
        try:
            k = df['response']['items'][i]['is_closed']
            if(k==False):
                q.append(m)
        except KeyError:
            k='no information'
        print(m,k)
        poi(id)
        print(q)
    for i in q:

        poi(i)

j = pd.DataFrame({"name": [],
                  "description":[],
                  "activity": []
                  })
asd = pd.DataFrame({"name": [],
                  "description":[],
                  "activity": []
                  })



om(557520569)


asd.to_excel('123.xlsx',index=False)

