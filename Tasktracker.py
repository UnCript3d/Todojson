import os
import json
import datetime

file='zap.json'
Progress=['Done','In Process','Started']

def makefile():
    file='zap.json'
    path= "C:/Users/sksrd/Desktop/Programming/zap.json"
    
    isexist=os.path.exists(path)
    print(isexist)
    if isexist ==True:
        pass
    else:

        Initailize=[]
        with open (file,'w') as p:
            json.dump(Initailize,p)
            
   
def delete():
     with open (file,'r') as ram:
        ceca=json.load(ram)
        for index,n in enumerate(ceca,start=0):
            print(f"{index}: {n}")
        pig=int(input("Provide the task number that needs to be updated."))
        lub=ceca[pig]
        he=ceca.pop(pig)
        print(ceca)
     with open (file,'w') as lakshman:
         json.dump(ceca,lakshman,indent=4)
         
            


def Hellouser():
    print('Hello and welcome to Will')
    Choice=input("You can press 1 to add a new goal. \nPress 2 to change Progress of the goals.\nPress 3 to view or remove the goals.")



def update():
    with open (file,'r') as sam:
        seca=json.load(sam)
        for index,i in enumerate(seca,start=0):
            print(f"{index}: {i}")

        zig=int(input("Provide the task number that needs to be updated."))
        sub=seca[zig]
        hello=sub.pop('Progress')
        sub['Progress']='Done'
    with open(file,'w') as lolita:
        json.dump(seca,lolita,indent=4)
        
        




def addagoal():
    goal=input("What goal do you have?")
    jsonn={"Goal":goal,
           'Progress':Progress[2],
           
           }
    
    with open(file,'r') as pop:
        swag=json.load(pop)
        swag.append(jsonn)
        print(swag)
    
    with open (file,'w') as peep:
        json.dump(swag,peep,indent=4)

delete()    







