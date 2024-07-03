import random
chairman = []
def vote():
    num = int(input("Enter number student chairman : ")) 
    return(num)
def rnchair(): 
    for i in range(500):
        ran = random.randint(0,num)
        chairman.append(ran)
    notVote= chairman.count(0)
    return(notVote)

def display(notVote):
    print(f'''Number of right student : 500
Number of Vote : {500-notVote} = {100-((notVote/500))*100}%
Number of not vote : {notVote} = {(notVote/500)*100}%\n''')
def show(notVote):

    print('''Result of election chairman
-----------------------------
No.\tVotes\tPercent(%)
-----------------------------''')
    votenow = 500 - notVote
    for n in range(1,num+1):
        print(f'''{n}\t{chairman.count(n)}\t{(chairman.count(n)/votenow)*100:.2f}''')
    print(f'-----------------------------\nToTal\t{500-notVote}\t100.00')

num = vote()
    
chair = rnchair()

display(chair)

show(chair)
