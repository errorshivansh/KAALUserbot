# Credit To @Murat_30_God . Keep credit if you are going to edit it. Join @kaalsupport01


import asyncio

from kaalBOT.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern="test ?(.*)"))
@bot.on(sudo_cmd(pattern="test ?(.*)", allow_sudo=True))
async def _(event):
    if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):

        await edit_or_reply(event, "`Testing kaalBOT`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing kaalBOT.`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing kaalBOT..`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing kaalBOT...`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing kaalBOT....`")
        await asyncio.sleep(1)
        await edit_or_reply(event, "`Testing kaalBOT.....`")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Testing Successful__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "`Generating Output`\nPlease wait")
        await asyncio.sleep(2)
        await edit_or_reply(event, "__Output Generated Successfully__")
        await asyncio.sleep(2)
        await edit_or_reply(event, "**SAVING OUTPUT TO kaalBOT LOCAL DATABASE**")
        await asyncio.sleep(3.5)
        await edit_or_reply(event, 
            "Your[kaalBOT](https:/t.me/kaalsupport01) is working Fine...\n       Join @kaalsupport For Any Help......"
        )

CmdHelp("test").add_command(
  "test", None, "Test wether your bot is running or not."
).add()
