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


def create_group_kb(groups):
    kb = []
    for group in groups:
        kb.append([InlineKeyboardButton(text=group, callback_data=group)])
    return InlineKeyboardMarkup(inline_keyboard=kb)


group_kb = create_group_kb(['М3В-337Бк-22', 'М3О-301Б-22', 'М3О-302Бки-22', 'М3О-304Б-22', 'М3О-305Б-22',
                            'М3О-306Б-22', 'М3О-308Бки-22', 'М3О-309Б-22', 'М3О-310Б-22', 'М3О-311Б-22',
                            'М3О-312Б-22', 'М3О-314Б-22', 'М3О-315Б-22', 'М3О-316Б-22', 'М3О-317Бк-22',
                            'М3О-319Бк-22', 'М3О-321Б-22', 'М3О-322Бк-22', 'М3О-323Б-22', 'М3О-325Бк-22',
                            'М3О-326Б-22', 'М3О-329Б-22', 'М3О-332Б-22', 'М3О-333Б-22', 'М3О-334Б-22',
                            'М3О-335Б-22', 'М3О-336Б-22'])
