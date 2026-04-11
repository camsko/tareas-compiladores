# Clases
class Humano:
    def __init__(self, nombre, **kwargs):
        super().__init__(**kwargs)
        self.nombre = nombre

    def hablar(self):
        return f"{self.nombre} está hablando."

    def __str__(self):
        return f"Humano = {self.nombre}"

# Herencia simple
class Estudiante(Humano):
    def __init__(self, nombre=None, carrera=None, **kwargs):
        super().__init__(nombre=nombre, **kwargs)
        self.carrera = carrera

    def hablar(self):
        return f"{self.nombre} estudia {self.carrera}."

class Trabajador(Humano):
    def __init__(self, nombre=None, puesto=None, **kwargs):
        super().__init__(nombre=nombre, **kwargs)
        self.puesto = puesto

    def hablar(self):
        return f"{self.nombre} trabaja como {self.puesto}."


# Herencia múltiple -> Para ver MRO (Method Resolution Order)
class EstudianteTrabajador(Estudiante, Trabajador):
    def __init__(self, nombre, carrera, puesto):
        super().__init__(
            nombre=nombre,
            carrera=carrera,
            puesto=puesto
        )

    def hablar(self):
        base = super().hablar()
        return base + f" y también trabaja como {self.puesto}."


# Metodos dunder
class Grupo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.miembros = []

    def agregar(self, persona):
        self.miembros.append(persona)

    def __len__(self):
        return len(self.miembros)

    def __add__(self, otro):
        nuevo = Grupo(self.nombre + "+" + otro.nombre)
        nuevo.miembros = self.miembros + otro.miembros
        return nuevo

    def __getitem__(self, index):
        return self.miembros[index]


if __name__ == "__main__":
    p1 = Humano("Keylor")
    e1 = Estudiante("Henoc", "Ingeniería")
    t1 = Trabajador("Keylor", "Profesor")
    et1 = EstudianteTrabajador("Keylor", "Medicina", "Enfermero")

    print(p1)
    print(e1.hablar())
    print(t1.hablar())
    print(et1.hablar())

    # Prueba de métodos dunder
    g1 = Grupo("Grupo 1")
    g1.agregar(p1)
    g1.agregar(e1)

    g2 = Grupo("Grupo 2")
    g2.agregar(t1)
    g2.agregar(et1)

    g3 = g1 + g2
    
    print("\nCantidad de miembros:", len(g3))
    print("Primer miembro:", g3[0])