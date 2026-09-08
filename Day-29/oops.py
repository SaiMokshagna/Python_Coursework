class flipkart:
    products={'Shirts':1000,'Handbag':2000,'Pants':3000}
    discount=30
    
    @classmethod
    def display(cls):
        print(cls.products)
        
    def userinfo(self,name,phone,address):
        self.name=name
        self.phone=phone
        self.address=address
        print(f"Hello {self.name}, Welcome to the Flipkart")
        
    @staticmethod
    def displaydiscount():
        print(f"{flipkart.discount}% discount is going on, grab the products....")
    
moksha=flipkart()
moksha.userinfo('Moksha',8985718795,'Mrk')
moksha.displaydiscount()
moksha.display()

bala=flipkart()
bala.userinfo('Bala Sai', 8985718896,'Hyd')
bala.displaydiscount()
bala.display()

harish=flipkart()
harish.userinfo('Harish',8985778574,'Che')
harish.displaydiscount()
harish.display()