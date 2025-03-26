from aiogram.types import BotCommand
import asyncio

from config import bot, dp


async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    bot_commands = [
        BotCommand(command="/start", description="Начать игру.")
    ]
    await bot.set_my_commands(
        bot_commands
    )
    await dp.start_polling(
        bot,
        allowed_updates=dp.resolve_used_update_types()
    )


if __name__ == "__main__":
    asyncio.run(main())