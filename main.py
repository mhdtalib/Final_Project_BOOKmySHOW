class movie_ticket:
    def __init__(self,row,col,name,gender,age,phno,price):
        self.row = row
        self.col = col
        self.name = name
        self.gender = gender
        self.age = age
        self.phno = phno
        self.price = price
    def __repr__(self):
        return ("name = "+str(self.name)+
        '\ngender = '+str(self.gender)+
        '\nage = '+str(self.age)+
        '\nphno = '+str(self.phno)+
        '\nprice = '+str(self.price))
        
        
all_tickets = {
    'reg':[],
    'no':0,
    'per':0,
    'curr_inc':0,
    'tot_inc':0
}

def showseats():
    max_row = int(all_tickets['max_rows'])
    max_col = int(all_tickets['max_cols'])
    matrix = [['S' for j in range(max_col)]for i in range(max_row)]
    for booked in all_tickets['reg']:
        matrix[booked.row-1][booked.col-1]= 'B'
    print(' ',end='')
    for i in range(max_col):
        print(i+1,end='') 
    print()
    for i in range(max_row):
        print(i+1,end='')
        for j in range(max_col):
            print(matrix[i][j],end='')
        print()
        
def isBooked(row,col):
    for i in all_tickets['reg']:
        if i.row==row and i.col==col:
            return True
        else:
            return False
def book_ticket():
    row = int(input('Enter the row:  '))
    col = int(input('Enter the column:  '))
    name = input('Enter your name:  ')
    gender = input('Enter your gender:  ')
    age = input('Enter your age:  ')
    phno = input('Enter your phone number:  ')
    
    max_row = int(all_tickets['max_rows'])
    max_col = int(all_tickets['max_cols'])
    
    if row<=max_row and col<=max_col and not isBooked(row,col):
#         print(max_row/2)
#         print(max_row*max_col>60 and row>int(max_row/2))
        if max_row*max_col>60 and row>int(max_row/2):
            price = 8
        else:
            price = 10
        all_tickets['curr_inc']=all_tickets['curr_inc']+price
        all_tickets['no']=all_tickets['no']+1
        all_tickets['per']= all_tickets['no']/(max_row*max_col) *100
        new_movie_ticket = movie_ticket(row,col,name,gender,age,phno,price)
        all_tickets['reg'].append(new_movie_ticket)
    else:
        print('enter a valid seat')
        
def details():
    row = int(input('Enter the row:  '))
    col = int(input('Enter the column:  '))
    for i in all_tickets['reg']:
        if i.row==row and i.col==col:
            print(i)
        else:
            print('not booked')
def statistics():
    print("No of purchased tickets  :"+str(all_tickets['no']))
    print("Percentage  :"+str(all_tickets['per']))
    print("Current Income  :"+str(all_tickets['curr_inc']))
    print("Total income  :"+str(all_tickets['tot_inc']))
        
if __name__=='__main__':
    max_rows = int(input('Enter number of rows:  '))
    max_cols = int(input('Enter number of columns:  '))
    all_tickets['max_rows'] = max_rows
    all_tickets['max_cols'] = max_cols
    if max_rows*max_cols>60:
        total_income = int(max_rows/2)*max_cols*10 + (max_rows-int(max_rows/2))*max_cols*8
    else:
        total_income = max_rows*max_cols*10
    all_tickets['tot_inc'] = total_income
    while(True):
        print(" 1.Show the seats\n",
            "2.Buy a ticket\n"
            ,"3.Statistcs\n",
            "4.Show booked Tickets User Info\n","0.Exit")
        choice=int(input())
        if(choice==1):
            showseats()
        elif(choice==2):
            book_ticket()
        elif(choice==3):
            statistics()
        elif(choice==4):
            details()
        elif(choice==0):
            break
        else:
            print('invalid option')
            continue