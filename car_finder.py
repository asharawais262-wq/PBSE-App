import sys

class Car:
    def __init__(self, make, model, variant, price, year_range, condition, fuel_type, body_type, engine_cc, trunk_space, fuel_avg_city, maintenance_cost, comfort_score, is_family_friendly):
        self.make = make
        self.model = model
        self.variant = variant
        self.name = f"{make} {model} {variant}"
        self.price = price  # In PKR Lacs (approx formatted as float e.g. 35.5)
        self.year_range = year_range # String e.g. "2019-2023"
        self.condition = condition # "New" or "Used"
        self.fuel_type = fuel_type # "Petrol", "Hybrid", "Electric"
        self.body_type = body_type # "Hatchback", "Sedan", "SUV", "Crossover"
        self.engine_cc = engine_cc
        self.trunk_space = trunk_space # Small, Medium, Large
        self.fuel_avg_city = fuel_avg_city # km/l
        self.maintenance_cost = maintenance_cost # Low, Medium, High
        self.comfort_score = comfort_score # 1-10
        self.is_family_friendly = is_family_friendly # Boolean

    def __repr__(self):
        return f"{self.name} ({self.condition}) - {self.price} Lacs"

# --- STATIC CATALOG (Approximate Market Data) ---
# Prices are rough estimates in PKR Lacs as of late 2024/2025 context
CAR_CATALOG = [
    # HATCHBACKS
    Car("Suzuki", "Alto", "VXR", 30.0, "2024", "New", "Petrol", "Hatchback", 660, "Small", 20, "Low", 5, False),
    Car("Suzuki", "Alto", "VXL AGS", 35.0, "2024", "New", "Petrol", "Hatchback", 660, "Small", 19, "Low", 6, False),
    Car("Suzuki", "Cultus", "VXL", 45.0, "2024", "New", "Petrol", "Hatchback", 1000, "Small", 16, "Low", 6, True),
    Car("Suzuki", "Swift", "GLX CVT", 58.0, "2024", "New", "Petrol", "Hatchback", 1200, "Small", 14, "Medium", 7, False),
    Car("Toyota", "Vitz", "F 1.0", 35.0, "2018-2020", "Used", "Petrol", "Hatchback", 1000, "Small", 15, "Medium", 7, False),
    Car("Daihatsu", "Mira", "ES", 28.0, "2018-2020", "Used", "Petrol", "Hatchback", 660, "Small", 22, "Medium", 6, False),

    # SEDANS
    Car("Toyota", "Yaris", "ATIV CVT", 63.0, "2024", "New", "Petrol", "Sedan", 1300, "Medium", 14, "Medium", 7, True),
    Car("Honda", "City", "1.2 CVT", 60.0, "2024", "New", "Petrol", "Sedan", 1200, "Medium", 13, "Medium", 7, True),
    Car("Toyota", "Corolla", "Altis 1.6", 75.0, "2024", "New", "Petrol", "Sedan", 1600, "Medium", 11, "Medium", 8, True),
    Car("Honda", "Civic", "Oriel", 95.0, "2024", "New", "Petrol", "Sedan", 1500, "Medium", 11, "High", 9, True),
    Car("Changan", "Alsvin", "Lumiere", 48.0, "2024", "New", "Petrol", "Sedan", 1500, "Medium", 13, "Medium", 7, True),
    Car("Toyota", "Corolla", "GLI", 38.0, "2016-2018", "Used", "Petrol", "Sedan", 1300, "Medium", 12, "Medium", 7, True),
    Car("Honda", "City", "Aspire 1.5", 35.0, "2015-2017", "Used", "Petrol", "Sedan", 1500, "Medium", 12, "Medium", 7, True),

    # SUVS / CROSSOVERS
    Car("Kia", "Sportage", "FWD", 85.0, "2024", "New", "Petrol", "SUV", 2000, "Large", 10, "High", 9, True),
    Car("Toyota", "Corolla Cross", "Hybrid", 120.0, "2024", "New", "Hybrid", "SUV", 1800, "Large", 18, "Medium", 9, True),
    Car("Haval", "H6", "HEV", 125.0, "2024", "New", "Hybrid", "SUV", 1500, "Large", 16, "High", 10, True),
    Car("Honda", "Vezel", "Hybrid Z", 65.0, "2016-2018", "Used", "Hybrid", "SUV", 1500, "Medium", 16, "High", 8, False),

    # LOW BUDGET / USED
    Car("Suzuki", "Mehran", "VX", 12.0, "2015-2018", "Used", "Petrol", "Hatchback", 800, "Small", 14, "Low", 3, False),
    Car("Suzuki", "Cultus", "Euro II", 18.0, "2015-2016", "Used", "Petrol", "Hatchback", 1000, "Small", 13, "Low", 4, False),
]

