from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from Config import MUST_JOIN


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link ="https://t.me/Disney_storeDan" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"𝙹𝙾𝙸𝙽 𝙺𝙴 𝙶𝚁𝚄𝙿 𝙳𝚄𝙻𝚄 [CHANEL]("https://t.me/Disney_storeDan") 𝚄𝙽𝚃𝚄𝙺 𝙼𝙴𝙽𝙶𝙶𝚄𝙽𝙰𝙺𝙰𝙽 𝙱𝙾𝚃 𝙸𝙽𝙸. 𝚂𝙴𝚃𝙴𝙻𝙰𝙷 𝙸𝚃𝚄 𝚂𝚃𝙰𝚁𝚃 𝙺𝙴𝙼𝙱𝙰𝙻𝙸 /start",
                    disable_web_page_preview=Ture,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("ᴅᴀɴ sᴜᴘᴘᴏʀᴛ​", url="https://t.me/musik_supportdan")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat : {MUST_JOIN} !")
