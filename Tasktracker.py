import json 
file ='tryyourbest.json'

class TodoCLI():
         
         def storage():
                  Goal=input('What is your Goal?')
                  Progress="in progress"
                  
                  Final={
                        'Goal':Goal,
                        'Progress':Progress
                  }                  
                  with open(file,'r') as ff:
                        filedata=json.load(ff)
                        filedata=[]
                        filedata.append(Final)

                  with open(file,'w') as storage:
                        json.dump(Final,storage,indent=4)

                        
                  
        
         def view():
               with open(file,'r') as f:
                     data=json.loads(f)
                     print(data)

            
               
         

         

                

         
         
         
      
             
        
        
        

        
         def startapp(): 
            print('****Todo CLI****')
            choice=input('1.Add a goal. \n 2.View goal. \n 3.Remove goal.\n 4.Mark goal as done or not.')
            if choice =='1':
                TodoCLI.storage()
            elif choice =='2':
                 TodoCLI.view()
            elif choice == '3':
                 print('')
            elif choice == '4':
                 print("")
            else:
                 print('Please make a valid choice')   

       
                  
TodoCLI.startapp()
             
            

    



