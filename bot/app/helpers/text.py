from typing import List, Dict


def get_text_and_correct_answer(answers: List[Dict]) -> str:
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
    return question_with_answers, correct_answer_idx