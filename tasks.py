import sched, time

def print_text(d = "a"):
    print("A")

def tasks():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(1, 1, print_text, argument=('positional',))
    s.run()