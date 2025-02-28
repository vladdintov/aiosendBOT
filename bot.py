import asyncio
from aiogram import Bot, Dispatcher
from aiosend import CryptoPay

cp = CryptoPay("TOKEN")
bot = Bot("TOKEN")
dp = Dispatcher()


@dp.message()
async def get_invoice(message):
    invoice = await cp.create_invoice(1, "USDT")
    await message.answer(f"Оплати счет для покупки токена: {invoice.bot_invoice_url}")
    invoice.poll(message=message)


@cp.invoice_polling()
async def handle_payment(invoice, message):
    await message.answer(f"Счет оплачен, ваш товар: 123:qwerty")


async def main():
    await asyncio.gather(
        dp.start_polling(bot),
        cp.start_polling(),
    )


if __name__ == "__main__":
    asyncio.run(main())
