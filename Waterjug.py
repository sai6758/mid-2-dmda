from collections import defaultdict
jug1=int(input("Enter the capacity of Jug1\n"))
jug2=int(input("Enter the capacity of Jug2\n"))
target=int(input("Enter the capacity to be measured within the range of Max(Jug1,Jug2)\n"))
visited=defaultdict(lambda: False)
print(visited)
def waterjugProblem(amount1,amount2):
    if(amount1==target and amount2==0) or (amount2 == target and amount1==0):
        print(amount1,amount2)
        return True
    if visited[(amount1,amount2)] ==False:
        print(amount1,amount2)
        visited[(amount1,amount2)]=True
        return (waterjugProblem(0,amount2) or
                waterjugProblem(amount1,0) or
                waterjugProblem(jug1,amount2) or
                waterjugProblem(amount1,jug2) or
                waterjugProblem(amount1 + min(amount2,(jug1-amount1)),
                amount2-min(amount2,(jug1-amount1))) or
                waterjugProblem(amount1-min(amount1,(jug2-amount2)),
                amount2+min(amount1,(jug1-amount2))))
    else:
        return False
print("Steps :")
waterjugProblem(0,0)