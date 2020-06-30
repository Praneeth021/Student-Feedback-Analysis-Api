import pandas as pd
import nltk
import re
from nltk.corpus import stopwords 
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer



db= pd.read_excel('./Dataset.xlsx')




ps= PorterStemmer()
corpus = []
wordnet=WordNetLemmatizer()
for i in range(0, len(db)):
    review = re.sub('[^a-zA-Z]', ' ', db['FeedBack'][i])
    review = review.lower()
    review = review.split()
    
    review = [wordnet.lemmatize(word) for word in review ]
    review = ' '.join(review)
    corpus.append(review)



from sklearn.feature_extraction.text import TfidfVectorizer
cv = TfidfVectorizer()
X = cv.fit_transform(corpus).toarray()
y=db['Label']



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.02, random_state = 42)



from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

model = MultinomialNB().fit(X_train, y_train)

y_pred=model.predict(X_test)
ac=accuracy_score(y_test,y_pred)


def pred(string):
    ps= PorterStemmer()
    wordnet=WordNetLemmatizer()
    review = re.sub('[^a-zA-Z]', ' ',string)
    review = review.lower()
    review = review.split()
    review = [wordnet.lemmatize(word) for word in review]
    review = ' '.join(review)
    X = cv.transform([review]).toarray()
    y=model.predict(X)

    return y[0]


