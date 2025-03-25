from aiogram.fsm.state import State, StatesGroup


class Questions(StatesGroup):
    questions = State()
    question_number = State()
    correct = State()