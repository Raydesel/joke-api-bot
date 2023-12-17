# Getting ready

First, create a new bot for Telegram. This is done through the channel here: https://telegram.me/botfather. Access it through your Telegram account.

Run `/start` to start the interface and then create a new bot with `/newbot`. 

Once it's set up, it will give you the following:
• The Telegram channel of your bot: *https:/t.me/<yourusername>.*
• A **TOKEN** to allow access to the bot. Copy it as it will be used later.

Next, install the Python module `telepot`, which wraps the RESTful interface from Telegram:

```bash
pip install telepot
```

Set up your generated token in the `joke_api_bot.py` script on the **TOKEN**
constant in line 27:

```bash
TOKEN = '<YOUR TOKEN>'
```

Start the bot:

```bash
python joke_api_bot.py
```

Open the Telegram channel on your phone using the URL and start it.

You can select from the following joke types: 'programming', 'christmas', 'misc', 'dark', 'pun', 'spooky'

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/4f32b134-ffb9-4a24-a457-4694df4e7f6a/d1e2ea69-686e-41de-97fa-8b97440ba257/Untitled.png)

More about the API of Telegram: https://core.telegram.org/bots/api
