from sklearn.feature_extraction.text import TfidfVectorizer


documents = [
    "I love machine learning",  "Machine learning is amazing", "I love AI and machine learning"
]


vectorizer = TfidfVectorizer()


X = vectorizer.fit_transform(documents)


print("Feature Names:")
print(vectorizer.get_feature_names_out())  #Returns the list of words/features that were extracted from the documents.


print("\nTF-IDF Matrix:")
print(X.toarray())
