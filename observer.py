import os
import time

import requests
import schedule
from discord_webhook import DiscordWebhook
from dotenv import load_dotenv

load_dotenv()  # Load .env


def check_api_status(api_url, api_name, discord_webhook_url):
    try:
        res = requests.head(api_url)
        is_success = res.status_code in [200, 204]
        if is_success:
            message = f"🌟 {api_name} server is running."
        else:
            message = f"🙊 {api_name} server is not running.\n{api_url}\nStatus code: {res.status_code}\nError : {res.text}"
    except:
        is_success = False
        message = f"🔥 {api_name} server is not running.\n{api_url}"

    print(message)
    if not is_success:
        send_discord_webhook(discord_webhook_url, message)


def send_discord_webhook(webhook_url, message):
    webhook = DiscordWebhook(url=webhook_url, content=message)
    webhook.execute()


if __name__ == '__main__':
    # Import API Server URL list from .env file
    api_urls = os.getenv("API_URLS").split(",")
    api_names = os.getenv("API_NAMES").split(",")
    discord_webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if len(api_urls) == 0 or len(api_names) == 0:
        print("Please enter API_URLS or API_NAMES in your .env file (separated by commas)")
        exit()
    elif len(api_urls) != len(api_names):
        print("Enter the same number of API_URLS and API_NAMES in the .env file.")
        exit()

    # Run the work on schedule cycle
    for api_url, api_name in zip(api_urls, api_names):
        schedule.every(5).minutes.do(
            check_api_status,
            api_url=api_url,
            api_name=api_name,
            discord_webhook_url=discord_webhook_url
        )

    # In the first one -time execution
    for api_url, api_name in zip(api_urls, api_names):
        check_api_status(
            api_url=api_url,
            api_name=api_name,
            discord_webhook_url=discord_webhook_url
        )
    send_discord_webhook(
        discord_webhook_url,
        '🚀 Observer is running\n- ' + '\n- '.join(api_names)
    )

    while True:
        schedule.run_pending()
        time.sleep(1)
