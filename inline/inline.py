from uuid import uuid4
from telegram import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    InlineQueryResultArticle,
    InputTextMessageContent
)
from config import FOOTER_TEXT

from helpers.torrent import torrent_search

def button(update, context):
    query = update.callback_query
    query.answer()
    torrent_name = query.data
    query.edit_message_text(text="Just a moment adding some final touch")
    if torrent_name == None:
        query.edit_message_text(text="may be next year🐙")
        return
    response = torrent_search(torrent_name)
    if response == None:
        query.edit_message_text(text="may be next year🐙")
        return
    if len(response) == 0:
        query.edit_message_text(text="may be next year🐙")
        return

    
    
    
    name = response[0].get("name")
    age = response[0].get("age")
    leechers = response[0].get("leecher")
    magnet_link = response[0].get("magnet")
    seeders = response[0].get("seeder")
    size = response[0].get("size")
    type_of_file = response[0].get("type")
    site = response[0].get("site")
    torrent_url = response[0].get("url")
    buttons = [[InlineKeyboardButton(text="Try InlineQuery", switch_inline_query="")]]

    query.edit_message_text(text=f"*Name : {name}\nSize : {size}\nAge : {age}\nLeechers : {leechers}\nNo: of seeds : {seeders}\nType of File : {type_of_file}\nTorrent Url : {torrent_url}*\n\n*Magnet Link : *`{magnet_link}`\n\n*Powered by {site} website*\n\n{FOOTER_TEXT}", parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(buttons))


