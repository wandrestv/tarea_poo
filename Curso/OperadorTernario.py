"""
String sexo;
sexo = (10 > 20) ? "Masculino" : "Femenino";
"""

sexos = ("Hombre", "Mujer")

posicion = True
sexo = sexos[1] # Mujer
print(sexo)
sexo = sexos[not posicion] # Hombre
print(sexo)