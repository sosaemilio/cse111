import math

def main():
    with open("can_sizes.txt","r") as can_sizes:
       for line in can_sizes:
        column = line.split(",")
        name = column[0]
        radius = float(column[1])
        height = float(column[2])

        storage_efficiency = round(compute_storage_efficiency(radius, height),2)

        print(f"{name} {storage_efficiency}")


def compute_volume(radius, height):
    """Computes de volume of a cylinder"""
    volume = math.pi * (radius ** 2) * height
    return volume

def compute_surface_area(radius, height):
    """Computes the surface area of storage shelter"""
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_storage_efficiency(radius, height):
    """
    Receives the parameters radius and height and computes them using 
    the functions compute_volume and compute_surface_area
    """

    # Stretch challenge #1
    volume = compute_volume(radius, height)
    surface_area = compute_surface_area(radius, height)

    storage_efficiency = volume / surface_area
    return storage_efficiency

main()