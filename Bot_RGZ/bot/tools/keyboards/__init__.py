from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Этот код импортирует два класса из модуля aiogram.types: InlineKeyboardMarkup и InlineKeyboardButton.
#
# InlineKeyboardMarkup представляет разметку клавиатуры с кнопками в виде сетки.
# Она используется для создания встроенной (инлайн) клавиатуры в сообщениях.
# InlineKeyboardButton представляет кнопку встроенной клавиатуры.
# Она используется для создания отдельных кнопок, которые пользователь может нажимать для выполнения определенных действий.
# Эти классы позволяют создавать и настраивать встроенные клавиатуры для взаимодействия с пользователем в
# Telegram боте.

def menu_inlines():
    markup = InlineKeyboardMarkup(row_width=1)

    markup.add(InlineKeyboardButton("Добавить ценную бумагу к портфелю", callback_data='add_security'))
    markup.add(InlineKeyboardButton("Показатели отслеживаемых ценных бумаг", callback_data='indicators_security'))

    return markup

# Эта функция menu_inlines() создает и возвращает объект InlineKeyboardMarkup,
# представляющий разметку встроенной клавиатуры.
# В данном случае, создается вертикальная клавиатура с одной кнопкой на каждой строке.
#
# InlineKeyboardMarkup(row_width=1) создает объект разметки встроенной клавиатуры с одной кнопкой в каждой строке.
# markup.add(InlineKeyboardButton("Добавить ценную бумагу к портфелю", callback_data='add_security:'))
# добавляет кнопку "Добавить ценную бумагу к портфелю" в разметку.
# Когда эта кнопка будет нажата, будет отправлено callback-сообщение с данными "add_security:".
# markup.add(InlineKeyboardButton("Показатели отслеживаемых ценных бумаг", callback_data='indicators_security:'))
# добавляет кнопку "Показатели отслеживаемых ценных бумаг" в разметку.
# Когда эта кнопка будет нажата, будет отправлено callback-сообщение с данными "indicators_security:".
# Функция menu_inlines() полезна для создания встроенной клавиатуры с заданными кнопками и их callback-данными.


def back():
    markup = InlineKeyboardMarkup(row_width=1)
    markup.add(InlineKeyboardButton('🔙 меню', callback_data='back'))

    return markup

# Эта функция back() создает и возвращает объект InlineKeyboardMarkup,
# представляющий разметку встроенной клавиатуры с кнопкой "🔙 меню" для возврата в предыдущее меню.
#
# InlineKeyboardMarkup(row_width=1) создает объект разметки встроенной клавиатуры с одной кнопкой в каждой строке.
# markup.add(InlineKeyboardButton('🔙 меню', callback_data='back')) добавляет кнопку "🔙 меню" в разметку.
# Когда эта кнопка будет нажата, будет отправлено callback-сообщение с данными "back".
# Функция back() полезна для создания кнопки возврата в предыдущее меню при использовании встроенных клавиатур.