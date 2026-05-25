import pandas as pd
import joblib

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

from preprocessing import clean_text


# LOAD DATASETS
fake_df = pd.read_csv(r"C:\AI_DATASET\Fake.csv")
true_df = pd.read_csv(r"C:\AI_DATASET\True.csv")


# KEEP ONLY TEXT COLUMN
fake_df = fake_df[['text']]
true_df = true_df[['text']]


# ADD LABELS
fake_df['label'] = 'rumor'
true_df['label'] = 'non-rumor'


# COMBINE DATASETS
df = pd.concat([fake_df, true_df])


# CLEAN TEXT
df['clean_text'] = df['text'].apply(clean_text)


# FEATURES
X = df['clean_text']

# LABELS
y = df['label']


# TF-IDF
vectorizer = TfidfVectorizer(max_features=5000)

X_vectorized = vectorizer.fit_transform(X)


# TRAIN TEST SPLIT
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)


# SVM MODEL
model = SVC(probability=True)

model.fit(X_train, y_train)


# PREDICTIONS
y_pred = model.predict(X_test)


# ACCURACY
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")


# SAVE MODEL
joblib.dump(model, 'model/svm_model.pkl')

joblib.dump(vectorizer, 'model/tfidf_model.pkl')

print("Model Saved Successfully")