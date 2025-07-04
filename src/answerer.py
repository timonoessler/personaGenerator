import json
import os
from src.models.api_connection import api_call_json

# Path constants
PERSONA_PATH = os.path.join(os.path.dirname(__file__), '../data/persona_results.json')
QUESTIONS_PATH = os.path.join(os.path.dirname(__file__), '../data/input_questions.JSON')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '../data/persona_beer_answers_regional.json')
ANSWER_FORMAT_PATH = os.path.join(os.path.dirname(__file__), '../data/answer_format.json')

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_results_to_json(data, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def get_answers_from_chatgpt(all_personas, all_questions, answer_format):
    """
    Instead of sending just one persona and the questions, send the entire persona list and full question set in the prompt,
    mimicking the web interface behavior for better JSON output. Extract all JSON code blocks and parse them.
    """
    persona_json = json.dumps(all_personas, ensure_ascii=False, indent=2)
    questions_json = json.dumps(all_questions, ensure_ascii=False, indent=2)
    prompt = (
        f"Beantworte nacheinander als jeweils eine Persona aus der Liste (persona_result.json) die Fragen "
        f"(input_questions.json)."
        f"Nutze die 'options', die zu den Fragen gehören, um die Fragen zu beantworten. Daraus ergeben sich numerische"
        f"Werte als Antworten. Achte darauf, dass manche Fragen mehrere Antwortmöglichkeiten haben, "
        f"die du dann in der Antwort berücksichtigen musst. "
        f"Gib die Antworten als ein JSON-Objekt mit dem Schlüssel 'answers' aus, wobei 'answers' "
        f"eine Liste von Antwort-Objekten (jeweils eines pro Persona) ist."
        f"Nutze als Antwortformat answer_format.json, um die Antworten zu strukturieren.\n\n"
        f"Wähle anhand der beer_preference bei Frage 3 eine passende existierende Biermarke. "
        f"Bevorzugt aus der Region Baden Württemberg. Achte zusätzlich auf stringente Antworten innerhalb einer "
        f"persona.\n\n"
        f"persona_result.json:\n{persona_json}\n\ninput_questions.json:\n{questions_json}\n\n"
        f"answer_format.json:\n{answer_format}\n\n"
    )
    messages = [
        {"role": "system", "content": "Du bist ein Marktforschungs-Experte für Bierkonsum."},
        {"role": "user", "content": prompt}
    ]
    response = api_call_json(messages)
    try:
        parsed = json.loads(response)
        # Expecting a dict with key 'answers' containing a list
        if isinstance(parsed, dict) and "answers" in parsed and isinstance(parsed["answers"], list):
            return parsed["answers"]
        else:
            return [{"error": "No 'answers' key found in response", "raw": response}]
    except Exception as e:
        return [{"error": f"Could not parse JSON: {str(e)}", "raw": response}]

import time

def main():
    personas_data = load_json_data(PERSONA_PATH)
    questions_data = load_json_data(QUESTIONS_PATH)
    answer_format = load_json_data(ANSWER_FORMAT_PATH)

    batch_size = 10
    wait_seconds = 60
    all_answers = []
    total = len(personas_data)
    persona_items = list(personas_data.items()) if isinstance(personas_data, dict) else list(enumerate(personas_data))

    for i in range(0, total, batch_size):
        batch = dict(persona_items[i:i+batch_size])
        answers = get_answers_from_chatgpt(batch, questions_data, answer_format)
        all_answers.extend(answers)
        save_results_to_json(all_answers, OUTPUT_PATH)
        print(f"Processed batch {i//batch_size+1} ({min(i+batch_size, total)}/{total}). Waiting {wait_seconds} seconds...")
        if i + batch_size < total:
            time.sleep(wait_seconds)
    print("All batches processed.")

if __name__ == "__main__":
    main()
