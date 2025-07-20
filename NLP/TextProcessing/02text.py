# Run this once to create the file
text_data = """1. <p>THIS is an EXAMPLE of TEXT inside a PARAGRAPH tag.</p>
2. <div>Hello WORLD! This TEXT contains UPPERCASE and html tags.</div>
3. <b>IMPORTANT:</b> PLEASE read the INSTRUCTIONS carefully.
4. <span class="note">NOTE:</span> ALL CAPS ARE USED here to grab attention.
5. <h1>WELCOME to the MACHINE LEARNING Course</h1>
6. This is a NORMAL sentence without tags but WITH UPPERCASE WORDS.
7. <a href="https://example.com">CLICK HERE</a> to VISIT OUR SITE.
8. <ul><li>FIRST ITEM</li><li>SECOND ITEM</li></ul>
9. <script>alert('IGNORE THIS SCRIPT');</script> This is ACTUAL CONTENT.
10. <p>THANK YOU for USING our PLATFORM</p>"""

with open("data.txt", "w", encoding="utf-8") as f:
    f.write(text_data)

import re    

# Step 1: Read from file
with open("data.txt", "r", encoding="utf-8") as file:
    data = file.read()


# Step 2: Remove HTML tags using regex
cleanedtext = re.sub(r"<.*?>", "", data)

# Step 3: Convert to lowercase
cleanedtext = cleanedtext.lower()

# Step 4: Remove extra whitespace
cleanedtext = cleanedtext.strip()

# Step 5: Print cleaned result
#print(cleanedtext)


href ="Shashankhttps://example.com"
removed_url = re.sub(r'(https?://[a-zA-Z0-9./?=#_%-]+)', '', href)
# print(removed_url)

import string

exclude=string.punctuation

def remove_pun(data):
    for char in data:
        text=data.replace(char,'')
        return text
    
# print(remove_pun(data))



# SPELLING CORRECTION

from textblob import TextBlob

incorrect_text = "My nmae is Shashank Sngh recently passed from galgotias college of engineerring"
textBlb = TextBlob(incorrect_text)
message = textBlb.correct().string
# print(message)

# STOP WORLD REMOVAL

from nltk.corpus import stopwords



 

def remove_stpwords(text):
    stop_words = set(stopwords.words('english'))
    new_text = []

    for word in text.split():
        if word.lower() not in stop_words:
            new_text.append(word)

    return " ".join(new_text)

# print(remove_stpwords(incorrect_text))


####  TOKENIZATION


import spacy


nlp = spacy.load('en_core_web_sm')

text = "This is a sample sentence, showing off spaCy capabilities."


doc = nlp(text)




# for token in doc:
#     print(token.text, token.lemma_)

## STEMMING
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

words = ["playing", "played", "plays", "player", "study", "studies","better"]

# for word in words:
#     print(f"{word} → {stemmer.stem(word)}")



### LEMMATIZATION
import nltk
nltk.download('wordnet')
nltk.download('omw-1.4')

from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

words = ["running", "studies", "was", "mice", "better"]

for word in words:
    print(f"{word} → {lemmatizer.lemmatize(word)}")
