Based on your **UseCases.md** for a car recommendation system, here’s a **TestPlan.md** with 5 test cases covering normal, positive, negative, and edge scenarios:

---

# Test Plan – Car Recommendation System

| Test Case ID | Test Type | Description                                 | Input                                                                             | Expected Result                                                                                                                        | Actual Result |
| ------------ | --------- | ------------------------------------------- | --------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| TC001        | Positive  | Normal flow – city commute car              | Budget: $15,000–20,000<br>Fuel: Petrol<br>Purpose: City Commute                   | System returns 3–5 cars optimized for compact size, fuel efficiency, and low maintenance                                               | Pending       |
| TC002        | Positive  | Normal flow – family trip car               | Budget: $30,000–40,000<br>Fuel: Hybrid<br>Purpose: Family Trips<br>Family size: 5 | System returns 3–5 cars with large seating, trunk space, and high safety ratings                                                       | Pending       |
| TC003        | Negative  | No car fits exact criteria                  | Budget: $10,000<br>Fuel: Electric<br>Purpose: Family Trips                        | System suggests nearest matches with notes like “slightly above budget”                                                                | Pending       |
| TC004        | Edge      | Very low-budget used car                    | Budget: $2,000<br>Condition: Used                                                 | System shows top used cars ranked by durability, maintenance, and resale strength; or suggests slightly older models if none available | Pending       |
| TC005        | Edge      | Extreme input – invalid budget or fuel type | Budget: -$5,000<br>Fuel: Water<br>Purpose: City Commute                           | System returns validation error messages: “Invalid budget” or “Unsupported fuel type”                                                  | Pending       |

---

This aligns with your **Use Cases**, testing:

* Normal positive flows (TC001 & TC002)
* Negative flows (TC003)
* Edge cases (TC004 & TC005)

If you want, I can also **expand this into a Markdown file with color-coded “Actual Result” status for easier QA tracking** and a checklist for each case.

Do you want me to do that?
