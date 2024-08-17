from aiogram.exceptions import TelegramBadRequest
from aiogram.types import LabeledPrice, Message, PreCheckoutQuery

from botlogic.keyboards.payment_keyboard import payment_keyboard


async def send_invoice_handler(message: Message):

    prices = [LabeledPrice(label="XTR", amount=10)]
    await message.answer_invoice(
        title="Stars payment test",
        description="Pay 10 ⭐️",
        prices=prices,
        provider_token="",
        payload="channel_support",
        currency="XTR",
        reply_markup=payment_keyboard(),
    )


async def pre_checkout_handler(pre_checkout_query: PreCheckoutQuery):
    await pre_checkout_query.answer(ok=True)


async def success_payment_handler(message: Message):
    await message.answer(text="Thanks you for donating!🤗")


async def pay_support_handler(message: Message):
    await message.answer(
        text="If you have any questions, please write to @<name>",
    )
