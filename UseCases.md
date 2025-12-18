# UseCases.md

## 1. Use Case 1: Find Car for Daily City Commute

### Actor

User (buyer)

### Trigger

User wants a fuel-efficient, low-maintenance car for daily city use.

### Preconditions

-   User provides budget range
-   User specifies fuel preference and usage type

### Main Flow

1.  User enters budget, fuel type, and selects "City Commute".
2.  System filters catalog by budget and fuel.
3.  System assigns scores based on compact size, fuel efficiency, and
    maintenance ease.
4.  System displays top 3--5 recommendations.
5.  User views trade-offs and selects models to explore further.

### Alternate Flow

-   If no car fits the exact criteria, system suggests nearest matches
    with a note like "slightly above budget".

------------------------------------------------------------------------

## 2. Use Case 2: Find Car for Family Trips

### Actor

User (family buyer)

### Trigger

User wants a comfortable, spacious vehicle for long family travel.

### Preconditions

-   User shares family size and trunk space needs
-   Budget and fuel preference provided

### Main Flow

1.  User selects "Family Trips".
2.  System prioritizes cars with good trunk space, seating comfort, and
    safety.
3.  Score calculation boosts larger vehicles and hybrids where relevant.
4.  System presents recommendations with notes like "best for luggage"
    or "excellent safety rating".
5.  User views ranked list.

### Alternate Flow

-   If budget is tight, system recommends used options or nearest
    alternatives.

------------------------------------------------------------------------

## 3. Use Case 3: Find Low-Budget Used Car

### Actor

User (cost-conscious buyer)

### Trigger

User specifically wants a reliable used car under a limited budget.

### Preconditions

-   User selects "Used"
-   Budget is below typical new car prices

### Main Flow

1.  User enters low budget and selects "Used".
2.  System filters catalog for used models only.
3.  System ranks cars on durability, low maintenance, and resale
    strength.
4.  System displays top used options with explanations.
5.  User reviews trade-offs.

### Alternate Flow

-   If no used option fits budget, system suggests slightly older models
    or expands recommendations.

------------------------------------------------------------------------

# High-Level Design / Data Flow

## 1. Components

-   **User Interface**: Collects user inputs (budget, condition, fuel
    type, purpose).
-   **Car Catalog (Static JSON/Array)**: Contains attributes for \~20
    cars (price range, fuel, body type, trunk space, comfort, etc.).
-   **Scoring Engine**: Applies rules/weights to evaluate how well each
    car matches input.
-   **Recommendation Engine**: Sorts by score, formats explanation, and
    returns top results.

## 2. Data Flow (Simple)

    User Input
        ↓
    Input Parser
        ↓
    Car Catalog → Filtering Module → Scoring Engine → Ranking
                                                        ↓
                                               Recommendation Output
                                                        ↓
                                                     User

## 3. Design Notes

-   Scoring criteria include: budget fit, fuel preference match, purpose
    suitability, size, trunk space, and reliability.
-   Each car receives a "fit score" and "justification explanation".
-   The design is modular so catalog or scoring rules can be easily
    updated later.
