import os
from pathlib import Path
from typing import List
from uuid import uuid4
from inputs import CAR_CLASSES, COMPONENTS, NUMBER_OF_PARTS

def create_directories(directories: List[Path]) -> None:
    for directory in directories:
        if not directory.exists():
            os.mkdir(directory)

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

if __name__ == '__main__':
    component_directories = create_component_directories(COMPONENTS)
    car_class_directories = create_car_class_directories(CAR_CLASSES, component_directories)
    part_directories = create_part_directories(NUMBER_OF_PARTS, car_class_directories)



