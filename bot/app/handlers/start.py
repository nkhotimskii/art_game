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
    question_text = "<b>Что это за картина?</b>"
    answers_text = ""
    for idx, answer in enumerate(answers):
        answer_text = answer["answer"]
        is_correct = answer["is_correct"]
        answer_number = idx + 1
        answers_text += f"{answer_number}. <i>{answer_text}</i>.\n"
        if is_correct:
            correct_answer_idx = idx
    question_with_answers = question_text + "\n"*2 + answers_text
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