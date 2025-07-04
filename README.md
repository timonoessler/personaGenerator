# Synthetic Market Research
Large language models (LLMs) have recently gained attention for their ability to generate human-like text across a wide range of tasks. In parallel, the use of synthetic data has emerged as a promising alternative to traditional data collection methods, particularly in domains where collecting high-quality human data is costly, time-consuming, or constrained by privacy concerns. This Repository offers a minimalistic framework for generating synthetic personas and use them to answer a survey.

## Project Structure
```
|config
|----|example_config.cfg
|data
|----|example_encodings.csv
|----|example_namelist.csv
|----|example_persona_format.json
|----|example_answer_format.json
|----|example_input_question.json
|----|example_output_format.json
|src
|----|helpers
|----|----|tool_box.py
|----|models
|----|----|api_connection.py
|----|----|dataset_generator.py
|----|answerer.py
|----|persona_generator.py
|README.md
|requirements.txt
```
## How to use
### Setup Python environment
Install requirements.txt in e.g. pipenv
```bash
pipenv install -r requirements.txt
pipenv shell
```

### Adjust persona Parameter
Create the files like the examples in ```models/examples_xxx.xxx```
Adjust the parameters in ```models/dataset_generator.py``` to your requirements. The encodings for some values are shown in ```data/example_encodings.csv```. The given parameters are:
* Needed survey base 
```python
n = xxx
```
* Age probabilities 
```python 
age_probs = [0.xxx,0.xxx,0.xxx]
```
* Age ranges 
```python 
age_ranges = {"key":list(range(xx,xx),...}
```
* Gender probabilities 
```python
genders = np.random.choice([1, 2], size=n, p=[0.xxx, 0.xxx]
```
* Origins probabilities 
```python
origin = np.random.choice([1, 2], size=n, p=[0.xxx, 0.xxx]
```
* Relationship status</br>
```python 
for age in ages:
    if 16 <= age <= 20:
        status = np.random.choice([1, 2], p=[0.xxx, 0.xxx])
    elif 21 <= age <= 25:
        status = np.random.choice([1, 2], p=[0.xxx, 0.xxx])
    else:  # 26–30
        status = np.random.choice([1, 2], p=[0.xxx, 0.xxx])
    relationship_status.append(status)
```
* Education depends on which educational degrees you would like to use</br> 
```python 
education_values = [1, 2, 3, 4, 5]
education_probs = np.array([0.xxx, 0.xxx, 0.xxx, 0.xxx, 0.xxx])
education_probs /= education_probs.sum()
education = np.random.choice(education_values, size=n, p=education_probs) 
```
* Employment status e.g. 1 = employed, 2 = unemployed 
```python
employment = np.random.choice([1, 2], size=n, p=[0.xx, 0.xx])
```
* Income depends in the age ranges and how many outliers you want to have
```python
# Non-employed persons (employed=2) have limited income (max 6756€)
random.randint(3000, 6756)
    
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
```
* Leisure activities
```python
leisure_activities = [
    (1, 0.81), (2, 0.63), (3, 0.43), (4, 0.40), (5, 0.39),
    (6, 0.95), (7, 0.731), (8, 0.711), (9, 0.171), (10, 0.173), (11, 0.504)
]
```
* Health consciousness
```python
base = 0.63 if gender == 1 else 0.51
    if edu_level == 5:  # Abitur
        base += 0.1
```

### Start synthesizing Personas
```bash
python3 model/dataset_generator.py
python3 persona_generator.py
python3 answerer.py
```
The programm will create the files
```
|data/erweiterter_persona_datensatz.csv
|data/persona_results.json
|data/persona_beer_answers.json
```
Final file is the last one it will hold your answered survey.
