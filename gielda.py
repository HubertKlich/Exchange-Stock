class shopping:
    all=[[],[],[],[],[]]#ids,orders,types,prices,quantities
    count=0
    minimum=0
    maximum=0
    results=[0,0] #the best price buy, sell
    def __init__(self,id_product,order,type_product,price,quantity):
        e=locals()
        i=0
        for ele in e:
            if ele!='self':
                shopping.all[i].append(e[ele])
                i+=1
        shopping.count += 1

    def the_best_price(self):
        values=[[],[]]#buy,sell
        for ele in range(shopping.count):
            if shopping.all[1][ele]=="Buy":
                values[0].append(shopping.all[3][ele]/shopping.all[4][ele])
            else:
                values[1].append(shopping.all[3][ele]/shopping.all[4][ele])
        if values[0]: #the best price to buy
            shopping.minimum=min(values[0])
        if values[1]: #the best price to sell
            shopping.maximum=max(values[1])
    def shorter_function(ele,value,number,text):
        if shopping.all[3][ele]/shopping.all[4][ele]==value:
                if shopping.all[1][ele]==text:
                    if shopping.all[2][ele]=="Add":
                        shopping.results[number]+=shopping.all[4][ele]
                    if shopping.all[2][ele]=="Remove":
                        shopping.results[number]-=shopping.all[4][ele]

    def products_buy_sell_the_best_price(self):
        for ele in range(shopping.count):
            shopping.shorter_function(ele,shopping.minimum,0,"Buy")
            shopping.shorter_function(ele,shopping.maximum,1,"Sell")
        print("The best price of buy:",shopping.minimum,"Count of products buy in this price:",shopping.results[0])
        print("The best price of sell:",shopping.maximum,"Count of products sell in this price:",shopping.results[1])
    def wywolanie(self):
        self.the_best_price()
        self.products_buy_sell_the_best_price()
#Example
shopping("001","Buy","Add",20.0,100)
shopping("002","Sell","Add",25.0,200)
shopping("003","Buy","Add",23.0,50)
shopping("004","Buy","Add",23.0,70)
shopping("003","Buy","Remove",23.0,50)
shopping("005","Sell","Add",28,100).wywolanie()
while True:
    id_value = input("Enter value of id: ")
    order_value = input("Enter value of order[Buy/Sell]: ")
    type_value = input("Enter value of type[Add/Remove]: ")
    price_value = input("Enter value of price: ")
    quantity_value = input("Enter value of quantity: ")
    shopping(id_value,order_value,type_value,int(price_value),int(quantity_value)).wywolanie()
    exit = input("Are you want exit from loop?[Y/N]: ")
    if exit=="Y":
        break
    

