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
import math
G = 6.6743e-11

def calculate_gravitational_force_2d(m1, m2, pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    dx = x2 - x1
    dy = y2 - y1

    r = math.sqrt(dx**2)
    if r <= 0:
        raise ValueError("distance must be greater than zero.")

force = G * (m1 * m2)/(r**2)

fx = force * (dx/r)
fy = force * (dy/y)

# Test 2D Intersection (Earth at origin, Moon along X-axis)
f_x, f_y =
calculate_gravitational_force_d(5.972e24, 7.348e22, (0,0), (384400000,0))
print(f"2D Force components on Moon -> Fx: {f_x:.4e} N, Fy: {f_y:.4E}"N)