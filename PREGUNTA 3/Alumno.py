
import unittest

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota
        print("Alumno creado")

    def __str__(self):
        return f"{self.nombre}, {self.nota}"
    
    def calificacion(self):
        if self.nota >= 5:
            return "Aprobado"
        else:
            return "Suspenso"
        
# Prueba de la clase Alumno
class TestAlumno(unittest.TestCase):
    def test_alumno(self):
        alumno = Alumno("Juan", 7)
        self.assertEqual(alumno.nombre, "Juan")
        self.assertEqual(alumno.nota, 7)
        self.assertEqual(alumno.calificacion(), "Aprobado")
        alumno = Alumno("Maria", 3)
        self.assertEqual(alumno.nombre, "Maria")
        self.assertEqual(alumno.nota, 3)
        self.assertEqual(alumno.calificacion(), "Suspenso")

if __name__ == "__main__":
    unittest.main()
    
