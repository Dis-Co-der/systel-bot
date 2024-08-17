# Systel-Bot

**Systel-Bot** is a Python-based Telegram bot designed to monitor and report system performance metrics. The bot tracks CPU usage, RAM usage, and GPU metrics such as temperature, power usage, and memory usage, sending updates via Telegram at regular intervals.

## Features

- **CPU Monitoring**: Tracks and reports CPU usage percentage.
- **RAM Monitoring**: Monitors used and total RAM.
- **GPU Monitoring**: Reports GPU load, temperature, power usage, and memory usage.
- **Telegram Notifications**: Sends regular updates to a specified Telegram chat.

## Installation

To get started, clone the repository and install the dependencies:

git clone https://github.com/Dis-Co-der/systel-bot.git
cd systel-bot
pip install .

In the '.env' file in the root directory and add your Telegram bot token and chat_id from telegram in the '':

BOT_KEY='your_bot_key'
CHAT_ID='your_chatid'

After setting up, you can start the bot by running:

python3 bot.py


Project Structure:

.
├── bot.py           # Main script for monitoring and sending updates
├── requirements.txt     # List of dependencies
├── setup.py             # setup
├── pyproject.toml       # Project configuration file
├── README.md            # Project documentation
├── LICENSE.txt          # LICENSE File  
└── .env                 # Environment variables

Contributing
If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcome.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any inquiries or support, please reach out to Dan Lappisto at https://github.com/Dis-Co-der.