import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
df= pd.read_csv('personality_quiz_training_data.csv')

# Split features and target
X= df.drop('Target', axis=1)
Y= df['Target']

# Convert text answers into numbers
X = X.apply(lambda col: col.astype('category').cat.codes)

# Split data for training and testing
X_train, X_test, Y_train, Y_test= train_test_split(X, Y, test_size=0.2, random_state=42)

# Train the model
model= RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train,Y_train)

# Check accuracy
accuracy= model.score(X_test, Y_test)
print("Model Trained Successfully!! Accuracy = {}".format(accuracy))

# Save the model to a file
with open("model_quiz.pkl", "wb") as f:
    pickle.dump(model, f)