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







