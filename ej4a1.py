"""
Enunciado:
Dadas dos listas de elementos, implementa una función llamada
find_intersection(list_1, list_2) que retorne la intersección de ambas listas.

Parámetros:
    list_1 (List): Lista de elementos
    list_2 (List): Lista de elementos

Ejemplo:
    Entrada:
    list_1 = [1, 2, 3, 4, 5]
    list_2 = [4, 5, 6, 7, 8]

    Salida:
    [4, 5]

Enunciat:
Donades dues llistes d'elements, implementa una funció anomenada
find_intersection(list_1, list_2) que retorni la intersecció de les dues llistes.

Paràmetres:
     list_1 (List): Llista d'elements
     list_2 (List): Llista d'elements

Exemple:
     Entrada:
     list_1 = [1, 2, 3, 4, 5]
     list_2 = [4, 5, 6, 7, 8]

     Sortida:
     [4, 5]

"""

list_1 = [1, 2, 3, 4, 5]
list_2 = [4, 5, 6, 7, 8]


def find_intersection(list_1, list_2):
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [4, 5, 6, 7, 8]
resultado = find_instersection(lista_1, lista_2)
assert resultado == [4,5], "find_instersection does not return the correct value for input ([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]). It should be [4, 5]" 
lista_3 = [1, 2, 3,]
lista_4 = [4, 5, 6]
assert resultado == [],"find_instersection does not return the correct value for input ([1, 2, 3,], [4, 5, 6]). It should be []"
lista_5 = []
lista_6 = [1, 2, 3]
resultado = find_instersection(lista_5, lista_6)
assert resultado == [],"find_instersection does not return the correct value for input ([],  [1, 2, 3]). It should be []"
   


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
# Si vols provar el teu codi, descomenta les línies següents i executa l'script

# print(find_intersection([1, 2, 3, 4], [3, 4, 5, 6]))
# print(find_intersection(['apple', 'banana', 'orange'], ['banana', 'kiwi', 'apple']))
