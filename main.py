#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:29:09 2024

@author: michal
"""

#Connect to the external database - web of science

import requests

url = 'https://www.google.com/'
search_query = 'Nano ZnO'

# Define the parameters for the search
params = {'q': search_query}

# Send a GET request to the website's search endpoint
response = requests.get(url, params=params)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Process the response, which may include the search results
    print(response.text)
else:
    print(f"Failed to retrieve search results. Status code: {response.status_code}")

# response = requests.get(url)

klm = response.text

# Process the response
print(response.text)