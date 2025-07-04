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
Install requirements.txt in e.g. pipenv
```bash
pipenv install -r requirements.txt
pipenv shell
```

Adjust the parameters in ```models/dataset_generator.py``` to your requirements. The given parameters are:
* Needed survey base ```n = xxx```
* Age probabilities ```age_probs = [xxx,xxx,xxx]```
* Age ranges ``` age_ranges = {"key":list(range(xx,xx),...}```
*
