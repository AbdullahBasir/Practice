from getpass import getpass as choose

def rock_paper(rock, paper, scissors):

    pl1score = 0
    pl2score = 0
    q = True

    while q == True:

        pl_1 = choose("\nPlayer 1's turn: input r for rock, p for paper and s for scissors: ").lower()
        pl_2 = choose("\nPlayer 2's turn: input r for rock, p for paper and s for scissors: ").lower()

        if pl_1 not in (rock, paper, scissors) or pl_2 not in (rock, paper, scissors):
            print("Bad input, The options are: 'r' for rock, 'p' for paper and 's' for scissors")
            continue
        elif pl_1 == pl_2:
            print("\nIts a tie!!!")
        elif (pl_1  == rock and pl_2 == scissors) or (pl_1  == paper and pl_2 == rock) or (pl_1  == scissors and pl_2 == paper):
            pl1score += 1
            print(f"\nPlayer 1 won the round, the score is {pl1score}")
        else:
            pl2score += 1
            print(f"\nPlayer 2 won the round, the score is {pl2score}")

        if pl1score == 5:
            print(f"\nTotal scores: Player 1 = {pl1score}: Player 2 = {pl2score}, Player 1 is the winner!\n")
            q = False
        elif pl2score == 5:
            print(f"\nTotal scores: Player 1 = {pl1score}: Player 2 = {pl2score}, Player 2 is the winner!\n")
            q = False

rock_paper('r', 'p', 's')
