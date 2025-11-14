import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_Key = os.getenv('LLM_API_LEY')
Model = os.getenv('GROQ_MODEL')
GROQ_API_URL = os.getenv('GROQ_URL') 

def call_llm_api(prompt):
    headers={
        "Authorization": f'Bearer {GROQ_API_Key}',
        "Content-Type": "application/json",
    }
    data = {
         "model": Model,
         "input": prompt
    }

    try:
        response = requests.post(GROQ_API_URL, json=data, headers=headers)
        if response.status_code == 200:
            response_data = response.json()
            if "output" in response_data:
                    return response_data["output"][1]['content'][0]['text']
            
        else:
            return response.text
    
    except Exception as e:
        return f'Error: {str(e)}'


if __name__ == '__main__':
    prompt = input("Enter prompt input :")
    result = call_llm_api(prompt)
    if result:
        print(result)
    else:
        print("Failed to get response")