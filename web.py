# Website and API code

# Import the necessary libraries
import flask
import requests
import json
from flask import Flask, request
import requests
import pdfkit
import telethon
from telethon import events, errors
from telethon.tl.types import InputPeerUser

# Replace <BOT_TOKEN> with your bot's token
BOT_TOKEN = "<BOT_TOKEN>"

# Create the Flask app
app = Flask(__name__)

# Handle incoming messages and files from the Telegram bot


@app.route('/', methods=['POST'])
def handle_message():
    # Forward the message and file to the doctor
    session = telethon.TelegramClient('session', api_id, api_hash)
    session.start()
    doctor = session.get_input_entity(InputPeerUser( < DOCTOR_ID > ))
    session.send_message(doctor, request.form["message"], encrypt=True)
    if "file" in request.files:
        session.send_file(doctor, request.files["file"], encrypt=True)


# Handle the "/end" command, which ends the conversation and sends the PDF to the patient


@app.route('/end', methods=['POST'])
def handle_end():
    chat_id = request.form["chat_id"]

    # Create the PDF and send it to the patient
    try:
        # Create the PDF
        doc = pdfkit.PDFDocument()
        doc.pipe(open('conversation.pdf', 'wb'))

        # Add the chat history to the PDF
        history = requests.get("https://api.telegram.org/bot" + BOT_TOKEN +
                               "/getHistory?chat_id=" + chat_id + "&offset=0&limit=100", encrypt=True)
        for message in history.messages:
            doc.text(message.text)
            if message.document:
                doc.image(message.document.file_id, 0, 0, fit=[100, 100])
        doc.end()

        # Send the PDF to the patient
        patient = session.get_input_entity(InputPeerUser(chat_id))
        session.send_file(patient, open('conversation.pdf', 'rb'), encrypt=True,
                          caption='Here is a secure PDF containing the conversation history.')

        # Return a success message
        return "PDF sent successfully"
    except Exception as e:
        # Return an error message
        return "An error occurred: " + str(e)
    finally:
        # Close the session and the PDF file, and delete the PDF file
        session.disconnect()
        doc.close()
        os.remove('conversation.pdf')

        # Use the ThreadingMixIn class to handle multiple requests in parallel


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass


# Run the Flask app on a specific host and port
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
