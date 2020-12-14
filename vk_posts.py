import json
import requests
import pandas as pd


# token dfc0b7cfe69b3e3aca95d9023bd62ef98567222590efcb9c185c0448dd1d45a22f221b6d7385dde6a3382

# https://oauth.vk.com/authorize?client_id=7625987&scope=notify,photos,friends,audio,video,notes,pages,docs,status,questions,offers,wall,groups,messages,notifications,stats,ads,offline&redirect_uri=http://api.vk.com/blank.html&display=page&response_type=token

def posts(user_id, temp):
    token = 'a1fbf936a1fbf936a1fbf9368ca18f8776aa1fba1fbf936fe4ab01cb3a2484568eeabd6'
    v = 5.92
    response = requests.get('https://api.vk.com/method/wall.get',
                            params={
                                'access_token': token,
                                'v': v,
                                'owner_id': user_id,
                                'count': temp,

                            }
                            )

    tablica: dict = {
        "id": [],
        "text": [],
        "copy_text": []
    }

    data = response.json()
    for x in data['response']['items']:
        id = '--'
        text = '--'
        cp_text = '--'

        if x['text']:
            text = x['text']
        try:
            if x['copy_history']:
                id = x['copy_history'][0]['from_id']
                if x['copy_history'][0]['text']:
                    cp_text = x['copy_history'][0]['text']
        except KeyError:
            pass

        tablica['id'].append(id)
        tablica['text'].append(text)
        tablica['copy_text'].append(cp_text)

    a = pd.DataFrame.from_dict(tablica)
    return a


result = posts(248781023, 30)
print(result)

result.to_excel('posts.xlsx')

