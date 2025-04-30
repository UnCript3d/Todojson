import json 
import os

import datetime
file = 'tryyourbest.json'
zum=[]
verify=os.path.exists(file)

if verify==False:
     with open(file,'w') as sleep:
           json.dump(zum,sleep,indent=4)
           
Progress=['Started','Done']

class TodoCLI():
     
     
     def delete():
                   
                    with open(file,'r') as kkr:
                                    pelo=(json.load(kkr))
                                    print(pelo)
                                    choice=int(input("Please Input the ID number you want to remove."))
                                    pelo=[task for task in pelo if task['id'] != choice]
                                    with open(file, 'w') as f:
                                              json.dump(pelo, f, indent=4)
                                            
                                            

                                 
                        
     def update():
             with open (file,'r') as helloi:
                     he=json.load(helloi)
                     print(he)
                     updation=(int(input('Which task will you like to remove please provide the id.')))
                    
                     

                               
                       

                     
                                     
                                     
                                     
                         
                                  
                                     
                          

                                                                       

            

     def startapp(): 
            print('****Todo CLI****')
            choice=input('1.Add a goal. \n 2.View goal. \n 3.Delete a task. \n 4.Update as done.')
            if choice =='1':
                TodoCLI.Writeanewgoal()
            elif choice =='2':
                 TodoCLI.read()
            elif choice == '3':
                 TodoCLI.delete()

            elif  choice =='4':
                    TodoCLI.update()
            else:
                 print('Please make a valid choice') 

                 
                   
    
          
                                            
     def Writeanewgoal():
                     
          
                        with open(file,'r') as z:
                               zack=json.load(z)
                               if verify==False: 
                                      lasttask=zack[-1]
                                      i=lasttask['id']+1
                               else:
                                     i=1        
                               
                               
                        Goal=input("What is your Goal?")
                        Goals={
                         'id' : 1+i,
                         'Goal': Goal,
                         'Progress':Progress[0],

                        }
                        zack.append(Goals)
                        print(zack)
                        with open (file,'w') as pum:
                               lum=json.dump(zack,pum,indent=4)
                               

     def read():
               with open(file, 'r') as hell:
                    
                    lack = json.load(hell)
                    for tasks in lack:
                            print(tasks['id'])
                            print(tasks['Goal'])
                            print(tasks['Progress'])                          
                    
                    
                  
               
                                                         
TodoCLI.startapp()
             
            

    



