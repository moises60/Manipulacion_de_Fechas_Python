import random
from datetime import datetime

class Fecha:
    def __init__(self, dia=1, mes=1, año=1):
        """
        Inicializa una instancia de la clase Fecha.
        
        Argumentos:
        dia (int): Día del mes (1-31). Por defecto es 1.
        mes (int): Mes del año (1-12). Por defecto es 1.
        año (int): Año (positivo). Por defecto es 1.
        """
        self.dia = dia
        self.mes = mes
        self.año = año
        
        if not self.fecha_valida():
            print("¡¡¡La fecha introducida no es una fecha válida!!!")
            self.dia = 1
            self.mes = 1
            self.año = 1

    def __str__(self):
        """
        Devuelve una representación en cadena de la fecha en formato "dd / mm / aaaa".
        
        Retorno:
        str: La fecha en formato "dd / mm / aaaa".
        """
        dia_str = f"{self.dia:02}"
        mes_str = f"{self.mes:02}"
        año_str = f"{self.año:04}"
        return f"{dia_str} / {mes_str} / {año_str}"

    def es_bisiesto(self):
        """
        Determina si el año de la fecha es bisiesto.
        
        Retorno:
        bool: True si el año es bisiesto, False en caso contrario.
        """
        if (self.año % 4 == 0 and self.año % 100 != 0) or (self.año % 400 == 0):
            return True
        else:
            return False

    def total_dias_mes(self):
        """
        Devuelve el número de días en el mes de la fecha actual.
        
        Retorno:
        int: Número de días en el mes correspondiente.
        """
        dias_en_mes = [31, 29 if self.es_bisiesto() else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return dias_en_mes[self.mes - 1]

    def fecha_valida(self):
        """
        Verifica si la fecha es válida.
        
        Retorno:
        bool: True si la fecha es válida, False en caso contrario.
        """
        if not (1 <= self.mes <= 12):
            return False
        if not (1 <= self.dia <= self.total_dias_mes()):
            return False
        return True
    
    @property
    def nombre_mes(self):
        """
        Devuelve el nombre del mes en español.
        
        Retorno:
        str: Nombre del mes.
        """
        nombres_meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        return nombres_meses[self.mes - 1]
    
    @staticmethod
    def son_iguales(fecha1, fecha2):
        """
        Compara dos fechas y determina si son iguales.
        
        Argumentos:
        fecha1 (Fecha): Primera fecha a comparar.
        fecha2 (Fecha): Segunda fecha a comparar.
        
        Retorno:
        bool: True si las fechas son iguales, False en caso contrario.
        """
        return fecha1.dia == fecha2.dia and fecha1.mes == fecha2.mes and fecha1.año == fecha2.año

    @staticmethod
    def es_posterior(fecha1, fecha2):
        """
        Determina si la primera fecha es posterior a la segunda.
        
        Argumentos:
        fecha1 (Fecha): Primera fecha a comparar.
        fecha2 (Fecha): Segunda fecha a comparar.
        
        Retorno:
        bool: True si la primera fecha es posterior, False en caso contrario.
        """
        if fecha1.año > fecha2.año:
            return True
        elif fecha1.año == fecha2.año:
            if fecha1.mes > fecha2.mes:
                return True
            elif fecha1.mes == fecha2.mes:
                return fecha1.dia > fecha2.dia
        return False

    @staticmethod
    def es_anterior(fecha1, fecha2):
        """
        Determina si la primera fecha es anterior a la segunda.
        
        Argumentos:
        fecha1 (Fecha): Primera fecha a comparar.
        fecha2 (Fecha): Segunda fecha a comparar.
        
        Retorno:
        bool: True si la primera fecha es anterior, False en caso contrario.
        """
        if fecha1.año < fecha2.año:
            return True
        elif fecha1.año == fecha2.año:
            if fecha1.mes < fecha2.mes:
                return True
            elif fecha1.mes == fecha2.mes:
                return fecha1.dia < fecha2.dia
        return False
    
    @classmethod
    def primer_dia_año(cls, año):
        """
        Crea una instancia de Fecha con el primer día del año dado.
        
        Argumentos:
        año (int): Año para crear la fecha.
        
        Retorno:
        Fecha: Instancia de Fecha con el primer día del año.
        """
        return cls(1, 1, año)
    
    @classmethod
    def ultimo_dia_año(cls, año):
        """
        Crea una instancia de Fecha con el último día del año dado.
        
        Argumentos:
        año (int): Año para crear la fecha.
        
        Retorno:
        Fecha: Instancia de Fecha con el último día del año.
        """
        return cls(31, 12, año)
    
    def incrementar_dia(self):
        """
        Incrementa un día la fecha actual, ajustando el mes y el año si es necesario.
        """
        self.dia += 1
        if self.dia > self.total_dias_mes():
            self.dia = 1
            self.mes += 1
            if self.mes > 12:
                self.mes = 1
                self.año += 1
    
    def decrementar_dia(self):
        """
        Decrementa un día la fecha actual, ajustando el mes y el año si es necesario.
        """
        self.dia -= 1
        if self.dia < 1:
            self.mes -= 1
            if self.mes < 1:
                self.mes = 12
                self.año -= 1
            self.dia = self.total_dias_mes()

    @classmethod
    def copiar(cls, fecha):
        """
        Crea una copia de la fecha dada.
        
        Argumentos:
        fecha (Fecha): Fecha a copiar.
        
        Retorno:
        Fecha: Una nueva instancia de Fecha con los mismos valores.
        """
        return cls(fecha.dia, fecha.mes, fecha.año)

    @staticmethod
    def diferencia(fecha1, fecha2):
        """
        Calcula la diferencia en días entre dos fechas.
        
        Argumentos:
        fecha1 (Fecha): Primera fecha.
        fecha2 (Fecha): Segunda fecha.
        
        Retorno:
        int: Número de días entre las dos fechas.
        """
        d1 = datetime(fecha1.año, fecha1.mes, fecha1.dia)
        d2 = datetime(fecha2.año, fecha2.mes, fecha2.dia)
        return abs((d1 - d2).days)

    @classmethod
    def fecha_aleatoria(cls):
        """
        Genera una fecha aleatoria válida.
        
        Retorno:
        Fecha: Una instancia de Fecha con valores aleatorios.
        """
        año = random.randint(1, 9999)
        mes = random.randint(1, 12)
        dia = random.randint(1, cls(1, mes, año).total_dias_mes())
        return cls(dia, mes, año)

    @classmethod
    def desde_cadena(cls, fecha_str):
        """
        Convierte una cadena con el formato "01 Enero 0001" a una instancia de Fecha.
        
        Argumentos:
        fecha_str (str): Cadena con la fecha en formato "dd Mes aaaa".
        
        Retorno:
        Fecha: Una instancia de Fecha con los valores correspondientes.
        """
        nombres_meses = {
            "Enero": 1, "Febrero": 2, "Marzo": 3, "Abril": 4,
            "Mayo": 5, "Junio": 6, "Julio": 7, "Agosto": 8,
            "Septiembre": 9, "Octubre": 10, "Noviembre": 11, "Diciembre": 12
        }
        dia_str, mes_str, año_str = fecha_str.split()
        dia = int(dia_str)
        mes = nombres_meses[mes_str]
        año = int(año_str)
        return cls(dia, mes, año)
