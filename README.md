# Zhina-Life

This project provides a Telegram bot for anonymous medical conversations between patients and doctors. The bot uses end-to-end encryption to ensure the privacy and security of the conversations, and provides a secure PDF containing the conversation history to the patient at the end of each conversation.

## Requirements

- Python 3.6 or later
- The `python-telegram-bot` library
- The `pdfkit` library

## Setup

1.  Install the required dependencies by running `pip install -r requirements.txt`.
2.  Replace `<BOT_TOKEN>` in the `bot.py` file with your bot's token.
3.  Replace `<DOCTOR_ID>` in the `bot.py` file with the ID of the doctor who will be using the bot.
4.  Run the `bot.py` script to start the bot.

## Usage

- Patients can use the bot to send messages and files to the doctor anonymously.
- The doctor can use the website to receive and reply to messages and files from the patients.
- At the end of each conversation, the bot sends a secure PDF containing the conversation history to the patient.

## Security Features

- End-to-end encryption: The bot uses end-to-end encryption to ensure the privacy and security of the conversations between the patients and the doctors.
- Secure PDF: The bot creates a secure PDF containing the conversation history at the end of each conversation, and sends the PDF to the patient using end-to-end encryption. The PDF cannot be modified and can only be sent to the bot using the Telegram bot.
- No patient information saved: The website does not save any patient information, and all patient data is deleted after each conversation.

## Technical Details

- The bot is implemented in Python using the `python-telegram-bot` library.
- The bot uses the Telegram bot API to communicate with the patients and doctors.
- The website uses an API to connect to the bot and receive messages and files from the patients.
- The website uses a chat-like interface to display the conversation between the patients and the doctors.
- The PDF is created using the `pdfkit` library, and is sent to the patient using the Telegram bot API.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
