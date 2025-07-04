import pandas as pd
import numpy as np
import random

# Seed für Reproduzierbarkeit
np.random.seed(42)
random.seed(42)

# Anzahl der Datenpunkte
n = 500

# Altersgruppen mit Wahrscheinlichkeiten
age_group_labels = ["16-20", "21-25", "26-30"]
age_probs = [0.288, 0.342, 0.37]

# Mapping Altersgruppe → konkrete Altersbereiche
age_ranges = {
    "16-20": list(range(16, 21)),
    "21-25": list(range(21, 26)),
    "26-30": list(range(26, 31))
}

# Altersgruppen zufällig wählen
age_groups = np.random.choice(age_group_labels, size=n, p=age_probs)

# Konkrete Einzelalter basierend auf der gewählten Gruppe
ages = [random.choice(age_ranges[group]) for group in age_groups]

# Geschlecht: 1 = männlich, 2 = weiblich
genders = np.random.choice([1, 2], size=n, p=[0.524, 0.476])

# Herkunft: 1 = Stadt, 2 = Land
origins = np.random.choice([1, 2], size=n, p=[0.185, 0.815])

# Beziehungsstatus abhängig vom Alter
relationship_status = []
for age in ages:
    if 16 <= age <= 20:
        status = np.random.choice([1, 2], p=[0.004, 0.996])
    elif 21 <= age <= 25:
        status = np.random.choice([1, 2], p=[0.036, 0.964])
    else:  # 26–30
        status = np.random.choice([1, 2], p=[0.167, 0.833])
    relationship_status.append(status)

# Bildung: 1 = ohne, 2 = Hauptschule, ..., 5 = Abitur
education_values = [1, 2, 3, 4, 5]
education_probs = np.array([0.025, 0.163, 0.307, 0.074, 0.432])
education_probs /= education_probs.sum()
education = np.random.choice(education_values, size=n, p=education_probs)

# Erwerbstätigkeit: 1 = ja, 2 = nein
employment = np.random.choice([1, 2], size=n, p=[0.63, 0.37])

# Einkommen: zufällig je nach Alter und Erwerbstätigkeit
def generate_income(age, employed):
    # Non-employed persons (employed=2) have limited income (max 6756€)
    if employed == 2:
        return random.randint(3000, 6756)
    
    # For employed persons (employed=1), income depends on age
    # Using median values as reference points: 
    # 16-24: 15400€ brutto median
    # 25-34: 41800€ brutto median
    
    # Apply a random multiplier between 0.75 and 1.25 to allow for variability
    multiplier = random.uniform(0.25, 1.75)
    
    if 16 <= age <= 24:
        # Base range around the median of 15400€
        base_income = random.randint(12500, 18500)
        
        # Small chance (5%) of a high income outlier
        if random.random() < 0.05:
            return int(random.randint(30000, 60000) * multiplier)
        return int(base_income * multiplier)
    else:  # 25-30
        base_income = random.randint(30000, 50000)
        # Base range around the median of 41800€ (for 25-34 age group)
        if random.random() < 0.05:
            return int(random.randint(60000, 80000) * multiplier)
        return int(base_income * multiplier)

income = [generate_income(age, employment[i]) for i, age in enumerate(ages)]

# Freizeitverhalten (2–4 Aktivitäten pro Person)
leisure_activities = [
    (1, 0.81), (2, 0.63), (3, 0.43), (4, 0.40), (5, 0.39),
    (6, 0.95), (7, 0.731), (8, 0.711), (9, 0.171), (10, 0.173), (11, 0.504)
]

def generate_leisure():
    selected = set()
    while len(selected) < random.randint(2, 4):
        activity, prob = random.choice(leisure_activities)
        if random.random() < prob:
            selected.add(activity)
    return list(selected)

leisure = [generate_leisure() for _ in range(n)]

# Gesundheitsbewusstsein: abhängig von Bildung und Geschlecht
def assign_health_conscious(edu_level, gender):
    base = 0.63 if gender == 1 else 0.51
    if edu_level == 5:  # Abitur
        base += 0.1
    return int(random.random() < min(base, 1.0))

health = [assign_health_conscious(education[i], genders[i]) for i in range(n)]

# DataFrame erzeugen
df = pd.DataFrame({
    "Index": range(1, n + 1),
    "Alter": ages,
    "Geschlecht": genders,
    "Herkunft": origins,
    "Beziehungsstatus": relationship_status,
    "Bildung": education,
    "Erwerbstätig": employment,
    "Einkommen": income,
    "Freizeit": leisure,
    "Gesundheitsbewusstsein": health
})

# CSV speichern
df.to_csv("../../data/erweiterter_persona_datensatz.csv", index=False)
print("✅ Datensatz erfolgreich gespeichert als 'erweiterter_persona_datensatz.csv'.")

# Vorschau
print(df.head())
