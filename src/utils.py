import os
import json
import random
import string


def clean_temp_files() -> None:
    """Cleans temporary files"""

    for file in os.listdir('temp'):
        with open(f'temp/{file}', 'w') as f:
            f.write('[]')
            

def generate_id(length: int=6) -> str:
    """Generates an ID and stores it in temp/generated_ids.json for later retreival and use"""

    with open("temp/generated_ids.json", "r") as f:
        generated = json.load(f)

    gen = "".join(random.choices(string.ascii_uppercase, k=length))
    
    while gen in generated:
        gen = ''.join(random.choices(string.ascii_uppercase, k=length))

    generated.append(gen)
    
    with open("temp/generated_ids.json", "w") as f:
        json.dump(generated, f, indent=4)
        
    return gen
