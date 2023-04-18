import sys
import random

class Bank:
    def __init__(self):
        self.client_details_list = []
        self.access = False
        self.cash = 100


    def register(self, name , ph , password, gender, age, address, num_acc, gmail):      # đăng ký  1
        cash = self.cash
        contitions = True
        
        num_acc = []
        numb1 = random.sample(range(0,9),4)
        numb2 = random.sample(range(0,9),4) 
        num_acc.append(numb1)
        num_acc.append(numb2)
        
        if len(str(ph)) ==  9:
            contitions = True
        else:
            ph = int(input("Invalid Phone number ! please enter 10 digit number\nEnter Phone Number: "))

        if len(str(password)) <= 18:
            contitions = True 
        else:
            password = input("Enter password less than 18 character\nEnter password: ")
        
        if contitions == True:
            print("========================")
            print("Account created successfully")
            print("Client's Account is: ", num_acc)
            print("========================")
            self.client_details_list = [name , ph , cash, password , num_acc, gmail, gender, age, address]
            with open(f"{name}.txt","w") as f:
                for details in self.client_details_list:
                    f.write(str(details)+"\n")

    def Access(self, name , ph):   # truy cập 2
        with open(f"{name}.txt","r") as f:
            details = f.read()
            self.client_details_list = details.split("\n")
            if str(ph) in str(self.client_details_list):
                self.access = True

            if self.access == True:
                print(f"access {name} infomation ")
                self.cash = int(self.client_details_list[2])
                self.name = name
            
            else:
                print("Wrong details")
    
    def add_cash(self, amount):   # thêm tiền mục 2.1
        if amount > 0:
            self.cash += amount
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
            
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(self.cash)))

            print("Amount added successfully")

        else:
            print("Enter correct value of amount")
    
    def withdraw (self, amount):  # rút tiền mục 2.2
        if amount > 0:
            self.cash -= amount 
            with open(f"{name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")
                
            with open(f"{name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[2]),str(self.cash)))
            
            print("Withdraw successfully")
        else:
            print("Enter correct value of amount")
            
                
    def password_change(self, password):   # đổi mk 2.3
        print(password)
        if len(password) >  18:
            password = input("Enter password less than 18 character\nEnter password: ")
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[3]),str(password)))
            print("new Password set up successfully")
                  
    def ph_change(self , ph):   # đổi sđt 2.3
        print("0",ph)        
        if len(str(ph)) !=  9:
            ph = int(input("Invalid Phone number ! please enter 10 digit number\nEnter Phone Number: "))
        else:
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[1]),str(ph))) 
            print("new Phone number set up successfully")
            print("0",ph)  
    
    def gmail_change(self , gmail):   # đổi gmail 2.3
            print(gmail)
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[5]),str(gmail)))
            print("new Gmail account set up successfully")
            print(gmail)
    
    def add_change(self , address):# đổi dc 2.3
            print(address)
            with open(f"{self.name}.txt","r") as f:
                details = f.read()
                self.client_details_list = details.split("\n")

            with open(f"{self.name}.txt","w") as f:
                f.write(details.replace(str(self.client_details_list[5]),str(address)))   
            print("new Address set up successfully")
            print(address) 
                
                               
if __name__ == "__main__":
    Bank_object = Bank()
    print("Client information management system")
    print("1.Access Client Information")  #1
    print("2.Create New Client information")   #2
    print("3.Exit")
    Admin = int(input("Make decision: "))

    if Admin == 1:
        print("Enter Client Information to Access")
        name = input("Enter Name: ")
        ph = int(input("Enter Phone Number: "))
        Bank_object.Access(name, ph)
        while True:
            if Bank_object.access:
                print("========================")
                print("Name: ",Bank_object.name,"    Age:",Bank_object.client_details_list[7],"    Gender: ",Bank_object.client_details_list[6])
                print("Account Number: ",Bank_object.client_details_list[4])
                print("Balacne:",Bank_object.cash)
                print("========================")
                print("1.Add amount")  #2.1
                print("2.Withdraw ") #2.2
                print("3.Edit profile")#2.3
                print("4.Exit") #2.4
                Admin_acces = int(input())
                if Admin_acces == 1:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.add_cash(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                
                elif Admin_acces == 2:
                    print("Balance =",Bank_object.cash)
                    amount = int(input("Enter amount: "))
                    Bank_object.withdraw(amount)
                    print("\n1.back menu")
                    print("2.Logout")
                    choose = int(input())
                    if choose == 1:
                        continue
                    elif choose == 2:
                        break
                    
                elif Admin_acces == 3:
                    print("1.Change Password")
                    print("2.Change Phone Number")
                    print("3.Change Gmail account")
                    print("4.Change Address ")
                    print("5.back menu ")
                    edit_profile = int(input())
                    if edit_profile == 1:
                        new_passwrod = input("Enter new Password: ")
                        Bank_object.password_change(new_passwrod)
                        print("\n1.back menu")
                        print("2.Exit")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 2:
                        new_ph = int(input("Enter new Phone Number: "))
                        Bank_object.ph_change(new_ph)
                        print("\n1.back menu")
                        print("2.Exit")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 3:
                        new_gm = input("Enter new Gmail account: ")
                        Bank_object.gmail_change(new_gm)
                        print("\n1.back menu")
                        print("2.Exit")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break    
                    elif edit_profile == 4:
                        new_add = input("Enter new Address: ")
                        Bank_object.gmail_change(new_add)
                        print("\n1.back menu")
                        print("2.Exit")
                        choose = int(input())
                        if choose == 1:
                            continue
                        elif choose == 2:
                            break
                    elif edit_profile == 5:        
                        continue
                    
                elif Admin_acces == 4 :
                    break
                        
                
    if Admin == 2:   # đăng ký
        print("========================")
        print("Create new client information")
        name = input("Enter Name: ")
        gmail = input("Gmail: ")
        password = input("Enter password: ")
        age = int(input("Age: "))
        ph = int(input("Enter Phone Number: "))
        gender = input("1.Male/ 2.Female\n")
        address = input("Enter client's address: ")
        num_acc = print("")
        Bank_object.register(name, ph, password, gender, age, address, num_acc, gmail)
       
    if Admin == 3:
        sys.exit(0)