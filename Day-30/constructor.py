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

harish=flipkart()
harish.userinfo('Harish',8985778574,'Che')
harish.displaydiscount()
harish.display()
print(harish.products)
print(harish.name)

flipkart.displaydiscount()
flipkart.display()
print(flipkart.products)

class flipkart:
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        print(f'Hello {self.name}, Welcome to the Flipkart')
moksha=flipkart('Mokshagna',7894561230)
bala=flipkart('Bala sai',9876543210)

class instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self.__posts=[]
        
    def getpassword(self):
        return self.__password
    
    @property
    def accesspost(self):
        return self.__posts
    
    def display(self):
        print(self.username,self.__password,self.__posts)
        
moksha=instagram('Moksha','Moksha123')
moksha.display()

#---Encapsulation---
class instagram:
    def __init__(self,username,password):
        self.username=username
        self.__password=password
        self.__posts=[]
        
    def getpassword(self):
        return self.__password
    
    def setpassword(self,newpassword):
        self.__password=newpassword
    
    @property
    def accesspost(self):
        return self.__posts
    
    @accesspost.setter
    def accesspost(self,newpost):
        self.__posts.append(newpost)
        
    def display(self):
        print(self.username,self.__password,self.__posts)
        
moksha=instagram('Moksha','Moksha123')
moksha.display()
bala=instagram('Bala Sai','Bala234')
print(moksha.username)
print(moksha.getpassword())
print(moksha.accesspost)

bala.username='Bala Sai'
bala.setpassword('bala@789')
bala.accesspost='sunrise.png'
bala.accesspost='beach.png'

print(bala.username)
print(bala.getpassword())
print(bala.accesspost)