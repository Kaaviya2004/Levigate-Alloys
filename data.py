import random
from datetime import datetime, timedelta
import pandas as pd
random.seed(42)

products = ['Stainless Steel Powder', 'Aluminium Powder', 'Copper Powder', 'Iron Powder', 'Nickel Powder', 'Titanium Powder']
suppliers = ['MetalCorp India', 'PowderTech Ltd', 'Global Metals', 'Shakti Alloys', 'Prime Powder Co']
seasons = ['Summer', 'Winter', 'Festival', 'Normal']

product_info = {
    'Stainless Steel Powder': {'base_demand': 2800, 'price': 1200},
    'Aluminium Powder': {'base_demand': 3500, 'price': 650},
    'Copper Powder': {'base_demand': 2200, 'price': 1800},
    'Iron Powder': {'base_demand': 4200, 'price': 450},
    'Nickel Powder': {'base_demand': 1500, 'price': 2800},
    'Titanium Powder': {'base_demand': 800, 'price': 3500}
}

data = []
start_date = datetime(2024, 1, 1)
for i in range(10000):
    product = random.choice(products)
    supplier = random.choice(suppliers)
    season = random.choice(seasons)
    info = product_info[product]
    particle_size = round(random.uniform(15, 150), 2)
    purity_pct = round(random.uniform(97.0, 99.9), 2)
    lead_time = random.randint(3, 18)
    delay = random.randint(0, 8)
    defect_rate = round(random.uniform(0.5, 6.0), 2)
    on_time = round(random.uniform(82, 100), 1)
    reliability = round(random.uniform(5.0, 9.8), 1)
    inventory = random.randint(200, 5000)
    price_per_kg = info['price'] + random.randint(-100, 100)
    promotion = random.choice([0, 1])
    prev_sales = int(info['base_demand'] + random.randint(-500, 500))
    orders = random.randint(50, 800)
    demand = int(info['base_demand'] * 0.7 + orders * 0.8 + (400 if promotion == 1 else 0) + random.randint(-200, 300))
    if defect_rate > 4.5 or delay > 5 or purity_pct < 97.5:
        risk = 'High Risk'
    elif defect_rate > 2.5 or delay > 2:
        risk = 'Medium Risk'
    else:
        risk = 'Low Risk'
    data.append([start_date + timedelta(days=i % 365), product, supplier, season, particle_size, purity_pct, lead_time, delay, defect_rate, on_time, reliability, inventory, price_per_kg, promotion, prev_sales, orders, demand, risk])

columns = ['Date','Product','Supplier','Season','Particle_Size_Micron','Purity_Pct','Lead_Time_Days','Supplier_Delay_Days','Defect_Rate','On_Time_Delivery_Pct','Supplier_Reliability_Score','Inventory_Level_Kg','Price_Per_Kg','Promotion','Prev_Month_Sales','Customer_Orders','Demand','Risk_Level']
df = pd.DataFrame(data, columns=columns)
df.to_csv('data.csv', index=False)
print("Done! 10000 records created")
print(df['Risk_Level'].value_counts())