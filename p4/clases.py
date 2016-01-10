#CLASE PUBLICACION
class Publicacion:
    nombre =""
    editorial = ""
    autor = ""
    fecha = ""
    stock = 0
    def __init__(self,nombre,editorial,autor,fecha,stock):
        self.nombre = nombre
        self.editorial = editorial
        self.autor = autor
        self.fecha = fecha
        self.stock = stock      
        
    def reducirStock(self):
        if int(self.stock) > 0:
            self.stock = int(self.stock) - 1
            return True
        else:
            return False

#CLASE LIBRO
class Libro(Publicacion):
    isbn = ""
    edicion = ""
    def __init__(self,nombre,editorial,autor,fecha,stock,isbn,edicion):
        Publicacion.__init__(self,nombre,editorial,autor,fecha,stock)
        self.isbn = isbn
        self.edicion = edicion
        
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.nombre, self.editorial, self.autor, self.fecha, self.stock, self.isbn, self.edicion)  

    def formatear(self):
        return "l,%s,%s,%s,%s,%s,%s,%s\n" % (self.nombre, self.editorial, self.autor, self.fecha, self.stock, self.isbn, self.edicion)
        
    def getId(self):
        return self.isbn

#CLASE COMIC
class Comic(Publicacion):
    issn = ""
    volumen =""
    numero =""
    def __init__(self,nombre,editorial,autor,fecha,stock,issn,volumen,numero):
        Publicacion.__init__(self,nombre,editorial,autor,fecha,stock)
        self.issn = issn
        self.volumen = volumen
        self.numero = numero
        
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s, %s" % (self.nombre, self.editorial, self.autor, self.fecha, self.stock, self.issn, self.volumen, self.numero)  
        
    def formatear(self):
        return "c,%s,%s,%s,%s,%s,%s,%s,%s\n" % (self.nombre, self.editorial, self.autor, self.fecha, self.stock, self.issn, self.volumen, self.numero)  
    
    def getId(self):
        return self.issn
