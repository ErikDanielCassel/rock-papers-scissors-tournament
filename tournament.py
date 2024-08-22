import player1
import player2

#rock = 0
#paper = 1
#scissor = 2



def who_wins(first, second):
    return (first - second + 1)%3 - 1
    
    # -1 means secondplayer won, 0 means tie, 1 means firstplayer won

def match(number_of_rounds):
    score = 0
    score1 = 0
    score2 = 0
    i = 0
    while i < number_of_rounds:
        round_winner = None
        choose1 = player1.choose(round_winner)
        choose2 = player2.choose(round_winner)
    
        round_winner = who_wins(choose1, choose2)
        score += round_winner
        score1 += max(round_winner, 0)
        score2 -= min(round_winner, 0) 
        i += 1