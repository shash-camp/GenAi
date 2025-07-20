from sklearn.feature_extraction.text import CountVectorizer


sentences = ["I love NLP", "NLP is fun"]


vectorizer = CountVectorizer(ngram_range=(1, 2))  
X = vectorizer.fit_transform(sentences)

print(vectorizer.get_feature_names_out())
print(X.toarray())
