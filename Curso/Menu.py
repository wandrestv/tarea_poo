from Curso.POO.RelacionesClases import opcion1
from Curso.POO.Polimorfismo import opcion2
from Curso.POO.Persona import opcion3
from Curso.POO.HerenciaMultiple import opcion4
from Curso.POO.Herencia import opcion5
from Curso.POO.Curso import opcion6
from Curso.POO.Cuenta import opcion7
from Curso.Break_Continue_Pass import opcion8
from Curso.Cadenas import opcion9
from Curso.Concatenacion import opcion10
from Curso.Conversiones import opcion11
from Curso.Diccionarios import opcion12
from Curso.Excepciones import opcion13
from Curso.Factorial import opcion14
from Curso.For import opcion15
from Curso.Funciones import opcion16
from Curso.Generadores import opcion17
from Curso.Generadores2 import opcion18
from Curso.HolaMundo import opcion19
from Curso.If_Else import opcion20
from Curso.If_In import opcion21
from Curso.IngreseDatos import opcion22
from Curso.Listas import opcion23
from Curso.Numero_Operaciones import opcion24
from Curso.OperadoresLogicos import opcion25
from Curso.OperadorTernario import opcion26
from Curso.PruebaPaquete import opcion27
from Curso.Raise import opcion28
from Curso.Range import opcion29
from Curso.Tuplas import opcion30
from Curso.Variables import opcion31
from Curso.While import opcion32
from Curso.modulos.modulos import opcion33
import os

# def menu_principal():
#     opciones = {
#         '1': ('Accion 1', opcion1),
#         '2': ('Accion 2', opcion2),
#         '3': ('Accion 3', opcion3),
#         '4': ('Accion 4', opcion4),
#         '5': ('Accion 5', opcion5),
#         '6': ('Accion 6', opcion6),
#         '7': ('Accion 7', opcion7),
#         '8': ('Accion 8', opcion8),
#         '9': ('Accion 9', opcion9),
#         '10': ('Accion 10', opcion10),
#         '11': ('Accion 11', opcion11),
#         '12': ('Accion 12', opcion12),
#         '13': ('Accion 13', opcion13),
#         '14': ('Accion 14', opcion14),
#         '15': ('Accion 15', opcion15),
#         '16': ('Accion 16', opcion16),
#         '17': ('Accion 17', opcion17),
#         '18': ('Accion 18', opcion18),
#         '19': ('Accion 19', opcion19),
#         '20': ('Accion 20', opcion3),
#         '21': ('Accion 21', opcion3),
#         '22': ('Accion 22', opcion3),
#         '23': ('Accion 23', opcion3),
#         '24': ('Accion 24', opcion3),
#         '25': ('Accion 25', opcion3),
#         '26': ('Accion 26', opcion3),
#         '27': ('Accion 27', opcion3),
#         '28': ('Accion 28', opcion3),
#         '29': ('Accion 29', opcion3),
#         '30': ('Accion 30', opcion3),
#         '31': ('Accion 31', opcion3),
#         '32': ('Accion 32', opcion3),
#
#         '4': ('Salir', salir)
#     }
#
#     generar_menu(opciones, '4')
#
# def generar_menu(opciones, opcion_salida):
#     opcion = None
#     while opcion != opcion_salida:
#         mostrar_menu(opciones)
#         opcion = leer_opcion(opciones)
#         ejecutar_opcion(opcion, opciones)
#         print()
#
# def mostrar_menu(opciones):
#     print('Seleccione una opci??n:')
#     for clave in sorted(opciones):
#         print(f' {clave}) {opciones[clave][0]}')





def menu():
    os.system("cls")
    print("Selecciona una opci??n")
    print("\t1 - primera opci??n")
    print("\t2 - segunda opci??n")
    print("\t3 - tercera opci??n")
    print("\t4 - cuarta opci??n")
    print("\t5 - quinta opci??n")
    print("\t6 - sexta opci??n")
    print("\t7 - septima opci??n")
    print("\t8 - octava opci??n")
    print("\t9 - novena opci??n")
    print("\t10 - decima opci??n")
    print("\t11 - decima primera opci??n")
    print("\t12 - decima segunda opci??n")
    print("\t13 - decima tercera opci??n")
    print("\t14 - decima cuarta opci??n")
    print("\t15 - decima quinta opci??n")
    print("\t16 - decima sexta opci??n")
    print("\t17 - decima septima opci??n")
    print("\t18 - decima octava opci??n")
    print("\t19 - decima novena opci??n")
    print("\t20 - vigesima opci??n")
    print("\t21 - vigesima primera opci??n")
    print("\t22 - vigesima segunda opci??n")
    print("\t23 - vigesima tercera opci??n")
    print("\t24 - vigesima cuarta opci??n")
    print("\t25 - vigesima quinta opci??n")
    print("\t26 - vigesima sexta opci??n")
    print("\t27 - vigesima septima opci??n")
    print("\t28 - vigesima octava opci??n")
    print("\t29 - vigesima novena opci??n")
    print("\t30 - trigesima opci??n")
    print("\t31 - trigesima primera opci??n")
    print("\t32 - trigesima segunda opci??n")
    print("\t32 - trigesima tercera opci??n")
    print("\t34 - salir")

