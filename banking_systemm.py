# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 18:04:49 2022

@author: Zainy
"""

class Customer:
    def __init__(self, password, name, address, accounts):
        self.__name = name
        self.__address = address
        self.__accounts = accounts
        self.__password = password
        
        self.current_accounts = accounts
        
    def get_password(self):
        return self.__password
    def get_name(self):
        return self.__name
    def get_address(self):
        return self.__address    
    def set_password(self, password):
        self.__password = password
    def set_name(self, name):
        self.__name = name
    def set_address(self, addr):
        self.__address = addr
        
        
class Admin:
    def __init__(self, password, name):
        self.__password = password
        self.__name = name
        
    def get_name(self):
        return self.__name
    def get_password(self):
        return self.__password
    def set_name(self, name):
        self.__name = name
    def set_password(self, password):
        self.__password = password
        
    
class Account:
      def __init__(self, aT, balance, overdraft, interest):
          self.__AccountType = aT
          self.__balance = balance
          self.__overdraft = overdraft
          self.__interest = interest
         
      def withdraw(self, balance):
          self.__balance -= balance
      def deposit(self, balance):
          self.__balance += balance
      def get_account_type(self):
          return self.__AccountType
      def get_account_balance(self):
          return self.__balance
   
class BankingSystem():
    user_list = {"Boris": "ABC", "Chloe": "1+x", "David": "aBC"}
    admin_list = {"Arthur": "123"}
    
    users = {"Boris": Customer("b123", "Boris", "10 London Road", 
                               [Account("Current Account", 1000, 100, 0.0)]),
             "Chloe": Customer("c123", "Chloe", "99 Queens Road",
                               [Account("Current Account", 1000, 100, 0.0),
                                Account("Saving Account", 4000, 0, 2.99)]),
             "David": Customer("1+x", "Chloe", "2 Birmingham Street", 
                               [Account("Saving Account 1", 200, 0, 0.99),
                                "Saving Account 2", 4000, 0, 4.99])}
    users123 = [['Boris', "10 London Road", "Current Account, £1000, Over draft limit £100,"],
                ["Chloe","99 Queens Road","Current Account £1000, Over draft limit £100", "Saving Account, £4000, Intrest Rate £2.99"],
                ["David","2 Birmingham Street","Saving Account 1, £200, Intrest rate 0.99%","Saving Account 2, £4000, Intrest rate 4.99%"]
                ]
    money = [1000,5000,5200]
                
                
    def __init__(self):
        pass
        
        
        
    

    def login(self):
        uname = input("Enter Username: ")
        pword = input("Enter Password: ")
        if uname in self.user_list:
            actual_password = self.user_list[uname]
            if pword == actual_password:
                self.current_user = uname
                self.display_menu_customer()
            else:
                print("Password is Incorrect.")
        if uname in self.admin_list:
            actual_password1 = self.admin_list[uname]
            if pword == actual_password1:
                self.current_user = uname
                self.display_menu_admin()
            else: 
                print("Password is Incorrect.")
           
        
        


    def display_menu_customer(self):
        print("Please select an option: ")
        print("1 - View account")
        print("2 - View summary")
        print("3 - Quit")
        select_option1 = int(input("Enter a number to select your option: "))
        if select_option1 == 1:
            self.view_account()
        elif select_option1 == 2:
            self.view_summary()
        elif select_option1 == 3:
            return
        else:
            print("PLease select a Valid option!")
            
    def view_account(self):
        print("--Account list--")
        print("Please select an option: ")
        for i in range(len(self.users[self.current_user].current_accounts)):
            print('  ' + str(i+1) + " - " + str(self.users[self.current_user].current_accounts[i].get_account_type()) +': ' +'£'+
                  str(self.users[self.current_user].current_accounts[i].get_account_balance()))
        inp = int(input('Enter a number to select your option: '))
        if inp <= 1:
            print('You selected ' + str(i+1) + ' - ' +  str(self.users[self.current_user].current_accounts[i].get_account_type())
              + ' £'+ str(self.users[self.current_user].current_accounts[i].get_account_balance()) + '.')
        elif inp > 1:
            print(print('You selected ' + str(i+1) + ' - ' +  str(self.users[self.current_user].current_accounts[i].get_account_type())
                 + ' £'+ str(self.users[self.current_user].current_accounts[i].get_account_balance()) + '.'))
                
            
            
        print('Please select an option: ')
        print('  1 - Deposit')
        print('  2 - Withdraw')
        print('  3 - Go back')
        x = int(input('Enter a number to select your option: ' ))
        if x == 1:
            amount = int(input('Enter amount to deposit: '))
            y = int(self.users[self.current_user].current_accounts[i].get_account_balance())
            y += amount
            print(str(amount) + ' Has succesfully been deposited')
            self.view_account()
        elif x == 2:
            amount = int(input('Enter amount to Withdraw: '))
            self.users[self.current_user].current_accounts[i].get_account_balance() == self.users[self.current_user].current_accounts[i].get_account_balance() - amount
            print(str(amount) + ' Has succesfully been Withdrawn')
            self.view_account()
        elif x == 3:
            self.view_account()
      
                
                
    
    
        
        
            
            
            
    def view_summary(self):
        x=0
        count = 0
        print("--Summary--")
        for i in range(len(self.users[self.current_user].current_accounts)):
            count +=1
        for i in range(len(self.users[self.current_user].current_accounts)):
            
            x += self.users[self.current_user].current_accounts[i].get_account_balance()
        print('  1 - ' + ' Total accounts with bank: '+  str(count))
        print( '  2 - ' + ' Total in all accounts: '+ '£'+ str(x))
        
       
        
            
        
            
        
    
        
    def run_app(self):
        self.current_user = None
        self.login()
        
        
        
    def display_menu_admin(self):
        print("Please select an option:")
        print("1 - Customer Summary")
        print("2 - Financial Forecast")
        print("3 - Transfer Money - GUI")
        print("4 - Account management - GUI")
        select_option2 = int(input("Enter a number to select your option: "))
        
        if select_option2 ==1:
           self.customer_summary()
        elif select_option2 ==2:
            self.financial_forecast()
        else:
            print("Please Select a Valid option. ")
        
    def customer_summary(self):
        print(' Customer Summary')
        for x in BankingSystem().users123:
            print(x)
    
    def financial_forecast(self):
        print('Financial Forecast')
        count = 0
        for x in BankingSystem().users123:
            print(x[0])
            if len(x) == 3:
                print('1 account in bank')
                print('Money in bank: ',BankingSystem().money[count])
                count += 1
            elif len(x) == 4:
                print('2 accounts in bank')
                print('Money in bank: ',BankingSystem().money[count])
                count += 1
            
            
            
        
            
    
            
        
        