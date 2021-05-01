from telethon.sessions import StringSession

from telethon.sync import TelegramClient

print("")

print("""Enter Your Valid Phone No. With Contry Code To Continue!\n\n """)

API_KEY = "5445895"

API_HASH = "b104f43c21861654005fa97c96a8a06f"

while True:

    try:

        with TelegramClient(StringSession(), API_KEY, API_HASH) as client:

            print(

                "String Session Sucessfully Sent To Your Saved Message, Store It To A Safe Place!!\n\n "

            )

            print("")

            session = client.session.save()

            client.send_message(

                "me",

                f"Here is your TELEGRAM STRING SESSION\n(Tap to copy it)👇 \n\n {session} \n\n"



