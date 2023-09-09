
# To accept an object mass in kilograms and velocity in meters per second and display its
# momentum. Momentum is calculated as e=mc2 where m is the mass of the object and c is
# its velocity. 

mass = float(input("\nEnter mass of the object (in Kg): "))
velocity = float(input("Enter speed of the object: "))

momentum = mass * (velocity ** 2)

print(f"\nThe momentum of the object of mass {mass} kg travelling at velocity {velocity} m/s is {momentum} kg.m/s.\n")