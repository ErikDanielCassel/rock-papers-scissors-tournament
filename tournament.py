import player1
import player2

#rock = 0
#paper = 1
#scissor = 2


choose1 = player1.choose()
choose2 = player2.choose()

def who_wins(first, second):
    dif = (first - second + 1)%3
    return dif
    # 0 means secondplayer won, 1 means tie, 2 means firstplayer won

print(who_wins(1,2))