import argparse
import json
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Set up argument parser
parser = argparse.ArgumentParser()
parser.add_argument('items', nargs='*', help="Items to add to the list")
args = parser.parse_args()

# Load existing list from JSON file, or initialize new list
try:
    my_list = load_from_json_file("add_item.json")
except FileNotFoundError:
    my_list = []

# Add new items to the list
my_list.extend(args.items)

# Save list to JSON file
save_to_json_file(my_list, "add_item.json")
