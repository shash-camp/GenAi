from sklearn.feature_extraction.text import CountVectorizer


documents = [
    "I love machine learning",
    "Machine learning is fun and exciting",
    "I love coding in Python"
]


vectorizer = CountVectorizer()


X = vectorizer.fit_transform(documents)

#fit learn the vocubalary and transform the document into no of count of words



print("Vocabulary:")


print(X.toarray()) 
