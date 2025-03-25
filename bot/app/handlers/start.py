import os

from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, FSInputFile
import aiohttp

from constants import API_URL, IMAGES_FOLDER
from markups.answers import get_answers_markup
from router import router
from states import Questions


@router.message(Command("start"))
async def start_handler(msg: Message, state: FSMContext) -> None:
    url = API_URL + "/questions-with-answers/"
    async with aiohttp.ClientSession() as session:
        async with session.request("get", url) as response:
            response.raise_for_status()
            questions = await response.json()
    await state.update_data(questions=questions)
    question = questions[0]
    image_name = question["image"]
    image_path = os.path.join(IMAGES_FOLDER, image_name)
    image = FSInputFile(image_path)
    answers = question["answers"]
    answers_markup = get_answers_markup(answers)    
    await msg.answer_photo(
        image
    )
    await msg.answer(
        text="Что это за картина?",
        reply_markup=answers_markup
    )
    await state.update_data(question_number=1)