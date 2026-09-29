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


apollo_negative_11.control.sas = True
orbit = apollo_negative_11.orbit


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
    print("empty")





def transfer_to_mars():
    print("empty")





def arrive_at_mars():
    print("empty")





def land_on_mars():
    print("empty")

launch(100000, 70000)










