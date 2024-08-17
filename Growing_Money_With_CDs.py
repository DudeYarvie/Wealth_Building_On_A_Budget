##      Growing_Money_With_CDs.py  ##
##Author:   Jarvis Hill (hilljarvis@gmail.com)
##Date:     AUG-17-2024
##Purpose:  CDs are marketed as a low-risk way to make money but tie up liquid assets for a long time.
##          For those who have a surplus of money and can afford to let it sit and accumulate, great!
##          I was conrcerned about the middle to upper-middle class parent in today's 2024 economy. If I
##          wanted to save a large sum of money for a kid's college or retirement, etc, of course it's smart
##          to leverage compound interest.  It's also smart to deversify between, high-risk, high gain/loss
##          investments and low-risk, lower-interest, likely stable postive gain investments.
##
##          I wrote this program to see if I took an extra sum of money, say from a bank savings account that's
##          earning 1.8%, it's a money market account, and then wanted to see if I could use that surplus to
##          make money in a faster low-risk way. I wanted to answer questions like,
##              1. Does something like a CD makes sense, considering the money will be tied up/unaccessable without
##                 penalty for the duration of the CD?
##              2. Can money be made faster if I deposit in the shortest duration CD, with the lowest interest-rate, then
##                 roll it over and over and over again or depositing in longer term higher interest rate CDs?


##MAIN PROGRAM##
def main():

    ##Example inputs from user
    money_goal = 100000.00       #Total college cost
    cd_duration = 6              #Months money needs to be in a CD
    made_money = 0.00            #Money made on interest
    cd_interest_rate = .019      #CD interest rate
    months_gone_by = 0           #Months money is tied up in CD, including amt made on interest
    deposit_amount = 15000.00    #Amount initially deposited in CD
    years_gone_by = 0.00         #Years money is tied up in CD, including amt made on interest
    
    
    ##Determines how long it will take to reach money goal
    while (made_money < (money_goal-deposit_amount)):
        interest_money_made += deposit_amount*cd_interest_rate              #Money made on interest at the end of each CD duration/cycle
        deposit_amount += interest_money_made                               #Calculate the roll-over deposit amount for the next CD cycle
        months_gone_by += cd_duration                                       #Stores the total time it takes for money goal to be reached.
                                                                            #Money needs to be immediately rolled over from one CD cycle to the next. No breaks.
        print ("Interest money made in CD: $%0.2f" %interest_money_made)    #Prints the money made after each CD cycle
        print ("Total money: $%0.2f" %deposit_amount)                       #Prints the accumulated money at the end of each CD cycle    
        
        
    years_gone_by = months_gone_by/12.0                                     #Calculates how long it took to reach the money goal.    
    print("Time for money made from interest to reach college cost: %d months (%0.2f years)" %(months_gone_by,years_gone_by))
    


if __name__ == '__main__':
    main()


