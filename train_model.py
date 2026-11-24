# train_model.py - ML Model Training File
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score

# Step 1: Load Dataset
df = pd.read_csv('data.csv')

# Step 2: Preprocess
df = df.dropna()
df = df.drop_duplicates()

# ---- RISK MODEL ----
# Step 3: Encoder
le_risk = LabelEncoder()
df['Risk_Code'] = le_risk.fit_transform(df['Risk_Level'])

# Step 4: Features Extraction
features_risk = ['Lead_Time_Days','Supplier_Delay_Days','Defect_Rate','On_Time_Delivery_Pct','Supplier_Reliability_Score','Inventory_Level_Kg']
X_risk = df[features_risk]
y_risk = df['Risk_Code']

# Step 5: Train Test Split
X_train, X_test, y_train, y_test = train_test_split(X_risk, y_risk, test_size=0.2, random_state=42)

# Step 6: Model
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Step 7: Model Train
clf.fit(X_train, y_train)

# Step 8: Model Evaluation
print("Risk Model Accuracy:", accuracy_score(y_test, clf.predict(X_test)))
print("Train Model Done!")






# ---- DEMAND MODEL - REGRESSION ----
# Step 3: Encoder - Season ah number ah maathu
le_season = LabelEncoder()
df['Season_Code'] = le_season.fit_transform(df['Season'])

# Step 4: Features Extraction - Input (X) and Target (y)
features_demand = ['Price_Per_Kg','Promotion','Season_Code','Prev_Month_Sales','Customer_Orders']
X_d = df[features_demand]
y_d = df['Demand']

# Step 5: Train Test Split - 80% Train, 20% Test
X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_d, y_d, test_size=0.2, random_state=42)

# Step 6: Model - Random Forest Regressor
reg = RandomForestRegressor(n_estimators=100, random_state=42)

# Step 7: Model Train
reg.fit(X_train_d, y_train_d)

# Step 8: Model Evaluation - R2 Score
print("Demand Model R2:", r2_score(y_test_d, reg.predict(X_test_d)))
print("Both Models Done!")
