from random import randint
# Initialize points for user and dealer.
user_points = 1000
dealer_points = 1000
round_number = 1
print("\nWelcome to Blackjack Game!\n")
# Game loop.
while True:
    print("\n###############################\n")
    print("Round => " + str(round_number))
    print("Current User Points => " + str(user_points))
    print("Current Dealer Points => " + str(dealer_points))
    print("\n###############################\n")
    # User places a bet.
    bet = int(input("Please place your bet: "))
    # Check if bet is valid.
    if bet > min(user_points, dealer_points) or bet <= 0:
        print("Maximum bet is " + str(min(user_points, dealer_points)) + " and Minumum bet is 0. Please change your bet.")
        bet = min(user_points, dealer_points)
        continue
    # Draw initial cards for user and dealer.    
    user_cards = [min(10, randint(1, 13)), min(10, randint(1, 13))]
    dealer_cards = [min(10, randint(1, 13)), min(10, randint(1, 13))]   
    # Calculate initial scores.
    user_score = 0
    for card in user_cards:
        user_score += card
        # Check Ace for user.
        if 1 in user_cards and user_score + 10 <= 21:
            user_score += 10
    dealer_score = 0
    for card in dealer_cards:
        dealer_score += card
        # Check Ace for dealer.
        if 1 in dealer_cards and dealer_score + 10 <= 21:
            dealer_score += 10
    # Show cards and users score.
    print("\nUser has: " + str(user_cards[0]) + " - " + str(user_cards[1]) + " (Total: " + str(user_score) + ")")
    print("\nDealer has: X - " + str(dealer_cards[1]))
    # User decides to draw more cards or not.
    if user_score < 21 and user_points >= bet * 2:
        double_bet = input("\nDo you want to draw just one more card and double the bet? (y or n)")
        if double_bet == "y":
            new_card = min(10, randint(1, 13))
            user_cards += [new_card]
            user_score += new_card
            bet *= 2
            print("\nNew Card: " + str(new_card)  + "\n")
            print("User has: " + str(user_cards) + " (Total: " + str(user_score) +")\n")
        else:
            while input("\nDo you want another card? (y or n)") == "y":
                new_card = min(10, randint(1, 13))
                user_cards += [new_card]
                user_score += new_card
                print("\nNew Card: " + str(new_card)  + "\n")
                print("User has: " + str(user_cards) + " (Total: " + str(user_score) +")")
                if user_score > 21:
                    break
    else:
        while input("\nDo you want another card? (y or n)")== "y":
            new_card = min(10, randint(1, 13))
            user_cards += [new_card]
            user_score += new_card
            print("\nNew Card: " + str(new_card)  + "\n")
            print("User has: " + str(user_cards) + " (Total: " + str(user_score) +")\n")
            if user_score > 21:
                break
    # İf User choose "n" and dealer score less to user score, dealer go on draw card and if user score less dealer score, game over.
    while dealer_score < user_score:
        new_card = min(10, randint(1, 13))
        dealer_cards += [new_card]
        dealer_score += new_card
    print("\nDealer has: " + str(dealer_cards) + " (Total: " + str(dealer_score) + ")")
    # Determine winner of the round and update points.
    if user_score > 21 or (dealer_score <= 21 and dealer_score > user_score):
        print("\nDealer wins the round.")
        user_points -= bet
        dealer_points += bet
    elif dealer_score > 21 or (user_score <= 21 and user_score > dealer_score):
        print("\nUser wins the round.")
        user_points += bet
        dealer_points -= bet
    else:
         print("\nIt's a tie!")
    # Check if game is over due to lack of points.    
    if user_points <= 0:
        print("\nUser has not any points")
        print("\nGame Over\n")
        break
    if dealer_points <= 0:
        print("\nDealer has not any points")
        print("\nGame Over\n")
        break
    # Ask if player wants to continue playing.
    play_again = input("\nPress Enter to continue... (or type 'quit' to end the game)")
    round_number += 1
    # End game if player wants to quit.
    if play_again == "quit":
        print("\nGame Over\n")
        break