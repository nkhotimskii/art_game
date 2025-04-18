from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
import aiohttp

from constants import API_URL
from helpers.image import get_image
from helpers.text import get_text_and_correct_answer
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
    image = get_image(image_name)
    answers = question["answers"]
    question_with_answers, correct_answer_idx = \
            get_text_and_correct_answer(answers)
    answers_quantity = len(answers)
    answers_markup = get_answers_markup(
        answers_quantity,
        correct_answer_idx
    )
    await msg.answer_photo(
        image
    )
    await msg.answer(
        text=question_with_answers,
        reply_markup=answers_markup
    )
    await state.update_data(question_number=1)