import krpc
import time
import math






#========================= connection sequence ======================
conn = krpc.connect(
    name="Launch test",
    address="100.85.76.35",
)
Apollo_Negative_11 = conn.space_center.active_vessel

#================================= Main ===============================================

































#================================= test ===============================================

print("Okkkkkk lets go")
Apollo_Negative_11.control.throttle = 1.0
Apollo_Negative_11.control.activate_next_stage()
time.sleep(3)
print("I think its working")

