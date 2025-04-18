from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder


def get_answers_markup(
    answers_quantity: int,
    correct_answer_idx: int
) -> InlineKeyboardMarkup:
    builder = InlineKeyboardBuilder()
    for answer_idx in range(answers_quantity):
        is_correct = False
        if answer_idx == correct_answer_idx:
            is_correct = True
        answer_btn = InlineKeyboardButton(
            text=str(answer_idx + 1),
            callback_data=str(int(is_correct))
        )
        builder.add(answer_btn)
    builder.adjust(2)
    markup = InlineKeyboardMarkup(
        inline_keyboard=builder.export()
    )
    return markup