while True:
    menu()
    opcionMenu = input("inserta un numero valor >> ")
    if opcionMenu == "1":
        a = opcion1()
        print("")
        input("Has pulsado la opci??n 1...\npulsa una tecla para continuar")
        os.system('cls')
    elif opcionMenu == "2":
        a2 = opcion2()
        print("")
        input("Has pulsado la opci??n 2...\npulsa una tecla para continuar")
    elif opcionMenu == "3":
        a3 = opcion3()
        print("")
        input("Has pulsado la opci??n 3...\npulsa una tecla para continuar")
    elif opcionMenu == "4":
        a4 = opcion4()
        print("")
        input("Has pulsado la opci??n 4...\npulsa una tecla para continuar")
    elif opcionMenu == "5":
        a5 = opcion5()
        print("")
        input("Has pulsado la opci??n 5...\npulsa una tecla para continuar")
    elif opcionMenu == "6":
        a6 = opcion6()
        print("")
        input("Has pulsado la opci??n 6...\npulsa una tecla para continuar")
    elif opcionMenu == "7":
        a7 = opcion7()
        print("")
        input("Has pulsado la opci??n 7...\npulsa una tecla para continuar")
    elif opcionMenu == "8":
        a8 = opcion8()
        print("")
        input("Has pulsado la opci??n 8...\npulsa una tecla para continuar")
    elif opcionMenu == "9":
        a9 = opcion9()
        print("")
        input("Has pulsado la opci??n 9...\npulsa una tecla para continuar")
    elif opcionMenu == "10":
        a10 = opcion10()
        print("")
        input("Has pulsado la opci??n 10...\npulsa una tecla para continuar")
    elif opcionMenu == "11":
        a11 = opcion11()
        print("")
        input("Has pulsado la opci??n 11...\npulsa una tecla para continuar")
    elif opcionMenu == "12":
        a12 = opcion12()
        print("")
        input("Has pulsado la opci??n 12...\npulsa una tecla para continuar")
    elif opcionMenu == "13":
        a2 = opcion13()
        print("")
        input("Has pulsado la opci??n 13...\npulsa una tecla para continuar")
    elif opcionMenu == "14":
        a14 = opcion14()
        print("")
        input("Has pulsado la opci??n 14...\npulsa una tecla para continuar")
    elif opcionMenu == "15":
        a15 = opcion15()
        print("")
        input("Has pulsado la opci??n 15...\npulsa una tecla para continuar")
    elif opcionMenu == "16":
        a16 = opcion16()
        print("")
        input("Has pulsado la opci??n 16...\npulsa una tecla para continuar")
    elif opcionMenu == "17":
        a17 = opcion17()
        print("")
        input("Has pulsado la opci??n 17...\npulsa una tecla para continuar")
    elif opcionMenu == "18":
        a18 = opcion18()
        print("")
        input("Has pulsado la opci??n 18...\npulsa una tecla para continuar")
    elif opcionMenu == "18":
        a18 = opcion18()
        print("")
        input("Has pulsado la opci??n 18...\npulsa una tecla para continuar")
    elif opcionMenu == "19":
        a19 = opcion19()
        print("")
        input("Has pulsado la opci??n 19...\npulsa una tecla para continuar")
    elif opcionMenu == "20":
        a20 = opcion20()
        print("")
        input("Has pulsado la opci??n 20...\npulsa una tecla para continuar")
    elif opcionMenu == "21":
        a21 = opcion21()
        print("")
        input("Has pulsado la opci??n 21...\npulsa una tecla para continuar")
    elif opcionMenu == "22":
        a22 = opcion22()
        print("")
        input("Has pulsado la opci??n 22...\npulsa una tecla para continuar")
    elif opcionMenu == "23":
        a23 = opcion23()
        print("")
        input("Has pulsado la opci??n 23...\npulsa una tecla para continuar")
    elif opcionMenu == "24":
        a24 = opcion24()
        print("")
        input("Has pulsado la opci??n 24...\npulsa una tecla para continuar")
    elif opcionMenu == "25":
        a25 = opcion25()
        print("")
        input("Has pulsado la opci??n 25...\npulsa una tecla para continuar")
    elif opcionMenu == "26":
        a26 = opcion26()
        print("")
        input("Has pulsado la opci??n 26...\npulsa una tecla para continuar")
    elif opcionMenu == "27":
        a27 = opcion27()
        print("")
        input("Has pulsado la opci??n 27...\npulsa una tecla para continuar")
    elif opcionMenu == "28":
        a28 = opcion28()
        print("")
        input("Has pulsado la opci??n 28...\npulsa una tecla para continuar")
    elif opcionMenu == "29":
        a29 = opcion29()
        print("")
        input("Has pulsado la opci??n 29...\npulsa una tecla para continuar")
    elif opcionMenu == "30":
        a30 = opcion30()
        print("")
        input("Has pulsado la opci??n 30...\npulsa una tecla para continuar")
    elif opcionMenu == "31":
        a31 = opcion31()
        print("")
        input("Has pulsado la opci??n 31...\npulsa una tecla para continuar")
    elif opcionMenu == "32":
        a32 = opcion32()
        print("")
        input("Has pulsado la opci??n 32...\npulsa una tecla para continuar")
    elif opcionMenu == "33":
        a33 = opcion33()
        print("")
        input("Has pulsado la opci??n 33...\npulsa una tecla para continuar")
    elif opcionMenu == "34":
        break
    else:
        print("")
        input("No has pulsado ninguna opci??n correcta...\npulsa una tecla para continuar")
