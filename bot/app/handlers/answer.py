from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery

from helpers.image import get_image
from helpers.text import get_text_and_correct_answer
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
    questions = data["questions"]
    if is_correct_answer:
        correct += 1
        await state.update_data(correct=correct)
        answer_text = "Правильно."
    else:
        previous_question_number = data["question_number"] - 1
        previous_question = questions[previous_question_number]
        for answer in previous_question["answers"]:
            if answer["is_correct"]:
                correct_answer = answer["answer"]
        answer_text = \
            f"Неправильно.\n<b>Правильный ответ</b>: <i>{correct_answer}</i>."
    await cb.message.answer(
        text=answer_text
    )
    # Selecting a question
    question_number = data["question_number"]
    if len(questions) > question_number:
        question = questions[question_number]
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