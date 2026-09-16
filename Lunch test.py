import time
import krpc

conn = krpc.connect(
    name="Launch test",
    address="100.85.76.35",
)
vessel = conn.space_center.active_vessel
print("Okkkkkk lets go")
vessel.control.throttle = 1.0
vessel.control.activate_next_stage()
print("I think its working")

