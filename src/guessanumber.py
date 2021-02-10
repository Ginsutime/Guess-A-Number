import random


def game_start():
    print("I'm thinking of 3 numbers between 1 and 10.")
    print("Guess one of them.")
    number_gen_list_results = random_number_generation()
    answer_checker(number_gen_list_results)


def game_input():
    while True:
        try:
            player_input = int(input("Take a guess: "))
            if 0 < player_input < 11:
                return player_input
            else:
                print("Your answer is not within the range of 1 to 10.")
        except ValueError:
            print("You've entered an answer that isn't a number.")


def random_number_generation():
    rand_list = []
    while len(rand_list) < 3:
        result = random.randint(1, 10)
        if result not in rand_list:
            rand_list.append(result)
    rand_list.sort()
    return rand_list


def answer_checker(number_gen_list: list[int]):
    answer = game_input()
    if answer in number_gen_list:
        print("Correct. The numbers are "
              + ", ".join(str(n) for n in number_gen_list) + ".")
    else:
        print("Incorrect. The numbers are "
              + ", ".join(str(n) for n in number_gen_list) + ".")
    game_restart()


def game_restart():
    while True:
        restart_input = input("Press Q to exit or "
                              "any other key to continue: ").lower()
        if restart_input == 'q':
            quit()
        else:
            game_start()


game_start()
