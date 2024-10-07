
# Ethereum Seed Phrase Checker

This Python script checks Ethereum seed phrases for their associated balances. If an account associated with a seed phrase has a balance greater than 0.01 ETH, it records the details and sends a notification to a specified Telegram bot. The script can generate seed phrases or read them from a file.

## Features

- Generates random Ethereum seed phrases or checks a list from a `.txt` file.
- Sends notifications to a Telegram bot when a seed phrase has a balance above 0.01 ETH.
- Records seed phrases with balances in a text file.
- Supports multithreading for faster checking.

## Prerequisites

- Python 3.x
- Required libraries:
  - `requests`
  - `web3`
  - `eth-account`
  - `colorama`

You can install the required libraries using pip:

```bash
pip install requests web3 eth-account colorama
```

## Setup

1. **Telegram Bot Token and Chat ID**: 
   - Replace `"tg bot token"` with your Telegram bot token.
   - Replace `"your id"` with your Telegram chat ID in the `snd2tg` function.

2. **Infura URL**: 
   - The script uses the Infura mainnet URL. Make sure the URL is correct and your Infura project is set up properly.

## Usage

1. **Run the script**:
   ```bash
   python seed_phrase_checker.py
   ```

2. **Choose an option**:
   - Press `1` to generate and check random seed phrases.
   - Press `2` to check seed phrases from a file.

3. **Input the required information**:
   - For option 1, specify the number of threads to use.
   - For option 2, provide the path to the `.txt` file containing seed phrases and specify the number of threads.

## Safety Note

This script interacts with Ethereum addresses and private keys. Please be cautious when handling seed phrases and private keys. Using this script with real seed phrases or private keys can result in the loss of funds. It is recommended to test with dummy seed phrases and ensure that you understand the script's functionality before using it with actual wallets.

## License

