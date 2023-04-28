# Telegram BotFather

Telegram automation.

## Add Bot in a TG Group

Here's how to add the bot you created to a Telegram group:

* Open Telegram and search for the specific group.
* Click on the group to open it.
* Click on the group's name at the top of the screen to open the Group Info page.
* Click on the "Add members" button.
* Search for your bot by its username (e.g., "@your_bot_username").
* Click on your bot's name to select it.
* Click on the "Add" button to add the bot to the group.

Once the bot is added to the group, you can send a message to the group with "@your_bot_username" (replace "your_bot_username" with the username you chose for your bot). This will allow the bot to retrieve the chat ID of the group, which you will need to use in your Python script.

## Bot Troubleshooting

### Cannot Add Bot to a Group

Provided that the specific Telegram does not banned any bot in it, follows these steps:

If you are getting an error message saying "could not add user" when trying to add your bot to the group, try the following steps:

* Make sure that you are entering the correct username for your bot (including the "@" symbol).
* Check if your bot is already a member of the group. If your bot is already in the group, you will not be able to add it again.
* Ensure that your bot has permission to join groups. You can check this in your bot's BotFather settings by selecting your bot, then selecting "Bot Settings" > "Group Privacy" > "Turn off".
* Make sure that the group is not full. Telegram groups have a limit on the number of members they can have, and if the group is already at capacity, you will not be able to add any more members.
* Try adding the bot to a different group to see if the issue persists. If you can add the bot to another group, then the issue may be specific to the group.

If none of these steps resolve the issue, you can try reaching out to Telegram support for further assistance.

### Cannot Find My Bot in the Group?

If you have added your bot to the group but cannot find it, make sure that you have followed the steps correctly:

* Search for the group in Telegram.
* Click on the group to open it.
* Click on the group's name at the top of the screen to open the Group Info page.
* Click on the "Add members" button.
* Search for your bot by its username (e.g., "@your_bot_username").
* Click on your bot's name to select it.
* Click on the "Add" button to add the bot to the group.

If you have completed these steps correctly and still cannot find your bot in the group, try the following:

* Make sure that your bot is not muted or blocked by any of the group members.
* Check the bot's permissions and make sure that it has the necessary permissions to send messages to the group.
* Restart the Telegram app or refresh the group page to see if the bot appears.

If you are still having trouble finding your bot in the group, you can try removing it from the group and adding it again, or contact Telegram support for further assistance.

## First Time Using Bot to Send Message in TG Group

To send a message to a Telegram group using your bot's username, you can use the following steps:

* Open the group in Telegram.
* Type "@" followed by your bot's username (e.g., "@your_bot_username") in the message box at the bottom of the screen.
* Type the message you want to send after your bot's username.
* Press Enter to send the message.

For example, if your bot's username is "@my_telegram_bot" and you want to send the message "Hello World" to the group, you would type:

```css
@my_telegram_bot !faucet 0x58e6f4ae9ea6e52a9baf08fee3cb031d54107080
```

Then, press Enter to send the message. Alternatively, you can create a file `MESSAGE_TEXT` via:

```bash
touch MESSAGE_TEXT
```

and store your message in this file. It can be called via `open` function in Python script. E.g.:

```python
with open('MESSAGE_TEXT', 'r') as f:
    MESSAGE = f.read().strip()
```

## Group Chat ID Determination

You can get the group chat ID manually by following these steps:

* Open Telegram on any device or platform (phone, desktop, web, etc.) that has access to the group you want to get the ID for.

* Open the group chat you want to get the ID for.

* Send any message in the group chat.

* Open your web browser and go to https://api.telegram.org/bot<your_bot_token_here>/getUpdates, replacing <your_bot_token_here> with your actual bot token.

* Look for the "chat" section in the JSON response. You should see an "id" field followed by a long number. This number is the chat ID of the group you just sent a message to.

Here's an example of what the JSON response might look like:

```json

{
    "ok": true,
    "result": [
        {
            "update_id": 123456789,
            "message": {
                "message_id": 1,
                "from": {
                    "id": 123456789,
                    "is_bot": false,
                    "first_name": "John",
                    "last_name": "Doe",
                    "language_code": "en"
                },
                "chat": {
                    "id": -123456789,
                    "title": "My Group",
                    "type": "group",
                    "all_members_are_administrators": true
                },
                "date": 1617944556,
                "text": "Hello, world!"
            }
        }
    ]
}
```

In this example, the chat ID of the group is -123456789. Note that the ID is a negative number for groups, so don't forget to include the minus sign in your code.
