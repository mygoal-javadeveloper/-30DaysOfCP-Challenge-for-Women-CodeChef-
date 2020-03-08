def selection(num):
    winner=''
    counter=0
    tempnum=num
    while tempnum>=2:
        for z in range(2,(num+1)):
            if (tempnum % z == 0):
                counter+=1
                tempnum = tempnum//z
                break
            else:
                continue
        if (counter%2 == 0):
            winner= 'Tanya'
        elif(counter%2 != 0):
            winner = 'Divesh'    
    return winner   
    

try:
    testcases = int(input())
    lst = []
    for x in range(testcases):
        num = int(input())
        lst.append(num)
    for y in lst:
        print(selection(y))   
except Exception as e:
    pass


'''
Tanya and Divesh once took part in a team programming competition where they had a team of three members.
The third member of their team (let's call this person as X for simplicity) is the reason why they're fighting with each other today.
There is another team programming competition coming up where programmers can take part in a team of two.
Now both of them want to team up with X for this upcoming team programming contest.
So both of them have mutually decided to conduct a Selection Battle, whoever wins this will team up with X.
Initially they have an integer N.

The rules are as follows:

Both players alternate turns, Tanya makes the first move.
In each turn (move), a player can choose an integer K (2≤K≤N and NmodK≡0) and set N=N/K.
A move after which no other legal move can be made is called as the last move. The player who makes the last move loses.
Assume that both players play optimally.

Input:
The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
The first and the only line of each test case contains an integer N.
Output:
For each test case print a single line containing Tanya if Tanya wins, else Divesh.

Sample Input:
2
14
2
Sample Output:
Tanya
Divesh
'''
