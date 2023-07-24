import os
from pathlib import Path
from typing import List
from uuid import uuid4
from inputs import CAR_CLASSES, COMPONENTS, NUMBER_OF_PARTS

def create_directories(directories: List[Path]) -> None:
    for directory in directories:
        if not directory.exists():
            os.mkdir(directory)

def create_result_file(index: int, source_directory: Path) -> Path:
    part_id = source_directory.parent.name
    source = source_directory.name
    result_file = source_directory / f"{part_id}_{source}.txt"
    with open(result_file, "w") as file:
        file.write(str(index))
    return result_file

def create_component_directories(components: List[str]) -> List[Path]:
    component_directories = [Path.cwd() / component_number for component_number in components]
    create_directories(component_directories)
    return component_directories

def create_car_class_directories(car_classes: List[str], component_directories: List[Path]) -> List[Path]:
    car_class_directories: List[Path] = []
    for component_directory in component_directories:
        car_class_directories += [component_directory / car_class for car_class in car_classes]
    create_directories(car_class_directories)
    return car_class_directories

def create_part_directories(number_of_parts: List[str], car_class_directories: List[Path]) -> List[Path]:
    part_directories: List[Path] = []
    for car_class_directory in car_class_directories:
            part_directories += [car_class_directory / str(uuid4()) for _ in range(number_of_parts)]
    create_directories(part_directories)
    return part_directories

def create_source_directories(sources: List[str], part_directories: List[Path]) -> List[Path]:
    source_directories: List[Path] =[]
    for part_directory in part_directories:
        source_directories += [part_directory / source for source in sources]
    create_directories(source_directories)
    return source_directories

def create_result_files(source_directories: List[Path]) -> List[Path]:
    result_files = []
    for index, source_directory in enumerate(source_directories):
        result_file = create_result_file(index, source_directory)
        result_files += [result_file]
    return result_files

def create_all_result_files(components: List[str], car_classes: List[str], parts: List[str], sources: List[str]) -> List[Path]:
    component_directories = create_component_directories(components)
    car_class_directories = create_car_class_directories(car_classes, component_directories)
    part_directories = create_part_directories(parts, car_class_directories)
    source_directories = create_source_directories(sources, part_directories)
    return create_result_files(source_directories)

if __name__ == '__main__':
    component_directories = create_component_directories(COMPONENTS)
    car_class_directories = create_car_class_directories(CAR_CLASSES, component_directories)
    part_directories = create_part_directories(NUMBER_OF_PARTS, car_class_directories)



