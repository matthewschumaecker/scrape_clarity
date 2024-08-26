import json

def count_prompt_response_pairs(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        
        if isinstance(data, list):
            pair_count = len(data)
            print(f"Number of prompt-response pairs: {pair_count}")
        else:
            print("Error: The JSON file does not contain a list of pairs.")
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"Error: The file '{file_path}' is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    file_path = "prompt_response_pairs.json"
    count_prompt_response_pairs(file_path)
