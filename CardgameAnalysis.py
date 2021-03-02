#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import lines

# Our Two-Sample Z Test statistic for a normal distributions
# avg: H_0 avg
# std: H_0 stdev
# n: number of games played in cheating games
# M: H_1 avg
def zTest (avg0, avg1, std0, std1, n0, n1):
    zVal = (avg0 - avg1)/math.sqrt((std0**2/n0)+(std1**2/n1))
    return zVal

# main function for our coin toss Python code
if __name__ == "__main__":
    # not making any assumptions about what is provided by user
    haveH0 = False
    haveH1 = False
    
    # default gimme
    gimme = 0
    
    # default number of cards
    Ncards = 80
    
    # available options for user input
    if '-input0' in sys.argv:
        p = sys.argv.index('-input0')
        InputFile0 = sys.argv[p+1]
        haveH0 = True
    if '-input1' in sys.argv:
        p = sys.argv.index('-input1')
        InputFile1 = sys.argv[p+1]
        haveH1 = True
    if '-gimme' in sys.argv:
        p = sys.argv.index('-gimme')
        gm = int(sys.argv[p+1])
        if gm >= 0 and gm < Ncards+1:
            gimme = gm
    if '-Ncards' in sys.argv:
        p = sys.argv.index('-Ncards')
        nc = int(sys.argv[p+1])
        if (nc % 2) == 0:
            Ncards = nc
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv or not haveH0:
        print ("Usage: %s [options]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print ("   -input0 [filename]  name of file for H0 data")
        print ("   -input1 [filename]  name of file for H1 data")
        print ("   -Ncards [number]    number of cards in deck")
        print ("   -gimme [number]     number of cards used to cheat")
        sys.exit(1)
    
    # gives ratio of games that will definitely win when cheated
    willwin = gimme/(Ncards//2)
    
    # These are probabilities of winning each play
    # p0 is always fair 50/50, p1 is a modified probability based on willwin
    p0 = .5
    p1 = 1*willwin + .5*(1-willwin)
    
    Outcome0 = []
    Outcome1 = []

    Outcome_min = 1e8
    Outcome_max = -1e8    
    
    # Takes values from input0 and sorts into list Outcome0 
    with open(InputFile0) as games:
        for game in games:
            gameVals = game.split()
            Outcome = 0
            for val in gameVals:
                Outcome += float(val)
                    
            if Outcome < Outcome_min:
                Outcome_min = Outcome
            if Outcome > Outcome_max:
                Outcome_max = Outcome
            Outcome0.append(Outcome)
            
            # Gets max, min, avg, and stdev of data. Also determines optimal
            # bin width for plotting
            Outcome0max = max(Outcome0)
            Outcome0min = min(Outcome0)
            binwidth0 = int(Outcome0max) - int(Outcome0min)
            avg0 = np.mean(Outcome0)
            std0 = np.std(Outcome0)
            std0p = avg0 + std0
            std0m = avg0 - std0
          
            # Takes values from input1 and sorts into list Outcome1              
    if haveH1:
            with open(InputFile1) as games:
                for game in games:
                    gameVals = game.split()
                    Outcome = 0
                    for val in gameVals:
                        Outcome += float(val)
                        
                    if Outcome < Outcome_min:
                        Outcome_min = Outcome
                    if Outcome > Outcome_max:
                        Outcome_max = Outcome
                    Outcome1.append(Outcome)    
                    
                    # Gets max, min, avg, and stdev of data. Also determines optimal
                    # bin width for plotting
                    Outcome1max = max(Outcome1)
                    Outcome1min = min(Outcome1)
                    binwidth1 = int(Outcome1max) - int(Outcome1min)
                    avg1 = np.mean(Outcome1)
                    std1 = np.std(Outcome1)
                    std1p = avg1 + std1
                    std1m = avg1 - std1
                    
    count0 = len(open(InputFile0).readlines(  ))
    count1 = len(open(InputFile1).readlines(  ))
                    
    zVal = zTest(avg0, avg1, std0, std1, count0, count1)
    # print(zVal)
                    
# Creating our plot
    title = str(Ncards) +  " card deck with " + str(gimme) + " cheater cards, Z = " + str(round(zVal,2))
                
    # make figure
    plt.figure()
    plt.hist(Outcome0, binwidth0, density=True, facecolor='deepskyblue',
             alpha=0.5, align = 'left', label="$\\mathbb{H}_0$")
    if haveH1: 
        plt.hist(Outcome1, binwidth1, density=True, facecolor='salmon',
                 alpha=0.7, align = 'left', label="$\\mathbb{H}_1$")
    
    # Adds vertical lines for average and standard deviation
    min_ylim, max_ylim = plt.ylim()
    
    plt.axvline(avg0, color = 'darkblue', linewidth = 2,
                label = '$\\mu_0$ = {:.1f}'.format(avg0))
    plt.axvline(std0p, color = 'darkblue', linestyle = '--',
                label = '$\\pm\\sigma_0$ = {:.1f}'.format(std0))
    plt.axvline(std0m, color = 'darkblue', linestyle = '--')
    
    plt.axvline(avg1, color = 'darkred', linewidth = 2,
                label = '$\\mu_1$ = {:.1f}'.format(avg1))  
    plt.axvline(std1p, color = 'darkred', linestyle = '--',
                label = '$\\pm\\sigma_1$ = {:.1f}'.format(std1))
    plt.axvline(std1m, color = 'darkred', linestyle = '--')
      
    plt.xlabel('$N_{wins}$ per game')
    plt.ylabel('Probability')
    plt.legend(loc = 2)
    plt.xlim(-.5 , Ncards/2+.5)
    plt.tick_params(axis='both')
    plt.title(title)
    plt.grid(True)

    plt.show()
    
# Plot that shows Z value