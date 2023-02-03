#1. Remueva los strings vaciós de una lista de strings
#lista1 = ["gatos","","perros","ratones",""]
#del(lista1[1])
#lista1.remove('')
#print(lista1)

#2. Añada un nuevo elemento a una lista despues de un elemento especifico.
#lista2= [1,2,[200,400,[1000,6000],800],30,40]
#lista2[2][2].insert(1,5000)
#print(lista2)

#3. Cree un nuevo string, usando el primer, tercer y ultimo elemento de un string dado
#str = "Después de la tempestad, viene la calma"
#str_2= str[0] +str[2] + str[-1]
#print(str_2)

#4. Escriba un script para convertir la temperatura dada en dados centigrados a Farhrenheit
#temperatura_centigrados = 20
#temperatura_farhenheint = temperatura_centigrados*1.8 +32
#print (temperatura_farhenheint)

#diccionario = {"marca": "ford", "modelo": "mustang", "año":2000}
#print(diccionario["marca"])

#5. Mezcle dos diccionarios en uno

#dict1 = {'Diez': 10, 'Veinte': 20, 'Treinta': 30}
#dict2 = {'Treinta': 30, 'Cuarenta': 40, 'Cincuenta': 50}

#dict3 = dict1 | dict2
#print(dict3)

#diccionarioEstudiante= {
#      "clase": {
#           "estudiante": {
#                "nombre": "Mike",
#                    "marcas": {
#                    "fisica": 70,
#                    "historia": 80
#                    }
#                }       
#            }
#        }
#x= diccionarioEstudiante["historia"]
#print(x)

#7. Cambie la fecha de nacimiento de Platonn del año 427 A.C. al año 428 A.C.
dict5 = {"nombre": "Platón", "país": "Antigua Grecia", "fecha_de_nacimiento": -427,"maestro": "Sócrates", "alumno": "Aristóteles"}
dict5.pop("fecha_de_nacimiento")
dict5.update({"fecha_de_nacimiento": -428})
print(dict5)

