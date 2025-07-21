# Vector Embeddings

## What Are Vector Embeddings?

Vector embeddings are **numerical representations of data points** in a high-dimensional space.  
- **Similar data points** are closer together  
- **Dissimilar data points** are farther apart  
- This helps in understanding and identifying relationships between data  

For example:  
- The distance between words in vector space can show **semantic similarity**  
- Words like `Paris` and `Tokyo` are close, but far from `Apple`  

**Applications:**
- Widely used in Machine Learning and AI
- Helps process unstructured data like **text, images, audio, and videos**
- Commonly generated using **Neural Networks** or **Transformer-based models**

---

## How Are Vector Embeddings Created?

1. **Choose Data:**  
   Pick the data type (e.g., text, images, user info)

2. **Preprocess Data:**  
   - For text: remove stopwords, tokenize, and stem words  
   - For images: extract features using CNNs

3. **Use a Model:**  
   - Apply models like `Word2Vec`, `GloVe`, or deep learning models  
   - These learn to represent similar items with similar vectors

4. **Get Vector Space:**  
   - The model creates a space where similar items are near each other  
   - Dissimilar items are placed farther apart

---

## Types of Embeddings

### 🔷 Dense Embeddings
- Most values in the vector are **non-zero**
- Compact but **informative**
- Examples: `Word2Vec`, `GloVe`, `FastText`
- Good at capturing **semantic meaning**
- Used in: classification, similarity search, clustering

---

### 🔷 Sparse Embeddings
- Most values in the vector are **zero**
- Typically **larger** in size
- Represent whether a feature exists or not
- Examples: `TF-IDF`, `Bag-of-Words`
- Easier to interpret and used in **traditional ML**

---

### 🔷 Binary Embeddings
- Vector values are only `0` or `1`
- **Very compact** and fast
- Great for: fast searching (e.g., using LSH), feature hashing
- Efficient in **space** and **speed**

---
