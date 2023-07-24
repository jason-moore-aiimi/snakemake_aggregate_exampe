from glob import iglob
import json
from pathlib import Path

with open("input.json") as input_file:
    input = json.load(input_file)
COMPONENTS = input["components"]
CAR_CLASSES = input["car_classes"]
SOURCES = input["sources"]
NUMBER_OF_PARTS = input["number_of_parts"]
PART_PATHS = [Path(directory) for directory in iglob("*/*/*")]


def get_result_files():
    result_files = []
    for part_path in [Path(directory) for directory in iglob("*/*/*")]:
        part_id = part_path.name
        result_files += [(part_path / f"results/{source}/{part_id}_{source}.txt").as_posix() for source in SOURCES]
    return result_files
            
RESULT_FILES = get_result_files()
PART_RESULT_FILES = [part_path / "result.txt" for part_path in PART_PATHS]