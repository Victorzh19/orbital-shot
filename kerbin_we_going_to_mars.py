import krpc
import time
import math
from tkinter import *
import threading





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


apollo_negative_11.control.sas = True
orbit = apollo_negative_11.orbit
time_to_apo = orbit.time_to_apoapsis
fuel = apollo_negative_11.resources.amount('LiquidFuel')
body = apollo_negative_11.orbit.body

#First stages
def launch(target_apoapsis, stage_altitude):
    apollo_negative_11.control.throttle = 1.0
    apollo_negative_11.control.activate_next_stage()
    time.sleep(0.5)
    apollo_negative_11.control.activate_next_stage()
    stage = False

    while True:
        current_altitude = apollo_negative_11.flight(body.reference_frame).mean_altitude
        current_apoapsis = orbit.apoapsis_altitude
        
        
        print(f" Altitude: {current_altitude:.2f} m, Apoapsis: {current_apoapsis:.2f} m")

        
        if not stage and current_altitude >= stage_altitude and current_apoapsis >= target_apoapsis:
            
            stage = True
            print("Stage activated!")
            break
        time.sleep(0.5)

    apollo_negative_11.control.throttle = 0


        
        











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








def transfer_to_mars():
    print("empty")





def arrive_at_mars():
    print("empty")





def land_on_mars():
    print("empty")

sc = conn.space_center



#Gui
window = Tk()
window.title("Kerbin to Mars")

def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width // 2) - (width // 2)
    y = (screen_height // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

title_label = Label(window, text="Kerbin to Mars", font=("Arial", 16))
title_label.grid(row=0, column=70, columnspan=2, pady=10)

def fuel_button_clicked():
    fuel = apollo_negative_11.resources.amount('LiquidFuel')
    fuel_label.config(text=f"Liquid Fuel: {fuel:.2f}")
def speed_button_clicked():
    speed = apollo_negative_11.flight(body.reference_frame).speed
    speed_label.config(text=f"Speed: {speed:.2f} m/s")
    
def start_launch():
    activate_launch_function.config(state="disabled")
    thread = threading.Thread(target=launch, args=(100000, 1000))
    thread.start()

fuel_button = Button(window, text="Check Fuel", command=fuel_button_clicked)
fuel_button.grid(row=1, column=10, pady=5)

fuel_label = Label(window, text="Liquid Fuel: 0.00")
fuel_label.grid(row=2, column=10, pady=5)

speed_button = Button(window, text="Check Speed", command=speed_button_clicked)
speed_button.grid(row=1, column=11, pady=5)

speed_label = Label(window, text="Speed: 0.00")
speed_label.grid(row=2, column=11, pady=5)

activate_launch_function = Button(window, text="Launch", command=start_launch)
activate_launch_function.grid(row=3, column=10, pady=5)

center_window(window, 400, 300)
window.after(0, lambda: activate_launch_function.config(state="normal"))



window.mainloop()











