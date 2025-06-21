from random import randint
from qna_dict import qna

count = 0
labels = ["A", "B", "C", "D"]

for i in range(5):
    keys = list(qna.keys())
    random_num = randint(0, len(keys) - 1)
    question = keys[random_num]

    print(question)
    options = qna[question]["options"]
    for idx, option in enumerate(options):
        print(f"{labels[idx]}. {option}")

    answer_input = input("Enter your option (A/B/C/D): ").strip().upper()

    correct_letter = qna[question]["answer"]
    correct_idx = labels.index(correct_letter)
    correct_option = options[correct_idx]

    if answer_input == correct_letter:
        print(f"Correct! The answer is {correct_letter}. {correct_option}")
        count += 1
    else:
        print(f"Wrong! The correct answer is {correct_letter}. {correct_option}")

    qna.pop(question)

print(f"Your Score is {count}/5")
