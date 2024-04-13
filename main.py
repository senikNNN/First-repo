import random

score = {} 

def update_score(user_name, user_attempt): # Формула що записує рекорд гравця
    if user_name in score.keys():
        if user_attempt < score[user_name]:
            score.update({user_name: user_attempt})
    else:
        score.update({user_name: user_attempt})

def show_score(): 
    print("\n    Таблиця лідерів:\nName : attempt")
    for i in score:
        print(i + " : " + str(score[i]))

def make_new_attempt(): 
    name = input("\nВаше ім'я \n>>> ")

    number = random.randint(1, 1000)
    attempt = 0
    print(f"Було загадано число від 1 до 1000\n Спробуй відгадати! {number}")

    while True:
        try:
            inp = int(input(">>> "))
            if inp < 1 or inp > 1000:
                print("Вказане число навіть не є в межах вибірки. Спробуй ще раз!")
                continue
        except:
            print("Вводьте лише цілі числа!")
            continue
        attempt += 1
        
        if inp > number:
            print(f" Вказане число {inp} є завеликим!")
        elif inp < number:
            print(f" Вказане число {inp} є замалим!")
        else:
            print(f" Вітаю, ви вгадали число {number} з {attempt} спроб!")
            break
    
    update_score(name, attempt)
    show_score()
    make_new_attempt()

print("\nВітаємо вас у грі \"Вгадай, якщо зможеш\"!\nСтвореній Юрієм Сеником з великої нудьги\n")
make_new_attempt()