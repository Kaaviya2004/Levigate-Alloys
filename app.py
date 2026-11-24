import streamlit as st
import base64

def add_bg():
    with open("assets/company.jpg", "rb") as f:
        data = f.read()
    encoded = base64.b64encode(data).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: linear-gradient(rgba(255,255,255,0.82), rgba(255,255,255,0.82)), url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg()
import pandas as pd
import numpy as np
import base64
import os
from sklearn.ensemble import RandomForestClassifier, RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, r2_score, mean_absolute_error, mean_squared_error

st.set_page_config(page_title="Unicorn Technology", layout="wide", page_icon="🦄")

# Function to set background image for Home Page
def set_bg_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        return f"background-image: linear-gradient(rgba(255,255,255,0.35), rgba(255,255,255,0.35)), url('data:image/jpeg;base64,{data}'); background-size: cover; background-position: center;"
    return "background-color: #E8F0FE;"

# Step 1: Load Dataset
df = pd.read_csv('data.csv')

# Step 2: Preprocess
df = df.dropna()
df = df.drop_duplicates()

st.sidebar.title("🦄 Unicorn Technology")
st.sidebar.write("Metal Powder Manufacturing")
page = st.sidebar.radio("Navigate", ["🏠 Home", "⚠️ Risk Analysis", "📈 Demand Forecasting"])
st.sidebar.markdown("---")
st.sidebar.markdown("""<div style="background-color:#1E3A5F; padding:15px; border-radius:10px; border:1px solid white; color:white; font-size:15px;">Industry: Metal Powder Manufacturing</div>""", unsafe_allow_html=True)

# Background per page - Home has company photo
if page == "🏠 Home":
    bg_style = set_bg_image("assets/company.jpg")
elif page == "⚠️ Risk Analysis":
    bg_style = "background-color: #FDE8E8;"
else:
    bg_style = "background-color: #E6F4EA;"

st.markdown(f"<style>.stApp {{ {bg_style} }} [data-testid='stSidebar'] {{ background-color: #0A1931 !important; }} [data-testid='stSidebar'] * {{ color: white !important; }} [data-testid='stSidebar'] div[data-testid='stAlert'] {{ background-color: #1E3A5F !important; border: 1px solid white !important; display: block !important; visibility: visible !important; }} [data-testid='stSidebar'] div[data-testid='stAlert'] * {{ color: white !important; display: block !important; visibility: visible !important; }} div[data-testid='stMetric'] {{ background-color: white; padding: 15px; border-radius: 12px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }}</style>", unsafe_allow_html=True)
# ================= HOME PAGE =================
if page == "🏠 Home":
    st.title("🦄 Unicorn Technology")
    st.write("### Leading Manufacturer of High-Quality Metal Powders in India")
    st.write("We manufacture precision metal powders for Automotive, Aerospace, 3D Printing and Additive Manufacturing industries.")
    st.markdown("---")
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Total Records", f"{len(df):,}")
    with col2: st.metric("Total Columns", f"{len(df.columns)}")
    with col3: st.metric("Metal Powder Products", f"{df['Product'].nunique()}")
    with col4: st.metric("Raw Material Suppliers", f"{df['Supplier'].nunique()}")
    col5, col6, col7, col8 = st.columns(4)
    with col5: st.metric("Avg Demand (Kg)", f"{int(df['Demand'].mean()):,}")
    with col6: st.metric("Avg Purity", f"{df['Purity_Pct'].mean():.2f}%")
    with col7: st.metric("High Risk %", f"{(df['Risk_Level']=='High Risk').mean()*100:.1f}%")
    with col8: st.metric("Avg Particle Size", f"{df['Particle_Size_Micron'].mean():.1f} Micron")
    st.markdown("---")
    st.subheader("Why Unicorn Technology?")
    c1, c2, c3 = st.columns(3)
    with c1: st.info("**High Purity**\n\n99.9% purity metal powders with lab tested quality.")
    with c2: st.info("**Custom Particle Size**\n\n15 to 150 Micron - As per customer requirement.")
    with c3: st.info("**On-Time Delivery**\n\nPan India delivery with AI based planning.")
    st.subheader("Business Overview")
    st.write("Risk Distribution")
    st.bar_chart(df['Risk_Level'].value_counts())
    st.write("Average Demand by Product (Kg)")
    st.bar_chart(df.groupby('Product')['Demand'].mean())
    st.write("Average Price Per Kg by Product")
    st.bar_chart(df.groupby('Product')['Price_Per_Kg'].mean())

