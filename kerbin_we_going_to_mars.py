import krpc
import time
import math






#========================= connection sequence ======================
conn = krpc.connect(
    name="Launch test",
    address="100.85.76.35",
)
apollo_negative_11 = conn.space_center.active_vessel

#================================= Main ===============================================
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


def angular_pos(x,y,z):
    x = -x
    angle_from_prograde = (math.atan2(x,y)*180/math.pi) % 360

    return angle_from_prograde


apollo_negative_11.control.sas = True
orbit = apollo_negative_11.orbit
time_to_apo = orbit.time_to_apoapsis
fuel = apollo_negative_11.resources.amount('LiquidFuel')



def launch(target_apoapsis, stage_altitude):
    apollo_negative_11.control.throttle = 1.0
    apollo_negative_11.control.activate_next_stage()

    stage = False

    while True:
        current_altitude = apollo_negative_11.flight().mean_altitude
        current_apoapsis = orbit.apoapsis_altitude

        print(f" Altitude: {current_altitude:.2f} m, Apoapsis: {current_apoapsis:.2f} m")

        if not stage and current_altitude >= stage_altitude and current_apoapsis >= target_apoapsis:
            apollo_negative_11.control.activate_next_stage()
            stage = True
            print("Stage activated!")
            break
        time.sleep(0.5)


        
        











def orbit_kerbin():
    print("orbiting sequence started")

    target_periapsis = float(input("Target periapsis: "))
    auto_pilot = apollo_negative_11.auto_pilot
    current_periapsis = apollo_negative_11.orbit.periapsis_altitude


    auto_pilot.engaged = True
    auto_pilot.target_pitch = 0
    auto_pilot.target_heading = target_heading(90)
    print("Adjusting pitch and heading")

    auto_pilot.wait()

    print("orbit maneuver node in")
    while orbit.time_to_apoapsis >= 15:
        time_to_apo = orbit.time_to_apoapsis

        print(f"T-{time_to_apo - 15:.0f}")
        time.sleep(1)

    print("Starting burn")



    apollo_negative_11.control.throttle = throttle_controller(target_periapsis, current_periapsis)

    while True:
        current_periapsis = apollo_negative_11.orbit.periapsis_altitude

        print("Target periapsis: ", target_periapsis)

        print(f" Periapsis: {current_periapsis:.2f} m")

        if fuel == 0:
            apollo_negative_11.control.activate_next_stage()
            time.sleep(1)
            apollo_negative_11.control.activate_next_stage()


        if current_periapsis >= target_periapsis:
            break

        time.sleep(0.5)

    print("periapsis reached. turning engines off")

    apollo_negative_11.control.throttle = 0

    print("orbiting sequence finished")





def transfer_to_mars():
    print("Mars transfer sequence started")
    print("verifying orbit integrity")

    current_apoapsis = orbit.apoapsis_altitude
    current_periapsis = orbit.periapsis_altitude

    orbit_eccentricity = orbit.eccentricity
    orbit_inclination = orbit.inclination

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



    if orbit_eccentricity > 0.1 : #work on this
        print("eccentricity not valid ")

        target_periapsis = float(input("Target periapsis: "))

        while orbit.time_to_apoapsis >= 5:
            time_to_apo = orbit.time_to_apoapsis

            print(f"T-{time_to_apo - 15:.0f}")
            time.sleep(1)

        print("Starting burn")

        apollo_negative_11.control.throttle = throttle_controller(target_periapsis, current_periapsis)

        while True:
            current_periapsis = apollo_negative_11.orbit.periapsis_altitude

            print("Target periapsis: ", target_periapsis)

            print(f" Periapsis: {current_periapsis:.2f} m")

            if fuel == 0:
                apollo_negative_11.control.activate_next_stage()
                time.sleep(1)
                apollo_negative_11.control.activate_next_stage()

            if current_periapsis >= target_periapsis:
                break

            time.sleep(0.5)

        print("periapsis reached. turning engines off")

        apollo_negative_11.control.throttle = 0

    current_angle = angular_pos(*apollo_negative_11.position(kerbin_prograde))
    target_angle = float(input("Target angle: "))

    wait_until(target_angle - current_angle == 5)


def arrive_at_mars():
    print("empty")





def land_on_mars():
    print("empty")

launch(100000, 70000)
orbit_kerbin()











