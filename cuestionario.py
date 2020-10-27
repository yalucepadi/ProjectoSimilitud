"""import sqlite3
import os
db = os.path.join(os.getcwd(),'mgtests.db3')
cnx = sqlite3.connect(db)
cur = cnx.cursor()
cur.execute('DROP TABLE IF EXISTS preguntas')
cur.execute('''
CREATE TABLE preguntas (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  pregunta TEXT NOT NULL,
  explicacion TEXT
);''')
cur.execute('DROP TABLE IF EXISTS respuestas')
cur.execute('''
CREATE TABLE respuestas (
  id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
  idpregunta INTEGER NOT NULL,
  respuesta text NOT NULL,
  correcta INTEGER DEFAULT 0
);''')
cnx.commit()
cur.close()
cnx.close()

numpregunta = 1
letras = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
correcta = ''
respuestascorrectas = 0
respuestasincorrectas = 0
db = os.path.join(os.getcwd(),'mgtests.db3')
cnx = sqlite3.connect(db)
curpreguntas = cnx.cursor()
currespuestas = cnx.cursor()
curpreguntas.execute('SELECT * FROM preguntas')
for pregunta in curpreguntas:
    print('----------')
    print('%s> %s' %(numpregunta,pregunta[1]))
    print('----------')
    numpregunta+=1
    currespuestas.execute('SELECT * FROM respuestas WHERE idpregunta=?',str(pregunta[0]))
    letrarespuesta = 0
    for respuesta in currespuestas:
        print('%s> %s' %(letras[letrarespuesta],respuesta[2]))
        if respuesta[3] == 1:
            correcta = letras[letrarespuesta]
        letrarespuesta +=1
    respuestausuario=input('¿Cual es la respuesta correcta? ')
    print()
    if respuestausuario.upper() == correcta:
        print('%s ->>> ¡Respuesta correcta!' %respuestausuario)
        respuestascorrectas+=1
    else:
        print('¡Error! la respuesta correcta era la %s' % correcta)
        respuestasincorrectas+=1
    print('----------')
    print()
print('----------')
print('Test finalizado')
print('----------')
print('Respuestas correctas: %s' %respuestascorrectas)
print('Respuestas incorrectas: %s' %respuestasincorrectas)

cnx.commit()
curpreguntas.close()
cnx.close()"""
import mysql.connector
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="",  database="preguntas")
cursor1=conexion1.cursor()
"""

sql="insert into cuestionario(pregunta, respuesta) values (%s,%s)"
datos=("De que color es el caballo blanco de simon bolivar","blanco")
cursor1.execute(sql, datos)
datos=("En que ciudad  esta la cultura chavin","ancash")
cursor1.execute(sql, datos)
"""
cursor1.execute("select pregunta, respuesta from cuestionario")
for fila in cursor1:
    print(fila)
conexion1.close()    

conexion1.commit()
conexion1.close()    