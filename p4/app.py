import funciones

def ver(almacen):
    print "Listado de libros:"
    funciones.imprimirAlmacen(almacen)

def aniadir(almacen):
    print "Add un Producto:"
    producto = funciones.introducirProducto()
    funciones.addProduct(almacen,producto)

def buscar(almacen):
    print "Buscar un producto"
    ident = raw_input("Introduce el identificador del producto. (isbn o issn)")
    print funciones.searchProduct(almacen,ident)
    
def borrar(almacen):
    print "Borrar un producto"
    ident = raw_input("Introduce el identificador del producto. (isbn o issn)")
    producto = funciones.searchProduct(almacen,ident)
    funciones.deleteProduct(almacen,producto)
    
def vender(almacen):
    print "Vender un producto"
    ident = raw_input("Introduce el identificador del producto. (isbn o issn)")
    producto = funciones.searchProduct(almacen,ident)
    funciones.vender(almacen,producto)
    
while(1):
    print "\n\nTIENDA VIRTUAL"
    print "\nSeleccione que desa hacer"
    print "(1) Ver los productos"
    print "(2) Aniadir un producto nuevo"
    print "(3) Buscar un producto"
    print "(4) Borrar un producto"
    print "(5) Vender un producto"
    print "(0) Salir"
    
    opcion = int(raw_input("Introduce opcion:"))
    almacen = funciones.getAlmacen()
    if opcion == 1:
        ver(almacen)
    elif opcion == 2:
        aniadir(almacen)
    elif opcion == 3:
        buscar(almacen)
    elif opcion == 4:
        borrar(almacen)
    elif opcion == 5:
        vender(almacen)
    elif opcion == 0:
        break
    else:
        print "Opcion incorrecta, vuelve a introducir otra vez"
        
print "FIN DEL PROGRAMA"


