class Mobile:
    mobile_type = "touch screen"  # Class variable    

    def __init__(self,brand,model,color,year):
        self.brand = brand  # Instance variable
        self.model = model
        self.color = color
        self.year = year
    

    def specs(self):
        print("The mobile brand is: " +self.brand)
        print("The mobile model name is: " +self.model)
        print("The color of the model is: "+self.color)
        print("The mobile was manufactured in: "+str(self.year))
        print(f"This is a {self.mobile_type} mobile")

    def calling(self):
        print("The " +str(self.model)+ " can make phone calls.")

    def messages(self):
        print("The " +str(self.model) +" can send messages.")

    def email(self):
        print("The " +str(self.model) + " can send emails")

    def gaming(self):
        print("You can play games on " +str(self.model))    
        
    