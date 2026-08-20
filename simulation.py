# Universal Gravitational Constant
G = 6.67430e-11

def calculate_gravitational_force(m1, m2, distance):
    """Calculates gravitational force between two point masses."""
    if distance <= 0:
        raise ValueError("Distance must be greater than zero.")
    return G * (m1 * m2) / (distance ** 2)

# Test Case: Earth and Moon interaction
m_earth = 5.972e24  # mass in kg
m_moon = 7.348e22   # mass in kg
r_earth_moon = 384400000  # distance in meters

force_earth_moon = calculate_gravitational_force(m_earth, m_moon, r_earth_moon)
print(f"Gravitational force between Earth and Moon: {force_earth_moons:.4e} N")
# Test case 2
m_sun = 1.989e30    # mass in kg
m_earth = 5.972e24  # mass in kg
r_earth_sun = 1.496e11 # distance in meters
force_earth_sun = calculate_gravitational_force(m_earth, m_sun, r_earth_sun)
print(f"Gravitational force between earth and the sun: {force_earth_sun:.4e} N")

