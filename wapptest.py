import os
from twilio.rest import Client
from PIL import Image

TWILIO_ACCOUNT_SID = 'AC4090af5a09cb929a72877bf016af0b72'
TWILIO_AUTH_TOKEN = 'ea6c989203b9c175e02c16af729f5d9b'

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your personal WhatsApp Messaging number
to_whatsapp_number='whatsapp:+351912978678'

img = Image.open('listarank.jpeg')

message = client.messages.create(body='Check out this owl!',
                       media_url='https://demo.twilio.com/owl.png',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
