from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.fsm.storage.memory import MemoryStorage

from constants import BOT_TOKEN
import handlers
from router import router


bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode="html")
)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(router)