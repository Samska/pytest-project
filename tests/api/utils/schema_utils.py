import json
import os
import glob
from jsonschema import validate, ValidationError

def load_schema(schema_file):
    current_dir = os.path.dirname(__file__)
    root_dir = os.path.abspath(os.path.join(current_dir, '..', '..', '..'))
    schema_path_pattern = os.path.join(root_dir, 'fixtures', 'schemas', '**', schema_file)

    schema_files = glob.glob(schema_path_pattern, recursive=True)
    
    if not schema_files:
        raise FileNotFoundError(f"Schema file {schema_file} not found in any subdirectory of 'fixtures/schemas'")
    
    with open(schema_files[0], 'r') as file:
        schema = json.load(file)
    
    return schema

def validate_json(response_json, schema_file):
    schema = load_schema(schema_file)
    try:
        validate(instance=response_json, schema=schema)
        return True, None
    except ValidationError as e:
        return False, e.message