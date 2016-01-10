import clases

def getAlmacen():
    arch = open("almacen.txt", "r")
    publicacion = arch.readlines()
    almacen = list()
    for i in publicacion:
        obj = i.strip().split(",")
        if obj[0] == 'l':
            almacen.append(clases.Libro(obj[1],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7]))
        elif obj[0] == 'c':
            almacen.append(clases.Comic(obj[1],obj[2],obj[3],obj[4],obj[5],obj[6],obj[7],obj[8]))
    return almacen   
    

def saveFile(almacen):
    archivo = open("almacen.txt", "w")     
    for i in almacen:
        archivo.write(i.formatear())
    archivo.close()
    
    
def addProduct(almacen,producto):
    almacen.append(producto)
    saveFile(almacen)
    print "Producto anadido correctamente"
    
def deleteProduct(almacen,producto):
    if almacen.count(producto) != 0:
        almacen.remove(producto)
        saveFile(almacen)
        print "Producto borrado correctamente"
    else:
        print "No se ha podido borrar, elemento no encontrado"
    
def searchProduct(almacen,busqueda):
    for i in almacen:
        if i.getId() == busqueda:
            return i
    return "Producto no encontrado"
            
def vender(almacen,producto):
    if almacen.count(producto) != 0:
        if producto.reducirStock():
            saveFile(almacen)
            print "Producto vendido correctamente"
        else:
            print "No queda stock para ese producto"
    else:
        print "No se ha podido vender, elemento no encontrado"
        
def imprimirAlmacen(almacen):
    for i in almacen:
        print i
        
def introducirProducto():  
    nombre = raw_input("Nombre: ")
    editorial = raw_input("Editorial: ")
    autor = raw_input("Autor: ")
    fecha = raw_input("Fecha: ")
    stock = raw_input("Stock: ")
    while(1):
        cat = raw_input("Es un libro o un comic (l/c)?")
        if cat == 'l':
            isbn = raw_input("ISBN: ")
            edicion = raw_input("Edicion: ")
            return clases.Libro(nombre,editorial,autor,fecha,stock,isbn,edicion)
        elif cat == 'c':
            issn = raw_input("ISSN: ")
            volumen = raw_input("Volumen: ")
            numero = raw_input("Numero: ")
            return clases.Comic(nombre,editorial,autor,fecha,stock,issn,volumen,numero)
        else:
            print "Dato incorrecto"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    