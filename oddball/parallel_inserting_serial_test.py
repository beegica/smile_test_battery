from smile.common import *

exp = Experiment()

with Parallel() as p:
    with Loop(10) as lp:
        with p.insert() as pp:
            with Serial():
                Rectangle(center_x=(lp.i%10)*100+Ref(floor,lp.i/10)*100,
                          center_y=(lp.i%10)*100, duration=2)
                Wait(2)
                Rectangle(center_x=(lp.i%10)*100+Ref(floor,lp.i/10)*100,
                          center_y=(lp.i%10)*100, duration=2)
        Debug(b = pp.first)

exp.run()