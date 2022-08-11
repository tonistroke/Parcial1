"""
Crear una aplicación de línea de comandos que permita 
1. registro
2. búsqueda
3. edición
4. eliminación 
de artículos dentro de un sistema de inventario."""

import pymongo
from pymongo import MongoClient


cluster = MongoClient("mongodb+srv://toni:1234@cluster0.wi9ojnj.mongodb.net/?retryWrites=true&w=majority")


db = cluster["FirstMongoDBApp"]
collection = db["Diccionario"]


#AddingArticles-------------------------------------------------------------------

#codigo = CÓDIGO PRODUCTO,	DESCRIPCIÓN,	ENTRADAS,	SALIDAS,	STOCK
#TOTAL

entrada00 = {"Codigo_de_producto":001, "Descripcion":"Espárragos", "Entradas":19, "Salidas":28,	"Stock":76}
entrada01 = {"Codigo_de_producto"002, "Descripcion":"Alcachofas", "Entradas":31,	"Salidas":39,	"Stock":72}
entrada02 = {"Codigo_de_producto":003, "Descripcion":"Pimientos del piquillo", "Entradas":16, "Salidas":14,	"Stock":57}
entrada03 = {"Codigo_de_producto":004, "Descripcion":"Tomates", "Entradas":9, "Salidas":12, "Stock":37}
entrada04 = {"Codigo_de_producto":005, "Descripcion":"Guisantes", "Entradas":11, "Salidas":6, "Stock":25}
entrada05 = {"Codigo_de_producto":006, "Descripcion":"Judías", "Entradas":7, "Salidas":6, "Stock":21}

collection_insert_many(entrada00, entrada01, entrada02, entrada03, entrada04, entrada05)


#Functions-----------------------------------------------------------------------

def add()
    result= collection.insert_one(In)
    print(result)
    return result

def find()
def edit()
def delete()

#MainApp--------------------------------------------------------------------------
print("INVENTARIO MENSUAL DE PRODUCTOS")
do{
  print("""
  ________________________MENU________________________
          1. Registrar nuevo articulo
          2. Buscar un articulo
          3. Editar un articulo
          4. Eliminar un articulo
  """)
  i = input("Elegir una de las 4 opciones")
  if i==1:
    print("Registrar nuevo articulo")
    
  if i==2:
    print("Buscar un articulo")

  if i==3:
    print("Editar un articulo")
  
  if i==4:
    print("Eliminar un articulo")
}while(i>0)
