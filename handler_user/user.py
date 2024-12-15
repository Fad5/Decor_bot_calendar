from aiogram import Router, types
from aiogram.filters import CommandStart, Command

from hendler_csv.csv_file_download import get_info_last_download
from hendler_csv.work_csv_file import show_orders
from hendler_json.refactor import show_zoom

router = Router()


@router.message(CommandStart())
async def start_cmd(message: types.Message):
    """
    Функция приветствия
    """
    await message.answer('Hi')


@router.message(Command("tomorrow"))
async def next_day_work(message: types.Message):
    """
    Отображения зуммов на завтра по id пользователя.
    Получаем id пользователя находим в базе данных как он записан
    и начинаем поиск по имени.
    """
    list_order = show_orders(1, 2)
    for i in list_order:
        await message.answer(show_zoom(i))


@router.message(Command("today"))
async def today_work_day(message: types.Message):
    """
    Отображения зуммов на сегодня по id пользователя.
    Получаем id пользователя находим в базе данных как он записан
    и начинаем поиск по имени.
    """
    list_order = show_orders()
    for i in list_order:
        await message.answer(show_zoom(i))


@router.message(Command("upd_db"))
async def upd_db(message: types.Message):
    """
    Функция для отображения даты создания и обновление файла.
    """
    last_upd = get_info_last_download()
    await message.answer(last_upd)


@router.message()
async def echo(message: types.Message):
    """
    Функция эхо
    """
    await message.answer(message.text)
