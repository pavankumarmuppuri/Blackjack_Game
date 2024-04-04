import random

def game() :

  def deal_card() :
    #cards = [11,10, 11]
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
  deal_card()
  user_card = []
  computer_card = []


  for i in range(2):
    user_card.append(deal_card())
    computer_card.append(deal_card())

  #print(user_card)
  #print(computer_card)

  def calculate_score() :


    if sum(user_card) == 21 :
      return 0
    #else :
      #print(sum(user_card))
    if sum(computer_card) == 21 :
      return 0
    #else :
      #print(sum(computer_card))


    if sum(user_card) >= 22 :
      if user_card[-1] == 11 :
        user_card.remove(11)
        user_card.append(1)
      #print(sum(user_card))
    if sum(computer_card) >= 22 :
      if computer_card[-1] == 11 :
        computer_card.remove(11)
        computer_card.append(1)
      #print(sum(computer_card))

  calculate_score()

  while sum(computer_card) == 21 : #or sum(user_card) > 21 :
    print("You Lost the Game !!")
    print(f"Computer got the BlackJack {computer_card}")
    break
  while sum(user_card) == 21 :
    print("You Won the Game")
    print(f"You got the BlackJack {user_card}")
    break
  if sum(computer_card) != 21 and sum(user_card) != 21 :
    while sum(user_card) < 21 :
    #elif sum(user_card) < 21 :
      print(f"Your cards are : {user_card} and Score is : {sum(user_card)}")
      print(f"Computer first card is {computer_card[0]}")
      choice = input("Do you Wish to draw the Card ? Y or N  : ").upper()
      if choice == "Y" :
        user_card.append(deal_card())
        calculate_score()
        print(user_card)
        print(sum(user_card))
        if sum(user_card) > 21 :
          print("You lost  the game")
          print(f"Computer cards are : {computer_card} and Score is {sum(computer_card)}")
          print(f"Your cards are {user_card} and Score is : {sum(user_card)}")
      elif choice == "N" :

        while sum(computer_card) < 17 :
          computer_card.append(deal_card())
          calculate_score()
          #print(f"Computer's Cards are : {computer_card}")
        if sum(computer_card) > 21 :
          print("You Won the Game")
          print(f"Your cards are {user_card} and Score is : {sum(user_card)}")
          print(f"Computer cards are : {computer_card} and Score is {sum(computer_card)}")
        else :
          if sum(user_card) > sum(computer_card) :
            print("You won the Game")
            print(f"Your cards are {user_card} and Score is : {sum(user_card)}")
            print(f"Computer cards are : {computer_card} and Score is {sum(computer_card)}")
          elif sum(user_card) == sum(computer_card) :
            print("It's a TIE !!!")
            print(f"Your cards are {user_card} and Score is : {sum(user_card)}")
            print(f"Computer cards are : {computer_card} and Score is {sum(computer_card)}")
          else:
            print("You lost the game")
            print(f"Computer cards are : {computer_card} and Score is {sum(computer_card)}")
            print(f"Your cards are {user_card} and Score is : {sum(user_card)}")
        break

while True :
  game()
  restart = input("Do you Want to Restart the Game ? Y/N ").upper()
  if restart == "N" :
    break
  elif restart == "Y" :
    continue