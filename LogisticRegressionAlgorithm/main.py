import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


par_df = pd.read_csv("data.csv", index_col=0)

train_df, test_df = train_test_split(par_df, test_size=0.2)
# print(par_df.shape)
# print(train_df.shape)
# print(test_df.shape)

# train_df.info()

train_df = train_df.drop(columns=["img_filename"])
test_df = test_df.drop(columns=["img_filename"])

X_train, y_train = train_df.drop(columns=["Parkinson"]), train_df['Parkinson']
X_test, y_test = test_df.drop(columns=["Parkinson"]), test_df['Parkinson']

# print(y_train)

model = LogisticRegression()
model.fit(X_train, y_train)

predict = model.predict(X_test)
# print(predict)

pred_result = test_df
pred_result['predicted'] = predict.tolist()

accuracy = accuracy_score(y_test, predict)
print(accuracy)