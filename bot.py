import os
import logging
from io import BytesIO
from telethon.tl.types import InputPeerUser
from pdfkit import PDFDocument
from telegram.ext import Updater, MessageHandler, CommandHandler
import flask
import requests
import json

# Set the bot token and the doctor ID
BOT_TOKEN = "<BOT_TOKEN>"
DOCTOR_ID = "<DOCTOR_ID>"

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)
logger = logging.getLogger(__name__)

# Define the updater, which connects to the Telegram API and receives updates
updater = Updater(token=BOT_TOKEN, use_context=True)

# Define the dispatcher, which dispatches messages to the appropriate handlers
dispatcher = updater.dispatcher

# Handle incoming messages and files from the website


def handle_message(update, context):
    # Forward the message and file to the doctor
    context.bot.send_message(DOCTOR_ID, update.message.text, encrypt=True)
    if update.message.document:
        context.bot.send_document(
            DOCTOR_ID, update.message.document.file_id, encrypt=True)

# Handle the "/end" command, which ends the conversation and sends the PDF to the patient


def handle_end(update, context):
    chat_id = update.effective_chat.id

    # Create the PDF
    doc = PDFDocument()
    doc.pipe(BytesIO())

    # Add the chat history to the PDF
    history = context.bot.get_history(chat_id, 0, 0, 100, encrypt=True)
    for message in history.messages:
        doc.text(message.text)
        if message.document:
            doc.image(message.document.file_id, 0, 0, fit=[100, 100])
    doc.end()

# Handle the "/end" command, which ends the conversation and sends the PDF to the patient


def handle_end(update, context):
    chat_id = update.effective_chat.id

    # Create the PDF
    doc = PDFDocument()
    stream = BytesIO()
    doc.pipe(stream)

    # Add the chat history to the PDF
    history = context.bot.get_history(chat_id, 0, 0, 100, encrypt=True)
    for message in history.messages:
        doc.text(message.text)
        if message.document:
            doc.image(message.document.file_id, 0, 0, fit=[100, 100])
    doc.end()

    # Send the PDF to the patient
    try:
        context.bot.send_document(chat_id, doc.output, encrypt=True,
                                  caption='Here is a secure PDF containing the conversation history.')
    except Exception as e:
        logger.error("An error occurred: %s" % e)

    # Close the stream and free up the memory
    stream.close()

# Handle the "/start" and "/help" commands, which provide instructions to the user


def handle_start_help(update, context):
    chat_id = update.effective_chat.id
    message = update.effective_message

    if message.text == "/start":
        text = "Hi, I'm a medical bot. You can use me to anonymously talk to a doctor. To start a conversation, just send me a message. To end the conversation, use the /end command. To get help, use the /help command."
    elif message.text == "/help":
        text = "Here are the available commands:\n\n/start - Start a conversation with a doctor\n/end - End the conversation and receive a secure PDF with the conversation history\n/help - Get help and information on the available commands"

    context.bot.send_message(chat_id, text, encrypt=True)


# Set up the bot and register the functions as handlers
updater = Updater(token="<BOT_TOKEN>", use_context=True)
dispatcher = updater.dispatcher

end_handler = CommandHandler("end", handle_end)
dispatcher.add_handler(end_handler)

start_help_handler = CommandHandler(["start", "help"], handle_start_help)
dispatcher.add_handler(start_help_handler)

# Start the bot
updater.start_polling()
