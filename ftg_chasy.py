from telethon import events
import asyncio
import os
import sys
a = 0

@borg.on(events.NewMessage(pattern=r"\.ч", outgoing=True))#🕐🕑🕒🕓🕔🕕🕖🕗🕘🕙
async def _(event):
    if event.fwd_from:
        return
        if a<4:
     await event.edit("🕐")
     await asyncio.sleep(0.5)
     await event.edit("🕑")
     await asyncio.sleep(0.5)
     await event.edit("🕒..")
     await asyncio.sleep(0.5)
     await event.edit("🕓")
     await asyncio.sleep(0.5)
     await event.edit("🕕")
     await asyncio.sleep(0.5)
     await event.edit("🕖")
     await asyncio.sleep(0.5)
     await event.edit("🕗")
     await asyncio.sleep(0.5)
     await event.edit("🕘")
     await asyncio.sleep(0.5)
     await event.edit("🕙")
     await asyncio.sleep(0.5)
     a+1

    
    