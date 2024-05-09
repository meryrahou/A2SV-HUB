# Problem: B - Firaols Contest - https://codeforces.com/gym/505936/problem/B

max_diff , problems = map(int, input().split())
difficulties = list(map(int, input().split()))


difficulty_cout = {}


res = []


# def can_round(list_probs):
#     if 0 not in list_probs:
#         for i in range(len(list_probs)):
#             list_probs[i] -= 1
#         return True
#     return False

# for problem in difficulties:
#     list_probs[problem - 1] += 1
#     if can_round(list_probs):
#         return_char += '1'
#     else:
#         return_char += '0'


# fixing it in order not to exceed time limit

for problem in difficulties:
    if problem not in difficulty_cout:
        difficulty_cout[problem] = 0
    difficulty_cout[problem] += 1

    if len(difficulty_cout) == max_diff:
        res.append('1')
        for diff in list(difficulty_cout.keys()):
            difficulty_cout[diff] -= 1
            if difficulty_cout[diff] == 0:
                del difficulty_cout[diff]

    else:
        res.append('0')

print(''.join(res))

