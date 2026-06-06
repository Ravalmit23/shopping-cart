class shopping_cart:
    def __init__(self):
        self.items=[]
    def menu(self):
        while(True):
            print('''
            PRESS 1:ADD ITEMS
            PRESS 2:REMOVE ITEM
            PRESS 3:TOTAL BILL
            PRESS 4:EXIT
                  ''')
            choice=int(input("enter your choice:-"))
            if choice==1:
                self.add_item()
            elif choice==2:
                self.remove_item()
            elif choice==3:
                self.total_bill()
            else:
                exit()
                break
    def add_item(self):
        item=input("enter product name=")
        price=int(input("enter price of product="))
        detail=(item,price)
        self.items.append(detail)
        print(self.items)

    def remove_item(self):
        name=input("enter name of product to remove=")
        for i in self.items:
            if i[0]==name:
                self.items.remove(i)
                print("product remove",i)
                print("after deletion your product list",self.items)
            else:
                print("no items found")
    def total_bill(self):
        total=0
        for i in self.items:
            total+=i[1]
            print("your total bill=",total)
        print('your cart is empty')

    
            


s1=shopping_cart()
s1.menu()