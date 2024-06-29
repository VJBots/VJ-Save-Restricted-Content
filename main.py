#import uvloop
from pyrogram import Client
from pyromod import listen
from config import APP_ID, API_HASH, TG_BOT_TOKEN
import asyncio 
from os import environ, execle, system

async def restart_after_delay(delay):
    await asyncio.sleep(delay)
    system("git pull -f && pip3 install --no-cache-dir -r requirements.txt")
    execle(sys.executable, sys.executable, "bot.py", environ)
    print('🖍️ Bot Restarted After 15000 Seconds ✔️')

class Bot(Client):

    def __init__(self):
        super().__init__(
            "droplink search bot",
            api_id=APP_ID,
            api_hash=API_HASH,
            bot_token=TG_BOT_TOKEN,
            plugins=dict(root="plugins"),
            workers=50,
            sleep_threshold=10
        )

      
    async def start(self):
            
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        print('Bot Restart After 15000 Second')
        asyncio.create_task(restart_after_delay(15000))   
        print('Bot Started Powered By @VJ_Botz')


    async def stop(self, *args):

        await super().stop()
        print('Bot Stopped Bye')


#uvloop.install()

