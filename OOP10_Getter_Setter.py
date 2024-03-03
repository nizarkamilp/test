class Hero:

    def __init__(self, name, health, armor):
        self.name = name
        self.__health = health
        self.__armor = armor
        #self.info = "name {} : \n\thealth: {}".format(self.name,self.__health)
    
    @property #bisa rubah si method menjadi varibale
    def info(self): #method menjadi variable >> variable akan berubah terus
        return "name {} : \n\thealth: {}".format(self.name,self.__health)
    
    @property
    def armor(self):
        pass

    @armor.getter
    def armor(self):
        return self.__armor
    
    @armor.setter
    def armor(self,input):
        self.__armor = input

    #@amor.deleter
    #def armor(self):
    #    self.__armor = None


sniper = Hero('sniper',100,10)

print('merubah info')
print(sniper.info)
sniper.name = "dadang"
print(sniper.info)

print('getter dan setter untuk __armor:')
print(sniper.armor)
sniper.armor = 50
print(sniper.armor)