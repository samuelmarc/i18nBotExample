import logging

from pyrogram import Client, filters
from pyrogram.enums import ParseMode

from gettext import _


logging.basicConfig(level=logging.INFO)


API_ID = 0
API_HASH = ''
BOT_TOKEN = ''


def get_lang(func):
    async def wrapper(cl, mc, *args, **kwargs):
        return await func(cl, mc, mc.from_user.language_code, *args, **kwargs)

    return wrapper


app = Client(
    'i18nbot',
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    parse_mode=ParseMode.HTML
)


@app.on_message(filters.command('start'))
@get_lang
async def start_example(__, m, lang):
    return await m.reply(_('start', lang, mention=m.from_user.mention))


app.run()
