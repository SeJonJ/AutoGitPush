import os
import requests
from dotenv import load_dotenv

# .env 파일을 로드
load_dotenv()

## slack api url
url = "https://slack.com/api/chat.postMessage"

def sendSlackMsg(news_data):
    headers = {
    "Authorization": "Bearer "+os.getenv('SLACK_TOKEN'), ## slack token => .env 파일에서 가져온다
    "Content-Type": "application/json"
    }

    payload = {
        "channel": 'it-news',
        "text": "새로운 뉴스가 도착했습니다 \n\n"+news_data
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Failed to send message")
