# Measurements taken directly from the probes
# The entries of the touples are:
# - reader command
# - timeseries id (as present in the remote database)
# - local timeline file name (optional)
# - local timeline maximum length (optional)

direct_timeseries_entries = [
        #("r1 pH", 11, "", 0),
        #("r1 cond", 12, "", 0),
        #("r1 mg", 13, "", 0),
        #("r2 temperature", 16, "", 0),
        ("r2 mg", 9, "magnesio_torre.json", 10),
        ("r2 cond", 8, "", 0),
        ("r2 pH", 7, "", 0)]

# Measurements which require an external program to measure
# The entries of the touples are:
# - external program name
# - timeseries id (as present in the remote database)
# - list of arguments to call the program with
# - local timeline file name (optional)
# - local timeline maximum length (optional)

processed_timeseries_entries = [(
    "linear-correction", 19, 
    ["--measurement", "magnesio_torre.json", "--calibration mg-calibration-torre.json"], 
    "", 0)]       
#(
            #"h2s-determination", 5,
            #["-t", "temperature.json", "-v", "voltage.json", "-c", "h2s-calibration.json"],
            #"",0)]

subprocess_timeout_seconds = 8
