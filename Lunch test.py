import krpc
import time
import math






#========================= connection sequence ======================
conn = krpc.connect(
    name="Launch test",
    address="100.85.76.35",
)
apollo_negative_11 = conn.space_center.active_vessel
#================================= test ===============================================
#Target heading prevents over correction and wiggle
def target_heading(desired_heading):
    heading_error = abs(desired_heading - apollo_negative_11.flight().heading)

    if heading_error > 20:
        tolerance = 5
    elif heading_error > 5:
        tolerance = 1
    else:
        tolerance = .5
    return desired_heading

#throttle_controller helps prevents overshoot of a specific target
def throttle_controller(target, actual):
    while True:
        remaining = target - actual
        throttle = apollo_negative_11.control.throttle

        if remaining <= 100:
            throttle = 0
            break
        elif remaining < 500:
            throttle = .05
        elif remaining <= 2000:
            throttle = .2
        elif remaining <= 5000:
            throttle = .5
        else:
            throttle = 1
        return throttle

def wait_until(condition):
    while not condition():
        pass


apollo_negative_11.control.sas = True
orbit = apollo_negative_11.orbit
time_to_apo = orbit.time_to_apoapsis
fuel = apollo_negative_11.resources.amount('LiquidFuel')
sc = conn.space_center


duna = sc.bodies["Duna"]
duna_orbit = duna.orbit

kerbin = sc.bodies["Kerbin"]
kerbin_orbit = kerbin.orbit

sun = sc.bodies["Sun"]

sun_non_rot_reference = sun.non_rotating_reference_frame
kerbin_non_rot_reference = kerbin.non_rotating_reference_frame
duna_non_rot_reference = duna.non_rotating_reference_frame
kerbin_prograde = kerbin.orbital_reference_frame

def angular_pos(x,y,z):
    x = -x
    angle_from_prograde = (math.atan2(x,y)*180/math.pi) % 360

    return angle_from_prograde



def target_heading(desired_heading):
    heading_error = abs(desired_heading - apollo_negative_11.flight().heading)

    if heading_error > 20:
        tolerance = 5
    elif heading_error > 5:
        tolerance = 1
    else:
        tolerance = .5
    return desired_heading



print("Okkkkkk lets go")

print (kerbin.position(sun_non_rot_reference))

print (kerbin.velocity(sun_non_rot_reference))

print(apollo_negative_11.position(kerbin_prograde))

angle = angular_pos(*apollo_negative_11.position(kerbin_prograde))

planet_angle = angular_pos(*duna.position(sun_non_rot_reference))

print(angle)

print(planet_angle)




