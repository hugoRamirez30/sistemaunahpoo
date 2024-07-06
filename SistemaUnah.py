class Persona:
    def __init__(self, nombre, apellido, edad, direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.direccion = direccion

    def mostrar_datos(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, Edad: {self.edad}, Dirección: {self.direccion}"


class Alumno(Persona):
    def __init__(self, nombre, apellido, edad, direccion, carrera, horario, numero_cuenta):
        super().__init__(nombre, apellido, edad, direccion)
        self.carrera = carrera
        self.horario = horario
        self.numero_cuenta = numero_cuenta

    def mostrar_datos(self):
        datos_persona = super().mostrar_datos()
        return f"{datos_persona}, Carrera: {self.carrera}, Horario: {self.horario}, Número de cuenta: {self.numero_cuenta}"


class Maestro(Persona):
    def __init__(self, nombre, apellido, edad, direccion, facultad, especializacion, numero_empleado):
        super().__init__(nombre, apellido, edad, direccion)
        self.facultad = facultad
        self.especializacion = especializacion
        self.numero_empleado = numero_empleado

    def mostrar_datos(self):
        datos_persona = super().mostrar_datos()
        return f"{datos_persona}, Facultad: {self.facultad}, Especialización: {self.especializacion}, Número de empleado: {self.numero_empleado}"


class Empleado(Persona):
    def __init__(self, nombre, apellido, edad, direccion, numero_empleado, area_trabajo, tipo_trabajo):
        super().__init__(nombre, apellido, edad, direccion)
        self.numero_empleado = numero_empleado
        self.area_trabajo = area_trabajo
        self.tipo_trabajo = tipo_trabajo

    def mostrar_datos(self):
        datos_persona = super().mostrar_datos()
        return f"{datos_persona}, Número de empleado: {self.numero_empleado}, Área de trabajo: {self.area_trabajo}, Tipo de trabajo: {self.tipo_trabajo}"


class Visitante(Persona):
    def __init__(self, nombre, apellido, edad, direccion, razon_visita, edificio):
        super().__init__(nombre, apellido, edad, direccion)
        self.razon_visita = razon_visita
        self.edificio = edificio

    def mostrar_datos(self):
        datos_persona = super().mostrar_datos()
        return f"{datos_persona}, Razón de visita: {self.razon_visita}, Edificio: {self.edificio}"


class JefeCoordinador(Maestro, Empleado):
    def __init__(self, nombre, apellido, edad, direccion, facultad, especializacion, numero_empleado, area_trabajo,
                 tipo_trabajo, fecha_inicio, fecha_fin, tipo_cargo):
        Maestro.__init__(self, nombre, apellido, edad, direccion, facultad, especializacion, numero_empleado)
        Empleado.__init__(self, nombre, apellido, edad, direccion, numero_empleado, area_trabajo, tipo_trabajo)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.tipo_cargo = tipo_cargo

    def mostrar_datos(self):
        datos_maestro = Maestro.mostrar_datos(self)
        datos_empleado = Empleado.mostrar_datos(self)
        return f"{datos_maestro}, {datos_empleado}, Fecha de inicio: {self.fecha_inicio}, Fecha de fin: {self.fecha_fin}, Tipo de cargo: {self.tipo_cargo}"


class Sistema:
    def __init__(self):
        self.personas = []

    def registrar_persona(self):
        tipo_persona = input(
            "Ingrese el tipo de persona (alumno, maestro, empleado, visitante, jefe/coordinador): ").strip().lower()

        nombre = input("Nombre: ")
        apellido = input("Apellido: ")
        edad = int(input("Edad: "))
        direccion = input("Dirección: ")

        if any(p.nombre == nombre and p.apellido == apellido for p in self.personas):
            print("Error: Esta persona ya ha sido registrada.")
            return

        if tipo_persona == "alumno":
            carrera = input("Carrera: ")
            horario = input("Horario(ejem:10:00-4:00): ")
            numero_cuenta = input("Número de cuenta: ")
            persona = Alumno(nombre, apellido, edad, direccion, carrera, horario, numero_cuenta)

        elif tipo_persona == "maestro":
            facultad = input("Facultad: ")
            especializacion = input("Especialización: ")
            numero_empleado = input("Número de empleado: ")
            persona = Maestro(nombre, apellido, edad, direccion, facultad, especializacion, numero_empleado)

        elif tipo_persona == "empleado":
            numero_empleado = input("Número de empleado: ")
            area_trabajo = input("Área de trabajo: ")
            tipo_trabajo = input("Tipo de trabajo (campo/oficina): ")
            persona = Empleado(nombre, apellido, edad, direccion, numero_empleado, area_trabajo, tipo_trabajo)

        elif tipo_persona == "visitante":
            razon_visita = input("Razón de visita: ")
            edificio = input("Edificio: ")
            persona = Visitante(nombre, apellido, edad, direccion, razon_visita, edificio)


        elif tipo_persona in ("jefe", "coordinador"):
            facultad = input("Facultad: ")
            especializacion = input("Especialización: ")
            numero_empleado = input("Número de empleado: ")
            area_trabajo = input("Área de trabajo: ")
            tipo_trabajo = input("Tipo de trabajo (campo/oficina): ")
            fecha_inicio = input("Fecha de inicio en el cargo: ")
            fecha_fin = input("Fecha de fin en el cargo: ")
            tipo_cargo = input("Tipo de cargo (jefe/coordinador): ")
            persona = JefeCoordinador(nombre, apellido, edad, direccion, facultad, especializacion, numero_empleado,
                                      area_trabajo, tipo_trabajo, fecha_inicio, fecha_fin, tipo_cargo)

        else:
            print("Tipo de persona no válido.")
            return

        self.personas.append(persona)
        print("Persona registrada con éxito.")

    def mostrar_personas(self):
        for persona in self.personas:
            print(persona.mostrar_datos())



sistema = Sistema()

while True:
    sistema.registrar_persona()
    continuar = input("¿Desea registrar otra persona? (si/no): ").strip().lower()
    if continuar != 'si':
        break


sistema.mostrar_personas()
