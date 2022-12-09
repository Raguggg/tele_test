
from pyrogram import Client, filters

API_ID = "7280833"
API_HASH = "faa0e3b6d30779426d833dec02ab70d9"
TOKEN = "1969982366:AAHoE4d2bnRem_Ng8pL694z_jHQAXMJB6LA"

app = Client("tagremover", bot_token=TOKEN, api_id=API_ID, api_hash=API_HASH)

def progress_show(percent=0, width=40):
    left = width * percent // 100
    right = width - left

    tags = "#" * left
    spaces = " " * right
    percents = f"{percent:.0f}%"

    print("\r[", tags, spaces, "]", percents, sep="", end="", flush=True)
async def progress(current, total):
    progress_show(round(current * 100 / total))
    # print(f"{current * 100 / total:.1f}%")

@app.on_message(filters.private & filters.text | filters.media)
async def tag(client, message):
    print(message,sep=" <---> ")
    await client.send_message(
        chat_id=message.chat.id,
        text=str(message),
        reply_to_message_id=message.id
    )
    await app.download_media(message, progress=progress,file_name="/content/drive/MyDrive/telegram/download/")
app.run()
