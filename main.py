import os
from pyrogram import filters, Client
from yt_dlp import YoutubeDL as YT

API_ID= 7541185
API_HASH= "4fde419fee2465bd03d68b1da1852459"
BOT_TOKEN= "5633804378:AAGlUHOaz86ac7BKrjTkNMYsqDJVJ9FWZvo"

bot= Client(
    "Porno Gallery Uploader Bot",
    api_id= API_ID,
    api_hash= API_HASH,
    bot_token= BOT_TOKEN,
)

@bot.on_message(filters.private & filters.command("start"))
def start(client, message):
    print("Started!")
    uid= message.from_user.id
    bot.send_message(uid, "Bot Started...!")

@bot.on_message(filters.private & filters.text)
def download(client, message):
    uid= message.from_user.id
    url= message.text

    bot.send_message(uid, "Started to Download Media...!")

    ydl_opts= {
        'format': 'hls-1839-1',
        'outtmpl': 'Downloads/video.mp4'
    }

    YT(ydl_opts).download(url)
    
    bot.send_message(uid, "Sending the media!")
    bot.send_video(uid, "Downloads/video.mp4")

    os.remove('Downloads/video.mp4')

bot.run()