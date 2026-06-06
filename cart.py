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
                pass
            elif choice==3:
                pass
            else:
                exit()
                break
    def add_item(self):
        item=input("enter product name=")
        price=int(input("enter price of product="))
        detail=(item,price)
        self.items.append(detail)
        print(self.items)


s1=shopping_cart()
s1.menu()