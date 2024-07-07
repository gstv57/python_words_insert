import requests

def insert_using_api(word_original):
    try:
        headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'User-Agent': 'insomnia/9.2.0',
        }

        json_data = {
            'word_original': f'{word_original}',
            'target_language': 'pt-BR',
        }

        response = requests.post('http://127.0.0.1:8000/api/words', headers=headers, json=json_data)

        if(response.status_code == 200):
            print('Word inserted successfully: ' + word_original)
        else:
            print('Error: ' + response.text)

    except Exception as e:
        print(e)

try:
    with open('words.txt', 'r') as file:
        words = file.readlines()
        for word in words:
            insert_using_api(word.strip()) 
            
except Exception as e:
    print(e)