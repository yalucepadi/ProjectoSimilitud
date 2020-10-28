from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import  pandas as pd 
from stop_words import get_stop_words
stop_words = get_stop_words('spanish')

from  sklearn.feature_extraction.text  import CountVectorizer
vectorizer = CountVectorizer()
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer= TfidfVectorizer()

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
"""cursor1.execute("select pregunta, respuesta from cuestionario")
for fila in cursor1:
    print(fila)
conexion1.close()    
"""
cursor1.execute("select pregunta from cuestionario")
dataRespuesta=[]
for fila in cursor1:
    print(fila)
    respuesta=input("Ingrese su respuesta:".format(fila))
    dataRespuesta.append(respuesta)
    #dataRespuesta[len(dataRespuesta):] = [respuesta]
    


SQL_Query=pd.read_sql_query('''select respuesta from cuestionario''',conexion1)
    
df = pd.DataFrame(SQL_Query,columns=['respuesta'])
df.fillna(0)
Text= df['respuesta'].tolist()    
print(Text)
print(dataRespuesta)
X_tfidf=vectorizer.fit_transform(Text)
Y_tfidf=vectorizer.fit_transform(dataRespuesta)
x=X_tfidf
y=Y_tfidf
sims=cosine_similarity(X_tfidf,Y_tfidf)

#print(df)  
#print(SQL_Query) 
print(x)
print(y)
print(sims)
    
conexion1.commit()
conexion1.close()  


#print(fila)

  