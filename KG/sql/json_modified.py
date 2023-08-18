import json

def read_multiple_json_objects(filename):
    """Read multiple top-level JSON objects from a file."""
    with open(filename, 'r') as file:
        content = file.read()
        objs = [json.loads(obj) for obj in content.split('\n') if obj.strip()]
    return objs

def replace_null_with_empty_string(obj):
    """Recursively replace all null values with empty strings in a JSON object."""
    if isinstance(obj, dict):
        return {k: replace_null_with_empty_string(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_null_with_empty_string(v) for v in obj]
    elif obj is None:  # This checks for the 'null' in JSON, which is None in Python
        return ""
    else:
        return obj

# Read multiple JSON objects from the file
data = read_multiple_json_objects("fundings_metadata.json")

data = [replace_null_with_empty_string(obj) for obj in data]


with open("fundings_metadata.json", "w") as file:
    json.dump(data, file, indent=4)
