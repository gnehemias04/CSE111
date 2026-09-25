"""
W03 Project: Water Pressure
Author: Gabriel Rengifo
Course CSS111

I add a new function that converts the kpa into psi, the function is called water_pressure_kpa_into_psi

"""

PVC_SCHED80_INNER_DIAMETER = 0.28687       # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013        # (unitless)
SUPPLY_VELOCITY = 1.65                     # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692       # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018         # (unitless)
HOUSEHOLD_VELOCITY = 1.75                  # (meters / second)
WATER_DENSITY = 998.2000000                # density of water (998.2 kilogram / meter^3)
EARTH_ACCELERATION_OF_GRAVITY = 9.8066500  # acceleration from Earths gravity 9.80665 (meter / second2)
WATER_DYNAMIC_VISCOSITY = 0.0010016        # is the dynamic viscosity of water (0.0010016 Pascal seconds)
PSI = 0.145038                             # 1 kpa is equal to 0.105039 psi

def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    pressure_psi = water_pressure_kpa_into_psi(pressure)

    print(f"Pressure at house: {pressure:.1f} kilopascals or {pressure_psi:.1f} psi")



#1
def water_column_height(tower_height, tank_height):

    """ 
    h = t + 3w / 4

    h is height of the water column
    t is the height of the tower (tower_height)
    w is the height of the walls of the tank that is on top of the tower (tank_height)

    """
    return tower_height + ((3*tank_height) / 4)


#2
def pressure_gain_from_water_height(height):
    """
    P = ρgh / 1000
    P is the pressure in kilopascals
    ρ is the density of water 998.2 (kilogram / meter3)
    g is the acceleration from Earths gravity 9.80665 (meter / second2)
    h is the height of the water column inmeters (height)

    """
    #TODO: Need to implement
    return (WATER_DENSITY * EARTH_ACCELERATION_OF_GRAVITY * height) / 1000


#3
def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    numerator = -friction_factor * pipe_length * WATER_DENSITY * fluid_velocity ** 2
    denominator = 2000 * pipe_diameter
    return numerator / denominator


#4
def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    return -.04 * WATER_DENSITY * fluid_velocity ** 2 * quantity_fittings / 2000


#5
def reynolds_number(hydraulic_diameter, fluid_velocity):
      """
      R = ρdv/μ

      R is the Reynolds number
      ρ is the density of water (998.2 kilogram / meter3)
      d is the hydraulic diameter of a pipe in meters. For a round pipe, the hydraulic diameter is the same as the pipe’s inner diameter. (hydraulic_diameter)
      v is the velocity of the water flowing through the pipe in meters / second (fluid_velocity)
      μ is the dynamic viscosity of water (0.0010016 Pascal seconds)

      """
      return (WATER_DENSITY * hydraulic_diameter * fluid_velocity) / WATER_DYNAMIC_VISCOSITY


#6
def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    k=(0.1 + 50 / reynolds_number) * ((larger_diameter / smaller_diameter) ** 4 - 1)
    return (-k * WATER_DENSITY * fluid_velocity ** 2) / 2000

#7
def water_pressure_kpa_into_psi(pressure):

    return pressure * PSI



if __name__ == "__main__":
    main()