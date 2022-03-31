'''NOTE *NO BACKTRACKING 
   LINK: https://www.youtube.com/watch?v=rA3a8QDtYLs

   STEP1: GENERATE A RANDOM SOLUTION
   STP2: EVALUATE THAT SOLUTION
   STEP3: GENERATE ANOTHER SOLUTION

   '''

import random
import string


def generate_random_solutions(answer):
    length = len(answer)
    return [random.choice(string.printable) for _ in range(length)]


def evaluate(solution, answer):
    target = list(answer)
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s) - ord(t))
    return diff


def mutate_solution(solution):
    index = random.randint(0, len(solution) - 1)
    solution[index] = random.choice(string.printable)


answer = "Hello Wor"
best = generate_random_solutions(answer)
best_score = evaluate(best, answer)
while True:
    print('The best score is: ', best_score, 'SOLUTION: ', " ".join(best))
    if best_score == 0:
        break
    new_solution = list(best)
    mutate_solution(new_solution)

    score = evaluate(new_solution, answer)
    if evaluate(new_solution, answer) < best_score:
        best = new_solution
        best_score = score