def calculate_suitability_score(car, inputs):
    score = 0
    justifications = []

    # 1. Budget Fit (Hard Filter mostly handled before, but add weighting for being well under budget)
    # If car is > budget + 10%, score is -100 (effectively filtering it out if not strict)
    # We will assume pre-filtering, but allow small wiggle room
    user_max_budget = inputs['budget_max']
    if car.price <= user_max_budget:
        score += 20
        justifications.append("Fits within budget")
    elif car.price <= user_max_budget * 1.1:
        score += 5
        justifications.append("Slightly above budget but manageable")
    else:
        return -100, [] # Too expensive

    # 2. Condition Match
    if inputs['condition'].lower() != "any":
        if car.condition.lower() == inputs['condition'].lower():
            score += 15
            justifications.append(f"Is {car.condition} as requested")
        else:
            score -= 20 # Penalty but not exclusion

    # 3. Fuel Type Match
    if inputs['fuel_type'].lower() != "any":
        if car.fuel_type.lower() == inputs['fuel_type'].lower():
            score += 15
            justifications.append(f"Matches {inputs['fuel_type']} preference")
        else:
             # If user wants Hybrid but car is Petrol, penalty
             score -= 10

    # 4. Purpose-based Scoring
    purpose = inputs['purpose'].lower()
    
    if "city" in purpose:
        # Prioritize Fuel Eff, Size, Low Maint
        if car.fuel_avg_city >= 18:
            score += 25
            justifications.append("Excellent fuel economy for city")
        elif car.fuel_avg_city >= 14:
            score += 10
        
        if car.body_type == "Hatchback":
            score += 15
            justifications.append("Compact size easy to park")
        
        if car.maintenance_cost == "Low":
            score += 10
            justifications.append("Low maintenance costs")

    elif "family" in purpose or "trip" in purpose:
        # Prioritize Trunk, Comfort, Family Friendly
        if car.trunk_space in ["Medium", "Large"]:
            score += 20
            justifications.append("Good trunk space for luggage")
        
        if car.is_family_friendly:
            score += 15
            justifications.append("Family-friendly seating")
        
        if car.comfort_score >= 7:
            score += 10
            justifications.append("Comfortable ride")
            
    elif "status" in purpose or "luxury" in purpose:
        if car.price > 60:
             score += 10
        if car.body_type in ["Sedan", "SUV"]:
            score += 15
            justifications.append("Premium body style")
        if car.comfort_score >= 8:
            score += 15
            justifications.append("High comfort level")

    return score, justifications

def format_price(acs):
    return f"PKR {acs} Lacs"

def main():
    print("--------------------------------------------------")
    print("Welcome to the Best-Fit Car Finder MVP Assistant")
    print("--------------------------------------------------")
    
    # --- INPUT COLLECTION ---
    try:
        print("\nPlease enter your constraints:")
        budget_input = input("1. Max Budget (in Lacs, e.g. 30, 45.5): ").strip()
        if not budget_input:
            budget_input = "50" # Default
        budget_max = float(budget_input)

        condition_input = input("2. Condition (New, Used, Any): ").strip()
        if not condition_input: 
            condition_input = "Any"

        fuel_input = input("3. Fuel Type (Petrol, Hybrid, Electric, Any): ").strip()
        if not fuel_input:
            fuel_input = "Any"
            
        print("4. Main Purpose?")
        print("   (a) Daily City Commute")
        print("   (b) Family Trips / Long Travel")
        print("   (c) Budget / Economy")
        print("   (d) Status / Luxury")
        purpose_choice = input("   Enter choice (a/b/c/d) or type custom: ").strip().lower()
        
        purpose_map = {
            'a': 'city commute',
            'b': 'family trips',
            'c': 'budget',
            'd': 'status'
        }
        purpose = purpose_map.get(purpose_choice, purpose_choice)

    except ValueError:
        print("Invalid input format. Please restart.")
        return

    user_inputs = {
        'budget_max': budget_max,
        'condition': condition_input,
        'fuel_type': fuel_input,
        'purpose': purpose
    }
    
    print(f"\nSearching for: Budget ~{budget_max} Lacs, {condition_input}, {fuel_input}, for '{purpose}'...")

    # --- PROCESSING ---
    results = []
    
    for car in CAR_CATALOG:
        # Pre-filter loosely by strict max limits to avoid showing cars 2x the budget
        # We allow 15% stretch for visibility but score them low
        if car.price > budget_max * 1.15:
            continue
            
        score, justifications = calculate_suitability_score(car, user_inputs)
        
        if score > 0:
            results.append({
                'car': car,
                'score': score,
                'reasons': justifications
            })

    # Sort by score descending
    results.sort(key=lambda x: x['score'], reverse=True)

    # --- OUTPUT ---
    print("\n--- TOP RECOMMENDATIONS ---\n")
    
    if not results:
        print("No exact matches found. Try increasing budget or adjusting filters.")
    else:
        top_n = results[:5]
        for i, res in enumerate(top_n, 1):
            car = res['car']
            reasons = ", ".join(res['reasons'][:3]) # Take top 3 reasons
            print(f"{i}. {car.name}")
            print(f"   Price: {format_price(car.price)} | Fuel: {car.fuel_avg_city} km/l | {car.condition}")
            print(f"   Why: {reasons}.")
            print("-" * 40)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
