from random import randint

secret_num = randint(1, 100)
num_guesses = 0  # 시도 횟수
guess = 0  # 예상 숫자

while guess != secret_num and num_guesses <= 4:
    guess = eval(input('Enter your guess (1-100): '))
    num_guesses = num_guesses + 1
    if guess < secret_num:
        print('더 큽니다.', 5 - num_guesses, '회 남았습니다.\n')
    elif guess > secret_num:
        print('더 작습니다.', 5 - num_guesses, '회 남았습니다.\n')
    else:
        print('맞았습니다!')
    if num_guesses == 5 and guess != secret_num:
        print('당신이 졌습니다. 정답은', secret_num, '입니다')
