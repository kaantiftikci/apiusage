pip install pandas requests

import pandas as pd
import requests


deepl_api_key = 'cae20839-82b8-4ab6-96b7-df5084a2b4bf:fx'

df = pd.read_excel('/content/3501-5801.xlsx')


def translate_text(text, target_lang='EN'):
    url = 'https://api-free.deepl.com/v2/translate'
    params = {
        'auth_key': deepl_api_key,
        'text': text,
        'target_lang': target_lang
    }
    response = requests.post(url, data=params)
    if response.status_code == 200:
        return response.json()['translations'][0]['text']
    else:
        return None

df['Translated_Review'] = df['review'].apply(lambda x: translate_text(x))

df.to_excel('translated_reviews_3501-5801.xlsx', index=False)

