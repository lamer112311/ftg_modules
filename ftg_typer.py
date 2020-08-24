from .. import loader, utils

from telethon.errors.rpcerrorlist import MessageNotModifiedError

import logging
import asyncio

logger = logging.getLogger(__name__)


def register(cb):
    cb(TyperMod())


@loader.tds
class TyperMod(loader.Module):
    """Makes your messages type slower"""
    strings = {"name": "Typer2",
               "no_message": "<b>You can't type nothing!</b>",
               "type_char_cfg_doc": "Character for typewriter"}

    def __init__(self):
        self.config = loader.ModuleConfig("TYPE_CHAR", "|", lambda: self.strings["type_char_cfg_doc"])
        self.name = self.strings["name"]

    async def typecmd(self, message):
        """.т <message>"""
        a = utils.get_args_raw(message)
        if not a:
            await utils.answer(message, self.strings["no_message"])
            return
        m = ""
        for c in a:
            m += self.config["TYPE_CHAR"]
            message = await update_message(message, m)
            await asyncio.sleep(0.04)
            m = m[:-1] + c
            message = await update_message(message, m)
            await asyncio.sleep(0.02)


async def update_message(message, m):
    try:
        return await message.edit(m)
    except MessageNotModifiedError:
        return message  # space doesnt count