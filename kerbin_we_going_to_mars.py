import krpc
import time
import math
from tkinter import *
import threading





#========================= connection sequence ======================
conn = krpc.connect(
    name="Orbital-shot",
    address="100.85.76.35",
    rpc_port= 50000,
    stream_port= 50001
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
body = apollo_negative_11.orbit.body

#First stages
def launch(target_apoapsis):
    apollo_negative_11.control.activate_next_stage()
    print("Yahoo")
    time.sleep(0.5)
    apollo_negative_11.control.throttle = 0.7
    
    apollo_negative_11.control.activate_next_stage()
    print("Fuck")
    
    
    auto_pilot = apollo_negative_11.auto_pilot
    auto_pilot.engaged = True
    auto_pilot.target_pitch = 90
    auto_pilot.target_heading = target_heading(0)
    
    stop_ts = False
    stop_ts1500 = False
    stop_ts13000 = False
    stop_ts15000 = False
    stop_ts17000 = False
    stop_ts20000 = False
    stop_ts20500 = False
    stop_ts21000 = False
    stop_ts21500 = False
    stop_ts22000 = False
    stop_ts22500 = False
    stop_ts23000 = False
    stop_ts23500 = False
    stop_ts24000 = False
    stop_ts24500 = False
    stop_ts25000 = False
    stop_ts25500 = False
    stop_ts26000 = False

    kickbacks = [p for p in apollo_negative_11.parts.all
             if "Kickback" in p.title and p.decouple_stage == 13]
    first_stage_tanks = [p for p in apollo_negative_11.parts.all if "Kerbodyne S3-14400" in p.title and p.decouple_stage == 12]
    
    dropped_kickbacks = False
    dropped_tank = False
    


    
    print("current stage:", apollo_negative_11.control.current_stage)
    
    #solid = apollo_negative_11.stage_at(15).resources(False).amount("SolidFuel")
    while True:
        altitude = apollo_negative_11.flight().mean_altitude
        speed = apollo_negative_11.flight(body.reference_frame).speed
        fuel = apollo_negative_11.resources.amount('LiquidFuel')
        apoapsis = orbit.apoapsis_altitude

        
        
        #print(f"solid fuel is: {solid}")
        #for i, t in enumerate(tank):
            #print(i, "decouple stage:", t.decouple_stage, "fuel:", t.resources.amount("LiquidFuel"))
        
        print(f"Altitude: {altitude:.2f} m")
        print(f"Speed: {speed:.2f} m/s")
        print(f"Liquid Fuel: {fuel:.2f}")
        print(f"Apoapsis {apoapsis:.2f}m")

       

           # shows exactly which resources this part holds

# inside the loop:
        

        if altitude >= 1000 and not stop_ts and speed == 100:
            auto_pilot.target_pitch = 90
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait
            print("it work yupii")
            
            stop_ts = True
        

        if altitude  >= 8000 and not stop_ts1500:
            auto_pilot.target_pitch = 80
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
            
            stop_ts1500 = True

        if altitude >= 13000 and not stop_ts13000:
            auto_pilot.target_pitch = 77
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                        
            stop_ts13000 = True

        if altitude >= 15000 and not stop_ts15000:
            auto_pilot.target_pitch = 75
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts15000 = True
        if altitude >= 17000 and not stop_ts17000:
            auto_pilot.target_pitch = 70
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                    
            stop_ts17000 = True

        if altitude >= 20000 and not stop_ts20000:
            auto_pilot.target_pitch = 60
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts20000 = True

        if altitude >= 20500 and not stop_ts20500:
            auto_pilot.target_pitch = 55
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts20500 = True

        if altitude >= 21000 and not stop_ts21000:
            auto_pilot.target_pitch = 50
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts21000 = True

        if altitude >= 21500 and not stop_ts21500:
            auto_pilot.target_pitch = 45
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts21500 = True

        if altitude >= 22000 and not stop_ts22000:
            auto_pilot.target_pitch = 40
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts22000 = True

        if altitude >= 22500 and not stop_ts22500:
            auto_pilot.target_pitch = 35
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts22500 = True

        if altitude >= 23000 and not stop_ts23000:
            auto_pilot.target_pitch = 30
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts23000 = True

        if altitude >= 23500 and not stop_ts23500:
            auto_pilot.target_pitch = 25
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts23500 = True

        if altitude >= 24000 and not stop_ts24000:
            auto_pilot.target_pitch = 20
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts24000 = True

        if altitude >= 24500 and not stop_ts24500:
            auto_pilot.target_pitch = 15
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts24500 = True

        if altitude >= 25000 and not stop_ts25000:
            auto_pilot.target_pitch = 10
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts25000 = True

        if altitude >= 25500 and not stop_ts25500:
            auto_pilot.target_pitch = 5
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts25500 = True

        if altitude >= 26000 and not stop_ts26000:
            auto_pilot.target_pitch = 0
            auto_pilot.target_heading = target_heading(90)
            auto_pilot.wait()
            print("yupieee2")
                                
            stop_ts26000 = True


        if not dropped_kickbacks:
            kickbacks_fuel = sum(p.resources.amount("SolidFuel") for p in kickbacks)
            if kickbacks_fuel < 0.5:
                apollo_negative_11.control.activate_next_stage()
                print("Quiero sexo")
                dropped_kickbacks = True

        elif not dropped_tank:
            tank_fuel = sum(t.resources.amount("LiquidFuel") for t in first_stage_tanks)
            if tank_fuel < 0.5:
                apollo_negative_11.control.activate_next_stage()
                time.sleep(0.5)
                apollo_negative_11.control.throttle = 1.0
                apollo_negative_11.control.activate_next_stage()
                dropped_tank = True
        #elif not dropped_second_tank:
            #second_tank_fuel = sum(t.resources.amount("LiquidFuel") for t in second_stage_tank)
            #if second_tank_fuel < 0.5:
                #apollo_negative_11.control.activate_next_stage()
                #dropped_second_tank = True

        

        if  apoapsis >= target_apoapsis:
            apollo_negative_11.control.throttle = 0.0
            print('One small step for kerbin one big step for humanity')
            break
        






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

sc = conn.space_center



#================================================= Gui =================================================================================
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
    thread = threading.Thread(target=launch, args=(100000,))
    thread.start()

def reset_launch():
    conn.space_center.revert_to_launch()

def camera_set_up():
    camera = conn.space_center.camera

    camera.mode = conn.space_center.CameraMode.free
    camera.pitch = 20
    camera.heading = 45
    camera.distance = 120 

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

reset_launch_button = Button(window, text="Reset Launch", command=reset_launch)
reset_launch_button.grid(row=3, column=11, pady=5)

camera_button = Button(window, text=" My good looking side", command=camera_set_up)
camera_button.grid(row=1, column= 13, pady= 5 )

center_window(window, 400, 300)
window.after(0, lambda: activate_launch_function.config(state="normal"))


print(apollo_negative_11.name)

stage_13 = apollo_negative_11.decouple_stage_at(13)
kickbacks = [p for p in stage_13.parts if "Kickback" in p.title]
print(len(kickbacks))

window.mainloop()











