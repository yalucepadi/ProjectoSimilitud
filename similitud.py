from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

from stop_words import get_stop_words
stop_words = get_stop_words('spanish')

from  sklearn.feature_extraction.text  import CountVectorizer
vectorizer = CountVectorizer()
 

"""
data=['Yo quiero aquel gato', 'Yo quiero un perro', 'Yo quiero aquel perro','Yo quiero aquel perico','Yo quiero aquel gato','Yo quiero gato']

x=vectorizer.fit_transform(data)
#print(x)

print("Obtener  caracteristicas de nombres")
print(vectorizer.get_feature_names()) 

print("Vocabulario")
print(vectorizer.vocabulary_)

from sklearn.feature_extraction.text import TfidfVectorizer
tfidf = TfidfVectorizer().fit_transform(data)
print(tfidf)


from sklearn.metrics.pairwise import cosine_similarity

print(cosine_similarity(tfidf[0:1],tfidf).flatten())
y=cosine_similarity(tfidf[0:1],tfidf).flatten()
print(y[5])
"""
"""vec1 = np.array([[1,1,0,1,1]])
vec2 = np.array([[0,1,0,1,1]])
k=cosine_similarity(vec1,vec2)
print(k)"""
import  pandas as pd 

df = pd.read_csv('GB3.csv')
df.fillna(0)
Text=df['title'].tolist()

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer= TfidfVectorizer()



X_tfidf=vectorizer.fit_transform(Text)
y=X_tfidf
#print(y)

sims=cosine_similarity(X_tfidf[0:1],X_tfidf)
print(sims)
