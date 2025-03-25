from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_answers_markup(answers: list) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for answer in answers:
        answer_text = answer["answer"]
        is_correct = str(int(answer["is_correct"]))
        answer_btn = InlineKeyboardButton(
            text=answer_text,
            callback_data=is_correct
        )
        builder.add(answer_btn)
    builder.adjust(1)
    markup = InlineKeyboardMarkup(
        inline_keyboard=builder.export()
    )
    return markup