class CocheEmpresa:
    def __init__(self,matricula,marca,modelo):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo

class Empleado:
    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario, aumento):
        self.nombre = nombre
        self.apellidos = apellidos
        self.dni = dni
        self.direccion = direccion
        self.telefono = telefono
        self.salario = salario
        self.supervisor = 0
        self.aumento = aumento

    def imprimir(self):
        print("Nombre: ",self.nombre, " Apellidos: ", self.apellidos)
        print("DNI: ",self.dni)
        print("Direccion: ",self.direccion)
        print("Telefono: ", self.telefono)
        print("Salario: ",self.salario)
        print("Incremento anual: ",self.aumento)

    def cambiarSupervisor(self,newSuper):
        self.supervisor = newSuper

    def incrementaSalario(self):
        self.salario = self.salario * ((100 + self.aumento) / 100)

class Secretario(Empleado):
    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario, despacho, fax):
        Empleado.__init__(self,nombre,apellidos,dni,direccion,telefono,salario, 5)
        self.despacho = despacho
        self.fax = fax

    def imprimir(self):
        Empleado.imprimir(self)
        print("Despacho: ", self.despacho)
        print("Fax: ", self.fax)

class Vendedor(Empleado):
    def __init__(self,nombre,apellidos,dni,direccion,telefono,salario, coche,areaVenta,comision):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, telefono, salario, 10)
        self.coche = coche
        self. areaVenta = areaVenta
        self.comision = comision

        self.clientes = []

    def imprimir(self):
        Empleado.imprimir(self)
        print("Coche: ", self.coche.matricula)
        print("Area de venta: ", self.areaVenta)
        print("Comision: ", self.comision)

    def altaCliente(self, cliente):
        self.clientes.append(cliente)
    def bajaCliente(self, cliente):
        self.clientes.remove(cliente)

    def cambiaCoche(self,newCoche):
        self.coche = newCoche

class JefeZona(Empleado):
    def __init__(self, nombre, apellidos, dni, direccion, telefono, salario, despacho, secretario, coche):
        Empleado.__init__(self, nombre, apellidos, dni, direccion, telefono, salario, 20)

        self.despacho = despacho
        self.secretario = secretario
        self.vendedores = []
        self.coche = coche

    def imprimir(self):
        Empleado.imprimir(self)
        print("Despacho: ", self.despacho)
        print("Secretario: ", self.secretario.dni)
        print("Coche: ", self.coche.matricula)

    def altaVendedor(self, vendedor):
        self.vendedores.append(vendedor)
    def bajaVendedor(self, vendedor):
        self.vendedores.remove(vendedor)


coche1 = CocheEmpresa("ABCD", "Ford", "Focus")
coche2 = CocheEmpresa("CBDA", "Citroen", "C15")

secret1 = Secretario("si", "si", "12341A", "Calle San Pedro nº 12", 123456789, 1000, "2º A", 1234)

vend1 = Vendedor("no", "no", "33341G", "Calle Leopol nº 4", 123456789, 1000, coche1, "Albolote", 10)

jefeZona1 = JefeZona("Tal vez", "Tal vez", "66643H", "Calle Leopol nº 15", 123456789, 1000, "3º A", secret1, coche2)

print("Todos los empleados comienzan un salario de 1000 para ver su incremento")
secret1.incrementaSalario()
vend1.incrementaSalario()
jefeZona1.incrementaSalario()

secret1.imprimir()
vend1.imprimir()
jefeZona1.imprimir()