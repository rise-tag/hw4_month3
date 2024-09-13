from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

start_button = [
    [KeyboardButton(text="Geeks"), KeyboardButton(text="Направления")]
]
start_keyboard = ReplyKeyboardMarkup(keyboard=start_button, resize_keyboard=True, one_time_keyboard=True)

geeks_inline = [
    [InlineKeyboardButton(text="GeeksPro", url="https://geeks.kg/geeks-pro")],
    [InlineKeyboardButton(text="Geeks.kg", url="https://geeks.kg/")],
    [InlineKeyboardButton(text="Geeks Studio", url="https://geekstudio.kg/")]
]
geeks_keyboard = InlineKeyboardMarkup(inline_keyboard=geeks_inline)

direction_inline = [
    [InlineKeyboardButton(text="Backend", callback_data="backend")],
    [InlineKeyboardButton(text="Frontend", callback_data="frontend")],
    [InlineKeyboardButton(text="Mobile", callback_data="mobile")],
    [InlineKeyboardButton(text="UX/UI", callback_data="ux/ui")]
]
direction_keyboard = InlineKeyboardMarkup(inline_keyboard=direction_inline)
