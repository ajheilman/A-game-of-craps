from player import Player

def playOneGame():
    #Plays a single game and prints the results
    player = Player()
    youWin = player.play()
    print player
    if youWin:
        print "You win!\n"
    else:
        print "You lose!\n"

def playManyGames():
    #Plays a number of games and prints the statistics
    number = input("Enter the number of games: ")
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in xrange(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
        else:
            losses += 1
            lossRolls += rolls

    print "The total number of wins is", wins
    print "The total number of losses is", losses

    print "The average number of rolls per win is %0.2f" % (float(winRolls) / wins)
    print "The average number of rolls per loss is %0.2f" % (float(lossRolls) / wins)
    print "The winning percentage is %0.3f" % (float(wins) / number)



def main():
    playOneGame()
    playManyGames()
    
main()
