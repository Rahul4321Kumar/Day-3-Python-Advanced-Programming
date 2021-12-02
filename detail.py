import csv

def create():
    with open("detail.csv","w") as obj:
        fobj=csv.writer(obj)
        fobj.writerow(["Product-Name", "Product-CostPrice","Product-SalesTax","Product-FinalPrice","Country"])
        sum=0
        while True:
            ProductName=input("Enter Product-Name:-")
            ProductCostPrice=int(input("Enter Product-CostPrice:-"))
            Country=input("Enter Country Name:-")
            Number=0.20
            ProductSalesTax= "{:.0%}".format(Number)
            print(type(ProductSalesTax))
            sum=ProductCostPrice*Number
            ProductFinalPrice=sum+ProductCostPrice
            record=[ProductName, ProductCostPrice,ProductSalesTax,ProductFinalPrice,Country]
            fobj.writerow(record)
            ch=int(input("1-EnterMore \n 2-Exit \n Enter Yput choice:"))
            if(ch==2):
                break


create()

  
    