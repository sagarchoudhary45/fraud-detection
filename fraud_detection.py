import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE

# Load your dataset
data = pd.read_csv('transaction.csv')

# Step 2: Data Preprocessing

# Handle missing values
data = data.fillna(method='ffill')

# Convert datetime column to numerical values
if 'transaction_date' in data.columns:
    data['transaction_date'] = pd.to_datetime(data['transaction_date'])
    data['transaction_date'] = data['transaction_date'].astype(int) / 10**9  # Convert to seconds since epoch

# Feature scaling
scaler = StandardScaler()
data[['amount']] = scaler.fit_transform(data[['amount']])

# Handle imbalanced dataset
X = data.drop('is_fraud', axis=1)
y = data['is_fraud']

# Ensure all features are numerical
X = pd.get_dummies(X, drop_first=True)

smote = SMOTE()
X_resampled, y_resampled = smote.fit_resample(X, y)

# Step 3: Feature Engineering
# (Assuming some domain-specific features have been created)

# Step 4: EDA
import matplotlib.pyplot as plt
import seaborn as sns

# Example plot
plt.figure(figsize=(10, 6))
sns.histplot(data['amount'], bins=50, kde=True)
plt.title('Transaction Amount Distribution')
plt.show()

# Step 5: Model Selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier

# Initialize models
rf = RandomForestClassifier()
svm = SVC()
nn = MLPClassifier()

# Step 6: Model Training
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.3, random_state=42)

# Train models
rf.fit(X_train, y_train)
svm.fit(X_train, y_train)
nn.fit(X_train, y_train)

# Step 7: Model Evaluation
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score

# Make predictions
rf_preds = rf.predict(X_test)
svm_preds = svm.predict(X_test)
nn_preds = nn.predict(X_test)

# Evaluate models
def evaluate_model(preds, y_test):
    accuracy = accuracy_score(y_test, preds)
    precision = precision_score(y_test, preds)
    recall = recall_score(y_test, preds)
    f1 = f1_score(y_test, preds)
    roc_auc = roc_auc_score(y_test, preds)
    return accuracy, precision, recall, f1, roc_auc

rf_metrics = evaluate_model(rf_preds, y_test)
svm_metrics = evaluate_model(svm_preds, y_test)
nn_metrics = evaluate_model(nn_preds, y_test)

print(f"Random Forest Metrics: {rf_metrics}")
print(f"SVM Metrics: {svm_metrics}")
print(f"Neural Network Metrics: {nn_metrics}")
