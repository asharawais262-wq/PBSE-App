import streamlit as st
import pandas as pd

# Page Config
st.set_page_config(
    page_title="Best-Fit Car Finder",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- DATA MODEL (Copied from logic to keep it self-contained for Streamlit cloud compatibility if needed) ---
class Car:
    def __init__(self, make, model, variant, price, year_range, condition, fuel_type, body_type, engine_cc, trunk_space, fuel_avg_city, maintenance_cost, comfort_score, is_family_friendly):
        self.make = make
        self.model = model
        self.variant = variant
        self.name = f"{make} {model} {variant}"
        self.price = price  # In PKR Lacs
        self.year_range = year_range 
        self.condition = condition 
        self.fuel_type = fuel_type 
        self.body_type = body_type 
        self.engine_cc = engine_cc
        self.trunk_space = trunk_space 
        self.fuel_avg_city = fuel_avg_city 
        self.maintenance_cost = maintenance_cost 
        self.comfort_score = comfort_score 
        self.is_family_friendly = is_family_friendly

CAR_CATALOG = [
    Car("Suzuki", "Alto", "VXR", 30.0, "2024", "New", "Petrol", "Hatchback", 660, "Small", 20, "Low", 5, False),
    Car("Suzuki", "Alto", "VXL AGS", 35.0, "2024", "New", "Petrol", "Hatchback", 660, "Small", 19, "Low", 6, False),
    Car("Suzuki", "Cultus", "VXL", 45.0, "2024", "New", "Petrol", "Hatchback", 1000, "Small", 16, "Low", 6, True),
    Car("Suzuki", "Swift", "GLX CVT", 58.0, "2024", "New", "Petrol", "Hatchback", 1200, "Small", 14, "Medium", 7, False),
    Car("Toyota", "Vitz", "F 1.0", 35.0, "2018-2020", "Used", "Petrol", "Hatchback", 1000, "Small", 15, "Medium", 7, False),
    Car("Daihatsu", "Mira", "ES", 28.0, "2018-2020", "Used", "Petrol", "Hatchback", 660, "Small", 22, "Medium", 6, False),
    Car("Toyota", "Yaris", "ATIV CVT", 63.0, "2024", "New", "Petrol", "Sedan", 1300, "Medium", 14, "Medium", 7, True),
    Car("Honda", "City", "1.2 CVT", 60.0, "2024", "New", "Petrol", "Sedan", 1200, "Medium", 13, "Medium", 7, True),
    Car("Toyota", "Corolla", "Altis 1.6", 75.0, "2024", "New", "Petrol", "Sedan", 1600, "Medium", 11, "Medium", 8, True),
    Car("Honda", "Civic", "Oriel", 95.0, "2024", "New", "Petrol", "Sedan", 1500, "Medium", 11, "High", 9, True),
    Car("Changan", "Alsvin", "Lumiere", 48.0, "2024", "New", "Petrol", "Sedan", 1500, "Medium", 13, "Medium", 7, True),
    Car("Toyota", "Corolla", "GLI", 38.0, "2016-2018", "Used", "Petrol", "Sedan", 1300, "Medium", 12, "Medium", 7, True),
    Car("Honda", "City", "Aspire 1.5", 35.0, "2015-2017", "Used", "Petrol", "Sedan", 1500, "Medium", 12, "Medium", 7, True),
    Car("Kia", "Sportage", "FWD", 85.0, "2024", "New", "Petrol", "SUV", 2000, "Large", 10, "High", 9, True),
    Car("Toyota", "Corolla Cross", "Hybrid", 120.0, "2024", "New", "Hybrid", "SUV", 1800, "Large", 18, "Medium", 9, True),
    Car("Haval", "H6", "HEV", 125.0, "2024", "New", "Hybrid", "SUV", 1500, "Large", 16, "High", 10, True),
    Car("Honda", "Vezel", "Hybrid Z", 65.0, "2016-2018", "Used", "Hybrid", "SUV", 1500, "Medium", 16, "High", 8, False),
    Car("Suzuki", "Mehran", "VX", 12.0, "2015-2018", "Used", "Petrol", "Hatchback", 800, "Small", 14, "Low", 3, False),
    Car("Suzuki", "Cultus", "Euro II", 18.0, "2015-2016", "Used", "Petrol", "Hatchback", 1000, "Small", 13, "Low", 4, False),
]

def calculate_score(car, inputs):
    score = 0
    justifications = []
    
    # Budget
    budget = inputs['budget']
    if car.price <= budget:
        score += 20
        justifications.append("✅ Fits Budget")
    elif car.price <= budget * 1.15:
        score += 5
        justifications.append("⚠️ Slightly over budget")
    else:
        return -1, []

    # Condition
    if inputs['condition'] != "Any":
        if car.condition == inputs['condition']:
             score += 15
        else:
            score -= 20

    # Fuel
    if inputs['fuel'] != "Any":
        if car.fuel_type == inputs['fuel']:
            score += 15
        else:
            score -= 10
            
    # Purpose
    purpose = inputs['purpose']
    if purpose == "City Commute":
        if car.fuel_avg_city >= 18: score += 25; justifications.append("⛽ Amazing Fuel Avg")
        elif car.fuel_avg_city >= 15: score += 10
        if car.body_type == "Hatchback": score += 15; justifications.append("🅿️ Easy to Park")
        
    elif purpose == "Family Trips":
        if car.trunk_space in ["Medium", "Large"]: score += 20; justifications.append("🧳 Good Trunk Space")
        if car.is_family_friendly: score += 15; justifications.append("👨‍👩‍👧‍👦 Family Friendly")
        if car.comfort_score >= 8: score += 10; justifications.append("🛋️ Very Comfortable")

    elif purpose == "Budget/Economy":
        if car.maintenance_cost == "Low": score += 25; justifications.append("🔧 Low Maintenance")
        if car.price < 20: score += 15; justifications.append("💰 Very Affordable")

    elif purpose == "Status/Luxury":
        if car.body_type in ["Sedan", "SUV"]: score += 20
        if car.price > 60: score += 15; justifications.append("💎 Premium Feel")

    return score, justifications

# --- UI ---
st.title("🚗 Best-Fit Car Finder")
st.markdown("Your smart assistant to find the perfect car in Pakistan.", unsafe_allow_html=True)

with st.sidebar:
    st.header("🎯 Your Preferences")
    
    budget = st.slider("Max Budget (PKR Lacs)", 10, 150, 50, step=5)
    
    condition = st.radio("Condition", ["Any", "New", "Used"], horizontal=True)
    
    fuel = st.selectbox("Fuel Preference", ["Any", "Petrol", "Hybrid"])
    
    purpose = st.selectbox("Main Purpose", 
        ["City Commute", "Family Trips", "Budget/Economy", "Status/Luxury"]
    )
    
    st.markdown("---")
    st.caption("Adjust sliders to see real-time updates!")

# Logic
inputs = {
    'budget': budget,
    'condition': condition,
    'fuel': fuel,
    'purpose': purpose
}

results = []
for car in CAR_CATALOG:
    score, reasons = calculate_score(car, inputs)
    if score > 0:
        results.append((car, score, reasons))

results.sort(key=lambda x: x[1], reverse=True)

# Display
if not results:
    st.warning("No cars found matching your criteria. Try increasing your budget.")
else:
    st.subheader(f"We found {len(results)} matches for you!")
    st.markdown("---")
    
    for car, score, reasons in results[:5]: # Top 5
        with st.container():
            col1, col2 = st.columns([1, 3])
            
            with col1:
                # Placeholder image based on body type
                if car.body_type == "SUV":
                    st.write("🚙 **SUV**")
                elif car.body_type == "Sedan":
                    st.write("🚗 **Sedan**")
                else:
                    st.write("🚕 **Hatchback**")
                
                st.metric("Price", f"{car.price} Lacs", delta_color="off")
            
            with col2:
                st.subheader(f"{car.name} ({car.year_range})")
                st.caption(f"Fuel: {car.fuel_avg_city} km/l | {car.condition} | {car.engine_cc}cc")
                
                # Tags
                tags_html = ""
                for r in reasons:
                    tags_html += f'<span style="background-color:#e0f2f1; color:#00695c; padding:4px 8px; border-radius:12px; margin-right:5px; font-size:0.85em;">{r}</span>'
                st.markdown(tags_html, unsafe_allow_html=True)
            
            st.divider()

st.info("💡 Tip: Prices are market estimates and can vary.")
