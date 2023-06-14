class Ninja():
    def __init__(self, nombre, apellido, mascotas, premio, comida_mascota):
        self.nombre=nombre
        self.apellido=apellido
        self.mascotas=mascotas
        self.premio=premio
        self.comida_mascota=comida_mascota
        self.mascota=Mascota('name','tipo','golosina',salud=0, energia=0)

    def caminar(self):
        print(f"{self.nombre} {self.apellido} trae a su mascota para jugar ...")
        self.mascota.jugar()
        

    def alimentar(self):
        print(f"{self.nombre} {self.apellido} llama a su mascota a comer ...")
        self.mascota.comer()

    def bañar(self):
        print(f"{self.nombre} trae a su mascota para bañarla...")
        self.mascota.sonido()
        
class Mascota():
    def __init__(self, name, tipo, golosinas, salud, energia):
        self.name=name
        self.tipo=tipo
        self.golosinas=golosinas
        self.salud=salud
        self.energia=energia
        
    
    def dormir(self):
        self.energia+=25
        
    def comer(self):
        print(f"{self.name} esta comiendo! su energía aumento en 5 y su salud aumento en 10!")
                
    def jugar(self):
        print(f"{self.name} esta jugando!  su salud aumento en 5!")
        
    def sonido(self):
        print(f"{self.name} dice: ppppprrr Guaf!")

#instancias

ninja1=Ninja("Jack", "Sparrow", "perro", "croqueta", "brit care")
mascota1=Mascota("Perla Negra", "Poodle", "croqueta", 0, 0 )

ninja1.mascota=mascota1

ninja1.caminar()
print()
ninja1.alimentar()
print()
ninja1.bañar()
print()