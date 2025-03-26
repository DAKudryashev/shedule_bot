from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

start_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='СТАРТ')]], resize_keyboard=True,
                               input_field_placeholder='Для начала работы нажмите кнопку старт...',
                               is_persistent=True, one_time_keyboard=True)

department_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Институт №1', callback_data='Институт №1'),
     InlineKeyboardButton(text='Институт №2', callback_data='Институт №2')],

    [InlineKeyboardButton(text='Институт №3', callback_data='Институт №3'),
     InlineKeyboardButton(text='Институт №4', callback_data='Институт №4')],

    [InlineKeyboardButton(text='Институт №5', callback_data='Институт №5'),
     InlineKeyboardButton(text='Институт №6', callback_data='Институт №6')],

    [InlineKeyboardButton(text='Институт №7', callback_data='Институт №7'),
     InlineKeyboardButton(text='Институт №8', callback_data='Институт №8')],

    [InlineKeyboardButton(text='Институт №9', callback_data='Институт №9'),
     InlineKeyboardButton(text='Институт №10', callback_data='Институт №10')],

    [InlineKeyboardButton(text='Институт №11', callback_data='Институт №11'),
     InlineKeyboardButton(text='Институт №12', callback_data='Институт №12')]])

course_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='1'), InlineKeyboardButton(text='2', callback_data='2')],
    [InlineKeyboardButton(text='3', callback_data='3'), InlineKeyboardButton(text='4', callback_data='4')],
    [InlineKeyboardButton(text='5', callback_data='5'), InlineKeyboardButton(text='6', callback_data='6')]])


def create_group_kb():
    pass

group_kb = create_group_kb()
