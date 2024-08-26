import json

with open('clarity_data_dictionary.json', 'r') as file:
    data = json.load(file)

prompt_response_pairs = []

for table in data:
    table_name = table.get('table_name', 'Unknown Table')
    table_description = table.get('table_description', 'No description available.')

    prompt_response_pairs.append({
        "prompt": f"What is the {table_name} table?",
        "response": table_description
    })

    for column in table.get('columns', []):
        column_name = column.get('column_name', 'Unknown Column')
        column_data_type = column.get('column_data_type', 'Unknown Data Type')
        column_description = column.get('column_description', 'No description available.')

        prompt_response_pairs.append({
            "prompt": f"What does the {column_name} column in the {table_name} table represent?",
            "response": column_description
        })

        prompt_response_pairs.append({
            "prompt": f"What is the data type of the {column_name} column in the {table_name} table?",
            "response": f"The data type of the {column_name} column is {column_data_type}."
        })

with open('prompt_response_pairs.json', 'w') as outfile:
    json.dump(prompt_response_pairs, outfile, indent=2)

print("Prompt-response pairs created successfully.")
