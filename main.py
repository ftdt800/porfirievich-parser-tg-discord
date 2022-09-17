import time
import pyperclip
import keyboard
from keyboard import press
from pyrogram import Client, types, filters, enums
chat_id = 1019975265 # Don't edit
app = Client(name='sessionon', api_id=ID_HERE, api_hash='HASH_HERE') #сюды надо писать
def ctrl_key(key):
    keyboard.press(29)
    time.sleep(0.02)
    keyboard.press(key)
    time.sleep(0.02)
    keyboard.release(29)
    keyboard.release(key)
    time.sleep(0.02)
async def main():
    async with app:
        await app.send_message("@PorfBot", text)
        time.sleep(5)
        async for message in app.search_messages(chat_id, limit=1):
            print(message.text)
            pyperclip.copy(message.text)
            ctrl_key(47)
            if not message.text == text:
                press('enter')
while 1==1:
    keyboard.wait('Ctrl + C')
    text = pyperclip.paste()
    app.run(main())