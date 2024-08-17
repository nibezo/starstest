import asyncio
import logging

from aiogram import Dispatcher, F
from aiogram.filters import Command, ChatMemberUpdatedFilter, IS_NOT_MEMBER, IS_MEMBER
from aiogram import Bot
from aiogram.client.default import DefaultBotProperties

from botlogic.handlers import payment

bot = Bot(
    token="",
    default=DefaultBotProperties(parse_mode="HTML"),
)

async def start():
    dp = Dispatcher()

    dp.pre_checkout_query.register(payment.pre_checkout_handler)
    dp.message.register(payment.pay_support_handler, Command(commands="paysupport"))
    dp.message.register(payment.send_invoice_handler, Command(commands="donate"))
    dp.message.register(payment.success_payment_handler, F.successful_payment)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(start())
