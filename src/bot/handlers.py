from aiogram import F, Router
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

from bot.keyboards import start_kb, department_kb, course_kb, group_kb

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Начнем?', reply_markup=start_kb)


@router.message(F.text == 'СТАРТ')
async def start_pressed(message: Message):
    await message.answer('Выбери свое место учебы...', reply_markup=department_kb)


@router.callback_query(F.data.startswith('Институт'))
async def department_selected(callback: CallbackQuery):
    await callback.answer('Вы выбрали какой-то институт')
    await callback.message.edit_text('Выбери свой курс...', reply_markup=course_kb)


@router.callback_query(F.data.in_({'1', '2', '3', '4', '5', '6'}))
async def course_selected(callback: CallbackQuery):
    await callback.answer('Вы выбрали какой-то номер курса')
    await callback.message.edit_text('Выберите группу', reply_markup=group_kb)


@router.callback_query(F.data.in_())
async  def group_selected(callback: CallbackQuery):
    pass
