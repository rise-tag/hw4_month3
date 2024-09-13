from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command

from app.keyboards import start_keyboard, geeks_keyboard, direction_keyboard

router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Выберите действие:", reply_markup=start_keyboard)

# Обработчик кнопки "Geeks"
@router.message(F.text == "Geeks")
async def show_geeks(message: Message):
    await message.answer("Информация про Geeks:", reply_markup=geeks_keyboard)

# Обработчик кнопки "Направления"
@router.message(F.text == "Направления")
async def show_directions(message: Message):
    await message.answer("Выберите направление:", reply_markup=direction_keyboard)

@router.callback_query(F.data == "ux/ui")
async def show_backend_info(callback: CallbackQuery):
    await callback.answer("Вы выбрали UX/UI")
    await callback.message.edit_text("UX/UI-дизайнер ― одна из самых востребованных сегодня профессий на рынке. В этом материале мы подробно разбираем, кто такой UX/UI-дизайнер и почему UX/UI-дизайн ― не только про графику.")

@router.callback_query(F.data == "mobile")
async def show_backend_info(callback: CallbackQuery):
    await callback.answer("Вы выбрали Mobile")
    await callback.message.edit_text("Мобильный разработчик — это программист, который пишет приложения для мобильных устройств. К ним относятся не только смартфоны и планшеты, но и умные часы, фитнес-трекеры, электронные читалки, GPS-навигаторы и все остальные штуки с экраном и клавиатурой, которые можно носить с собой.")
    
@router.callback_query(F.data == "frontend")
async def show_backend_info(callback: CallbackQuery):
    await callback.answer("Вы выбрали Frontend")
    await callback.message.edit_text("Фронтенд-разработка — это создание внешнего интерфейса веб-сайтов и приложений. Для фронтенд-разработчика важно, чтобы пользователи с легкостью могли найти на сайте все, что им нужно. К примеру, прочитать подробности о товаре, узнать о его преимуществах, почитать отзывы, посмотреть видео и сделать покупку.")

@router.callback_query(F.data == "backend")
async def show_backend_info(callback: CallbackQuery):
    await callback.answer("Вы выбрали Backend")
    await callback.message.edit_text("Backend - это серверная часть приложения.")

@router.callback_query(F.data == "studio")
async def show_geeks_studio(callback: CallbackQuery):
    await callback.answer("Geeks Studio — наше креативное агентство!")
    await callback.message.edit_text("Информация про Geeks Studio")
