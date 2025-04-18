import os

from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, FSInputFile

from constants import IMAGES_FOLDER
from markups.answers import get_answers_markup
from router import router
from states import Questions


@router.callback_query(F.data.in_({'0', '1'}))
async def answer_handler(
    cb: CallbackQuery,
    state: FSMContext
) -> None:
    # Adding a correct answer
    data = await state.get_data()
    correct = data.get("correct", 0)
    is_correct_answer = int(cb.data)
    if is_correct_answer:
        correct += 1
        await state.update_data(correct=correct)
        answer_text = "✅Правильно! Молодец."
    else:
        answer_text = "Неправильно."
    await cb.message.answer(
        text=answer_text
    )
    # Selecting a question
    questions = data["questions"]
    question_number = data["question_number"]
    if len(questions) > question_number:
        question = questions[question_number]
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
        await cb.message.answer_photo(
            image
        )
        await cb.message.answer(
            text=question_with_answers,
            reply_markup=answers_markup
        )
        question_number += 1
        await state.update_data(question_number=question_number)
    else:
        result = int(correct / len(questions) * 100)
        await cb.message.answer(
            text=f"Ваш результат: {result}%"
        )
        await state.clear()