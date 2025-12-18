Bilkul — neeche **TestPlan.md** ka complete content seedha text form mén de raha hoon.
Aap ise copy karke khud `.md` file bana sakte ho.

---

# **TestPlan.md**

## **1. Test Case 1 – Normal Case (City Commute)**

### **Input**

* Budget: 50 Lacs
* Condition: New
* Fuel: Petrol
* Purpose: City Commute

### **Expected Result**

* System 3–5 cars show kare (Alto, Cultus, Swift etc.).
* High fuel average wali hatchbacks top score lein.
* Koi error ya crash na ho.

### **Actual Result**

* *To be tested*

---

## **2. Test Case 2 – Positive Case (Family Trips)**

### **Input**

* Budget: 80 Lacs
* Condition: Any
* Fuel: Any
* Purpose: Family Trips

### **Expected Result**

* System sedans/SUVs show kare (Corolla, Yaris, Sportage etc.).
* “Family Friendly”, “Good Trunk Space”, “Comfortable Ride” jaise tags appear hon.

### **Actual Result**

* *To be tested*

---

## **3. Test Case 3 – Negative Case (Very Low Budget)**

### **Input**

* Budget: 5 Lacs
* Condition: Any
* Fuel: Any
* Purpose: Budget/Economy

### **Expected Result**

* Koi car match na kare.
* System warning show kare:
  **“No cars found matching your criteria. Try increasing your budget.”**

### **Actual Result**

* *To be tested*

---

## **4. Test Case 4 – Edge Case (Budget Slightly Below Price)**

### **Input**

* Budget: 30 Lacs
* Condition: New
* Fuel: Petrol
* Purpose: City Commute

### **Expected Result**

* Alto (30 Lacs) direct show ho.
* Cars priced 34–35 Lacs ko “Slightly over budget” ke saath show kare.
* 35 Lacs se upar wali cars skip hon.

### **Actual Result**

* *To be tested*

---

## **5. Test Case 5 – Conflicting Filters (Hybrid + Low Budget)**

### **Input**

* Budget: 20 Lacs
* Condition: New
* Fuel: Hybrid
* Purpose: City Commute

### **Expected Result**

* 20 Lacs ke budget me hybrid car exist nahi karti → empty result.
* System warning message show kare.

### **Actual Result**

* *To be tested*

---

