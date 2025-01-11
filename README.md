# Telegram Chat ID Finder Bot

A simple Python bot that retrieves the chat ID of a Telegram user or group, useful for setting up bots and integrations that require chat IDs.

## Features

- Fetches the chat ID from user or group interactions with the bot.
- Useful for developers needing Telegram chat IDs for bot setups or other integrations.

## Installation and Setup

### Prerequisites

- **Python 3.x** installed on your machine.
- A **Telegram Bot API Token**.

### Installation

1. **Clone or Download** this repository:
   ```bash
   git clone https://github.com/EnesKeremAYDIN/telegram-chat-id.git
   cd telegram-chat-id
   ```

2. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Set Up Environment Variables**:
   - Open the `.env` file and add your **Telegram Bot API Token**.

### Running the Bot

Run the bot to retrieve chat IDs:
```bash
python bot.py
```

## Files

- **`bot.py`**: Main script to fetch chat IDs from Telegram interactions.
- **`.env`**: Stores configuration values securely, including the Telegram Bot API Token.

## Disclaimer

This tool is intended for personal or development use to aid in obtaining chat IDs. Ensure compliance with Telegram's terms of service.
