class whatsappV1:
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp - v1 {self.name}!")
    def messaging(self):
        print("You can send messages")
        
class whatsappV2(whatsappV1):
    def __init__(self,name):
        self.name=name
        print(f"Welcome to the whatsapp - v2 {self.name}!")
    def calls(self):
        print("You can do audio and video calls")
        
moksha=whatsappV1("Mokshagna")
moksha.messaging()
bala=whatsappV2("Bala Sai")
bala.messaging()
bala.calls()