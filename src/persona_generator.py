from models.api_connection import api_call
import pandas as pd
import json

def main():
    # Load the datasets
    personas = pd.read_csv('../data/erweiterter_persona_datensatz.csv')
    encodings = pd.read_csv('../data/Encodings_f_r_den_Datensatz.csv')
    names = pd.read_csv('../data/Namenliste__500_Eintr_ge_.csv')
    
    # Get unique categories from encodings
    categories = encodings['Kategorie'].unique()
    
    # Create mapping dictionary for each category
    for category in categories:
        if category == 'Freizeit':
            # Handle Freizeit separately as it's a list of codes
            continue
            
        # Create mapping for this category
        category_mapping = dict(zip(
            encodings[encodings['Kategorie'] == category]['Code'],
            encodings[encodings['Kategorie'] == category]['Bedeutung']
        ))
        
        # Apply mapping to the corresponding column
        if category in personas.columns:
            personas[category] = personas[category].map(category_mapping)
    
    # Special handling for Freizeit which contains lists of codes
    freizeit_mapping = dict(zip(
        encodings[encodings['Kategorie'] == 'Freizeit']['Code'].astype(str),  # Convert codes to strings
        encodings[encodings['Kategorie'] == 'Freizeit']['Bedeutung']
    ))
    
    # Convert string representation of list to actual list and map values
    personas['Freizeit'] = personas['Freizeit'].apply(eval).apply(
        lambda x: [freizeit_mapping.get(str(code), code) for code in x]
    )

    with open("../data/output_format_persona.json", "r") as f:
        persona = json.load(f)

    # Initialize an empty list to store results
    result_list = []
    # Track chosen beer preferences
    chosen_beers = []

    # Loop through the first 500 rows of personas and names
    for i in range(0,499):
        df_row = personas.iloc[i]
        name = names.iloc[i]

        persona["gender"] = df_row["Geschlecht"]
        persona["age"] = df_row["Alter"]
        persona["income"] = df_row["Einkommen"]
        persona["education"] = df_row["Bildung"]
        persona["employment"] = df_row["Erwerbstätig"]
        persona["leisure"] = df_row["Freizeit"]
        persona["marriage_status"] = df_row["Beziehungsstatus"]
        persona["health_conscious"] = df_row["Gesundheitsbewusstsein"]
        message = [
            {
                "role": "user",
                "content":(
                    f"Erstelle mir für folgende Daten eine "
                    f"ausführliche Persona die an einer Marktforschung teilnehmen kann. Du darfst gerne noch "
                    f"zusätzliche Vorlieben und Informationen hinzufügen. Es handelt sich bei der Person um eine "
                    f"Person aus der Generation Z aus dem deutschen Bundesland Baden Württemberg. Nutze die geografische"
                    f"Herkunft um ein Bier passend zu der Person zu wählen. Du kannst hier die allgemeinen Vorlieben der "
                    f"deutschen für Biermarken nutzen um ein passendes Bier für die Person zu wählen. Füge dies "
                    f"als beer_preference als eine Beschreibung über den Biertyp in die JSON ein. "
                    f"Die Informationen findest du in dem JSON: {persona}, bitte füge die zusätzlichen "
                    f"Informationen in die JSON ein und gib in der selben JSON-Datei zurück! "
                    f"Du brauchs nichts erläutern und ersetze das x in persona_x durch {i} "
                    f"Der Nachname ist: {name['Nachname']}. "
                    f"Folgende Bierpräferenzen wurden bereits gewählt, bringe eine gewisse Varianz in die Auswahl:"
                    f"{', '.join(chosen_beers) if chosen_beers else 'Keine'}."
                )
            }
        ]
        response = api_call(message)
        # Clean the response: remove markdown code block and parse JSON
        cleaned_response = response.strip().replace('```json', '').replace('```', '').strip()
        try:
            json_response = json.loads(cleaned_response)
            # Try to extract the beer_preference and add to chosen_beers
            beer_pref = None
            if isinstance(json_response, dict):
                beer_pref = json_response.get("beer_preference")
            elif isinstance(json_response, list) and len(json_response) > 0 and isinstance(json_response[0], dict):
                beer_pref = json_response[0].get("beer_preference")
            if beer_pref and beer_pref not in chosen_beers:
                chosen_beers.append(beer_pref)
            result_list.append(json_response)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for row {i}: {e}")
        
    # Save the results to a JSON file
    with open("../data/persona_results.json", "w", encoding='utf-8') as f:
        json.dump(result_list, f, indent=4, ensure_ascii=False)
    print("✅ Results saved to 'persona_results.json'")

if __name__ == "__main__":
    main()