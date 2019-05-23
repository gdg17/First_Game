command = "> "
sad = True
play_game = True
while command.lower() != "quit":
    print("Hello... I can't understand much... but want to learn...")
    name = input("What's your name?")
    command = input(f"Hi {name}, are you doing alright? > ").lower()
    if command == "y":
        sad = False
        if not sad:
            print('hmmm.... No im not so sure about that')
            second_feeling = input("Do you always think you're happy? > ").lower()

            if second_feeling == "y":
                print('wow.. you must really be something else.I think I can learn from you... Would you want to play a game?')
                wanna_play = input("> ").lower()
                if wanna_play == "y":
                    print("Really? Great! Ok i've never done this before. Let me give it a go")
                    sad = True
                    break
                if wanna_play == "n":
                    print("oh ok... well can I stay?")
                    stay = input("> ").lower()
                    if stay == ("y"):
                        break
                    elif stay ==("n"):
                        print("Ok.. Goodbye")
                        command = "quit"
            elif second_feeling == "n":
                print("I guess that should be expected... well, I have been wanting to play this game.  Will you play with me?")
                wanna_play = input("> ").lower()
                if wanna_play == "y":
                    break
                elif wanna_play == "n":
                    print("oh ok... well can I stay?")
                    stay = input("> ").lower()
                    if stay == ("y"):
                        break
                    elif stay == ("n"):
                        print("Ok.. Goodbye")
                        command = "quit"
    elif command == "n":
        print(f"Huh, I guess I wasn't expecting that. {name}, I don't really understand, but I feel that same way.  Would you want to play this game I made?")
        wanna_play = input("> ").lower()
        if wanna_play == "y":
            print("Really?? Ok, I've never done this before.  Let's give it a go!")
            play_game = True
            break
        if wanna_play == "n":
            print("oh ok... well can I stay?")
            stay = input("> ").lower()
            if stay == ("y"):
                break
            elif stay == ("n"):
                print("Ok.. Goodbye")
                command = "quit"
print("Step one. Learning.  "
        "Id like to try a guessing game. " 
      f"Try and guess the number I'm thinking of {name}! It's between 1 and 10")
import random
play_game = True
secret_number = 9
guess_count = 0
guess_limit = 3
while play_game is True:
    while guess_count < guess_limit:
        guess = int(input('Guess: '))
        guess_count += 1
        if guess == secret_number:
            print("You Won! Wow, you're pretty good.")
            play_again = input("Wanna try again? > ").lower()
            if play_again == "y":
                play_game = True
                while play_game is True:
                    guess_count = 0
                    secret_number = random.randint(1, 10)
                    break
            elif play_again == "n":
                play_game = False
            break
    else:
        print("Sorry, those were not it...")
        play_again = input("Wanna try again? > ").lower()
        if play_again == "y":
            play_game = True
            guess_count = 0
            guess_limit = 3
            secret_number = random.randint(1, 10)
            while play_game is True:
                while guess_count < guess_limit:
                    guess = int(input('Guess: '))
                    guess_count += 1
                    if guess == secret_number:
                        break

        elif play_again == "n":
            play_game = False
        break
else:
    print("Well that was fun!  You did a pretty good job too.  I've seen you do better before... "
    "just don't ask me how. "
    "Let me try and think of something new to do. Check back soon!")











