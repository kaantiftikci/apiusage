pip install pandas requests

import pandas as pd
import requests


deepl_api_key = 'DEEPL API KEY'

df = pd.read_excel('file patch')


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

df.to_excel('file_name.xlsx', index=False)

