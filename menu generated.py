import pickle
with open("menu.dat" , "wb") as m:
    while True:
        print("WELCOME TO THE MENU GENERATED PROGRAM!!!!")
        print("\n 1. CREATE RECORD")
        print(" 2. ADD RECORD")
        print(" 3. UPDATE RECORD")
        print(" 4. SEARCH RECORD")
        print(" 5. DELETE RECORD")
        ch = int(input("WHAT DO YOU WANNA DO: "))
        if ch == 1:
            def create():
                
                while True:
                    d = {}
                    roll = int((input("ENTER THE ROLL. NO. : ")))
                    name = input("ENTER THE NAME: ")
                    per = float(input("ENTER THE PERCENTAGE: "))
                    d[roll] = {}
                    d[roll]['NAME'] = [name]
                    d[roll]['PERCENTAGE'] = [per]
                    pickle.dump(d,m)
                    c= input(" WANNA ADD MORE RECORDS : ")
                    if c == 'n':
                        break
            create()
            
        elif ch == 2:
            def add():
                d = {}
                roll = int((input("ENTER THE ROLL. NO. : ")))
                name = input("ENTER THE NAME: ")
                per = float(input("ENTER THE PERCENTAGE: "))
                d[roll] = {}
                d[roll]['NAME'] = [name]
                d[roll]['PERCENTAGE'] = [per]
                pickle.dump(d,m)
            add()

    
        elif ch == 3:
            def upi():
                d= {}
                r = int(input("ENTER ROLL NO. YOU WWANNA UPDATE: "))
                for i in d:
                    if r in d:
                        print(r)
            
            upi()
              
                                
            
       
       
            
        
                
               
    
