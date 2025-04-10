import random

secret = random.randint(1, 100)

print("Вгадайте число від 1 до 100. У вас є 7 спроб.")

for attempt in range(1, 8):
    guess = int(input(f"Спроба {attempt}: "))

    if guess == secret:
        print(f"Вітаю! Ви вгадали за {attempt} спроб.")
        break
    elif guess < secret:
        print("Загадане число більше.")
    else:
        print("Загадане число менше.")
else:
    print(f"На жаль, ви не вгадали. Це було число {secret}.")
