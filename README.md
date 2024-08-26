# Systel-Bot

**Systel-Bot** is a Python-based Telegram bot designed to monitor and report system performance metrics. The bot tracks CPU usage, RAM usage, and GPU metrics such as temperature, power usage, and memory usage, sending updates via Telegram at regular intervals.

## Features

- **CPU Monitoring**: Tracks and reports CPU usage percentage.
- **RAM Monitoring**: Monitors used and total RAM.
- **GPU Monitoring**: Reports GPU load, temperature, power usage, and memory usage.
- **Telegram Notifications**: Sends regular updates to a specified Telegram chat.

## Installation

To get started, clone the repository and install the dependencies:

**git clone https://github.com/PSYGNEX/systel-bot.git
cd systel-bot
pip install .**

In the '.env' file in the root directory (.venv) and add your Telegram bot token and chat_id from telegram in the '':

**BOT_KEY='your_bot_key'
CHAT_ID='your_chatid'**

**Or you could hard code it too in the bot.py, your choice**

After setting up, you can start the bot by running:

**python3 bot.py**

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or support, please reach out to Dan Lappisto at https://github.com/PSYGNEX.
