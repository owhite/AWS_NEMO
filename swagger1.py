#!/usr/bin/env python3

import requests

BASE_URL = "https://api.umigs.org/v1.4"   # example — confirm in Swagger

url = f"{BASE_URL}/projects"

response = requests.get(url)

response.raise_for_status()

projects = response.json()

print(projects)
