# To create a Python script that can post text messages to a Telegram group, you will need to use the Telegram Bot API.
# Here are the steps to create a bot and a Python script:

# Open Telegram and search for the "BotFather" account.
# Send a message to BotFather with the "/newbot" command to create a new bot.
# Follow the prompts to name your bot and choose a username.
# Once you've created the bot, BotFather will give you a token. Save this token somewhere safe, as you will need it to authenticate your bot in the Python script.

# Here is a sample script that will post the message:
# "!faucet your_haqq_public_address_here" to the "HAQQ Network // TE2 Faucet" group every 1 hour and 15 minutes:

# Replace "your_bot_token_here" with the token you received from BotFather, and "your_group_chat_id_here" with the ID of the "HAQQ Network // TE2 Faucet" group,
#  (you can find this ID by adding the bot to the group and sending a message to the group; the bot will then be able to retrieve the group ID).

# Replace your haqq_public_address_here with your actual public address.

# Save the script as a Python file (e.g., "telegram_bot.py") and run it from the command line using the "python" command:
# python telegram_bot.py

# The script will run indefinitely, posting the message to the group every 1 hour and 15 minutes. You can stop the script at any time by pressing "Ctrl+C".

import time
import requests

# TOKEN = "your_bot_token_here"
# CHAT_ID = "your_group_chat_id_here"
# MESSAGE = "!faucet haqq_public_address_here"

# Create 3 files via touch BOT_TOKEN GROUP_CHAT_ID MESSAGE_TEXT and populate them accordingly.
# Declare these 3 files in .gitignore to avoid pushing your sensitive information.
with open('BOT_TOKEN', 'r') as f:
    TOKEN = f.read().strip()

with open('GROUP_CHAT_ID', 'r') as f:
    CHAT_ID = f.read().strip()

with open('MESSAGE_TEXT', 'r') as f:
    MESSAGE = f.read().strip()


def send_message(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    params = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, params=params)

while True:
    send_message(MESSAGE)
    time.sleep(60*75)  # sleep for 1 hour and 15 minutes
