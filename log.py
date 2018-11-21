enable_tracing = True
if enable_tracing:
    debug_log = open("debug.log", "w")

def func_z():
    if enable_tracing:
        def main(*args,**kwargs):
            debug_log.write("Вызов %s: %s, %s\n" % (main__name__, args, kwargs))
            r = func_z(*args,**kwargs)
            debug_log.write("%s вернула %s\n" % (main__name__, r))
            return r
        return main
    else:
        return func_z
