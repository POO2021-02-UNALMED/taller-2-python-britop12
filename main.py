# -*- coding: utf-8 -*-

class Asiento:
    def __init__(self,color,precio,registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        colores = ["rojo", "verde", "amarillo", "negro", "blanco"]
        if color in colores:
            self.color = color


class Auto:
    cantidadCreados = 0 # Atributo de clase
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos (self) :
        c = 0
        for i in self.asientos :
            if isinstance (i, Asiento):
                c = c + 1
        return c

    def verificarIntegridad(self):
        if self.motor.registro == self.registro:
            for i in self.asientos:
                if type(i) == Asiento and self.registro != i.registro:
                    return "Las piezas no son originales"
            return "Auto original"
        
        else:
            return "Las piezas no son originales"
        
 
class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, num):
        self.registro = num

    def asignarTipo(self,tipo):
        tipos = ["electrico", "gasolina"]
        if tipo in tipos:
            self.tipo = tipo