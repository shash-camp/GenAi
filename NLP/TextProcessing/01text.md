# 🔶 What is Text Processing?

**Text processing** in NLP means cleaning and converting **unstructured text** into a **structured format** so that machine learning models can understand and use it.

---

## 🔷 Step-by-Step Text Processing Pipeline

| Step | What it Does                              | Example                          |
|------|-------------------------------------------|----------------------------------|
| 1. Text Cleaning       | Remove noise like punctuation, symbols, etc. | `"Hello!!!"` → `"Hello"`       |
| 2. Lowercasing         | Normalize words                            | `"Hello"` → `"hello"`          |
| 3. Tokenization        | Split text into words or sentences         | `"I love AI"` → `["I", "love", "AI"]` |
| 4. Removing Stop Words | Remove frequent words with little meaning | `"the", "is", "a", etc.`       |
| 5. Stemming            | Cut word to its base form                 | `"running"` → `"run"`          |
| 6. Lemmatization       | Use dictionary to find actual root word   | `"better"` → `"good"`          |
| 7. Vectorization       | Convert text into numbers for modeling    | e.g., Word Embeddings, BoW     |

---

✅ After all these steps, the text is **ready to be used in an NLP model**.


