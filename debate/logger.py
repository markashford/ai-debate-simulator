import json
import os
from datetime import datetime

def save_run(data):
    os.makedirs("runs", exist_ok=True)
    file = f"runs/{datetime.now().isoformat().replace(':','-')}.json"

    with open(file, "w") as f:
        json.dump(data, f, indent=2)

    return file
