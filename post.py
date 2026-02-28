import os
import requests

SLACK_BOT_TOKEN = os.environ["SLACK_BOT_TOKEN"]
CHANNEL_ID = os.environ["SLACK_CHANNEL_ID"]
MESSAGE = os.environ["BUILDING_INFO_MESSAGE"]

def main():
    url = "https://slack.com/api/chat.postMessage"
    headers = {
        "Authorization": f"Bearer {SLACK_BOT_TOKEN}",
        "Content-Type": "application/json; charset=utf-8",
    }
    payload = {
        "channel": CHANNEL_ID,
        "text": MESSAGE,
    }

    r = requests.post(url, headers=headers, json=payload, timeout=20)
    data = r.json()

    if not data.get("ok"):
        raise SystemExit(f"Slack API error: {data}")

if __name__ == "__main__":
    main()
