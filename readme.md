# 🚗 Best-Fit Car Finder (MVP)

A simple MVP car recommendation assistant that helps users find suitable car options based on:
- Budget  
- New/Used condition  
- Fuel preference  
- Usage purpose (City Commute, Family Trips, Budget, Luxury)

The system compares user inputs against a small curated catalog and ranks the best-fitting cars with short justifications.

---

# 📦 Features
- Lightweight rule-based scoring engine  
- Static catalog of common cars in Pakistan  
- Clear breakdown of "why this car?"  
- Interactive **Streamlit UI**  
- Command-line (CLI) version also included  

---

# 📁 Project Structure

project/
│
├── app.py # Streamlit UI version
├── car_finder.py # Command-line version (CLI)
├── README.md # Documentation
└── requirements.txt # Python dependencies



---

# 🛠 Requirements

Create a file named `requirements.txt` with the following:


Python 3.8+ recommended.

---

# ▶️ How to Run (Streamlit UI)

### **1. Install dependencies**
```bash
pip install -r requirements.txt
2. Run Streamlit app

streamlit run app.py

3. Open in browser

The app will open automatically.
If not, visit:
http://localhost:8501
▶️ How to Run (CLI Version)

python car_finder.py
The terminal will ask for:

Budget

Condition

Fuel type

Purpose

💡 Example Input/Output (CLI)

1. Max Budget (in Lacs): 50
2. Condition (New/Used/Any): New
3. Fuel Type (Petrol/Hybrid/Any): Petrol
4. Purpose (a/b/c/d): a   # City Commute

Example Output

--- TOP RECOMMENDATIONS ---

1. Suzuki Alto VXR
   Price: PKR 30 Lacs | Fuel: 20 km/l | New
   Why: Fits within budget, Excellent fuel economy, Compact size easy to park.
----------------------------------------

2. Suzuki Cultus VXL
   Price: PKR 45 Lacs | Fuel: 16 km/l | New
   Why: Fits within budget, Good city mileage, Low maintenance.
----------------------------------------

3. Suzuki Swift GLX CVT
   Price: PKR 58 Lacs | Fuel: 14 km/l | New
   Why: Slightly above budget but manageable, High comfort.
----------------------------------------
🧠 Scoring Logic Summary

The system evaluates cars based on:

Budget Fit

Fully within budget → +20

Condition

Matches user request → +15

Fuel Type

Direct match → +15

Purpose Scoring

Examples:
ity Commute

Fuel avg >= 18 → +25

Hatchback → +15

Low maintenance → +10

Family Trips

Medium/Large trunk → +20

Family friendly → +15

High comfort → +10

Budget/Economy

Low maintenance → +25

Very cheap cars → +15

Status/Luxury

Sedan/SUV → +15