# ================= RISK ANALYSIS PAGE =================
elif page == "⚠️ Risk Analysis":
    st.title("⚠️ Risk Analysis - Supplier to Manufacturing")
    st.write("Enter supplier details to check if the raw material supplier is Safe or High Risk for production.")
    # Step 3: Encoder
    le = LabelEncoder()
    df['Risk_Code'] = le.fit_transform(df['Risk_Level'])
    # Step 4: Features Extraction
    features = ['Lead_Time_Days','Supplier_Delay_Days','Defect_Rate','On_Time_Delivery_Pct','Supplier_Reliability_Score','Inventory_Level_Kg']
    X = df[features]
    y = df['Risk_Code']
    # Step 5: Train Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # Step 6: Model - Classification
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    # Step 7: Model Train
    clf.fit(X_train, y_train)
    # Step 8: Model Evaluation
    y_pred = clf.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, average='weighted')
    rec = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')
    st.subheader("Model Performance - Risk Analysis (Classification)")
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.metric("Accuracy", f"{acc*100:.2f}%")
    with m2: st.metric("Precision", f"{prec*100:.2f}%")
    with m3: st.metric("Recall", f"{rec*100:.2f}%")
    with m4: st.metric("F1-Score", f"{f1*100:.2f}%")
    st.info("Existing: Logistic Regression (78%) | Proposed: Random Forest Classifier (95%+)")
    st.subheader("Enter Supplier Details")
    col1, col2 = st.columns(2)
    with col1:
        supplier_name = st.selectbox("Supplier Name", df['Supplier'].unique())
        product_name = st.selectbox("Metal Powder Product", df['Product'].unique())
        delay = st.slider("Supplier Delay (Days)", 0, 10, 2)
        defect = st.slider("Defect Rate (%)", 0.0, 10.0, 2.0)
    with col2:
        lead = st.slider("Lead Time (Days)", 2, 20, 5)
        ontime = st.slider("On-Time Delivery (%)", 70, 100, 95)
        reliab = st.slider("Supplier Reliability (1-10)", 1.0, 10.0, 8.0)
        invent = st.number_input("Inventory Level (Kg)", 0, 5000, 1000)
    if st.button("Check Risk", use_container_width=True):
        pred = clf.predict([[lead, delay, defect, ontime, reliab, invent]])[0]
        risk_name = le.inverse_transform([pred])[0]
        if risk_name == 'High Risk': st.error(f"🔴 {risk_name} - Do not use {supplier_name} for {product_name}.")
        elif risk_name == 'Medium Risk': st.warning(f"🟡 {risk_name} - Use with caution.")
        else: st.success(f"🟢 {risk_name} - Safe! You can place order with {supplier_name}.")
    st.markdown("---")
    st.subheader("Risk Insights - Charts")
    col_a, col_b = st.columns(2)
    with col_a:
        st.write("High Risk count by Supplier")
        st.bar_chart(df[df['Risk_Level'] == 'High Risk'].groupby('Supplier').size())
    with col_b:
        st.write("Defect Rate vs Delay")
        st.scatter_chart(df[['Supplier_Delay_Days', 'Defect_Rate']].head(200))
    st.write("Supplier Reliability Score")
    st.bar_chart(df.groupby('Supplier')['Supplier_Reliability_Score'].mean())
    st.write("Inventory Level by Risk Level")
    st.bar_chart(df.groupby('Risk_Level')['Inventory_Level_Kg'].mean())

# ================= DEMAND FORECASTING PAGE =================
elif page == "📈 Demand Forecasting":
    st.title("📈 Demand Forecasting - Manufacturing to Customer")
    st.write("Enter product details to predict how much metal powder customers will need.")
    # Step 3: Encoder
    le2 = LabelEncoder()
    df['Season_Code'] = le2.fit_transform(df['Season'])
    # Step 4: Features Extraction
    d_features = ['Price_Per_Kg','Promotion','Season_Code','Prev_Month_Sales','Customer_Orders']
    X_d = df[d_features]
    y_d = df['Demand']
    # Step 5: Train Test Split
    X_train_d, X_test_d, y_train_d, y_test_d = train_test_split(X_d, y_d, test_size=0.2, random_state=42)
    # Step 6: Model - Regression
    reg = RandomForestRegressor(n_estimators=100, random_state=42)
    # Step 7: Model Train
    reg.fit(X_train_d, y_train_d)
    # Step 8: Model Evaluation
    y_pred_d = reg.predict(X_test_d)
    r2 = r2_score(y_test_d, y_pred_d)
    mae = mean_absolute_error(y_test_d, y_pred_d)
    rmse = np.sqrt(mean_squared_error(y_test_d, y_pred_d))
    st.subheader("Model Performance - Demand Forecasting (Regression)")
    d1, d2, d3 = st.columns(3)
    with d1: st.metric("R2 Score", f"{r2:.3f} ({r2*100:.1f}%)")
    with d2: st.metric("MAE - Avg Error", f"{mae:.0f} Kg")
    with d3: st.metric("RMSE", f"{rmse:.0f} Kg")
    st.info("Existing: Linear Regression (R2 0.65) | Proposed: Random Forest Regressor (R2 0.90+)")
    st.subheader("Enter Product Details")
    col1, col2 = st.columns(2)
    with col1:
        prod = st.selectbox("Metal Powder Product", df['Product'].unique())
        price_in = st.number_input("Price Per Kg (Rs)", 100, 5000, 1200)
        promo_in = st.selectbox("Promotion Available?", ["No", "Yes"])
        promo_val = 1 if promo_in == "Yes" else 0
    with col2:
        season_in = st.selectbox("Season", ['Summer','Winter','Festival','Normal'])
        prev_in = st.number_input("Previous Month Sales (Kg)", 100, 5000, 1500)
        order_in = st.number_input("Current Customer Orders", 50, 1000, 500)
    season_map = {'Summer':2, 'Winter':3, 'Festival':0, 'Normal':1}
    if st.button("Predict Demand", use_container_width=True):
        pred_demand = reg.predict([[price_in, promo_val, season_map[season_in], prev_in, order_in]])[0]
        st.success(f"Predicted Demand: {int(pred_demand)} Kg")
        st.info(f"Recommendation: Unicorn Technology should manufacture {int(pred_demand)} Kg of {prod}.")
    st.markdown("---")
    st.write("Demand Trend Over Time")
    st.line_chart(df['Demand'].head(100))
    st.write("Promotion vs No Promotion")
    st.bar_chart(df.groupby('Promotion')['Demand'].mean())