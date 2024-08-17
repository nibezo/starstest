from aiogram.utils.keyboard import InlineKeyboardBuilder


def payment_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text=f"Pay 10 ⭐️", pay=True)

    return builder.as_markup()
