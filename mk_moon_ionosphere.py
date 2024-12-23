#
# A basic python script that tracks a specified position on the 
# sky over the time range from START_TIME to END_TIME from
# a specific location on the Earth's surface.

# The output is a text file giving Slant Tec (STEC) and
# ionosphere rotation measure (RM) as a function of time

from __future__ import print_function
import os
import time
import matplotlib
matplotlib.use("agg") # display should not be set

import MS_Iono_functions as iono 
import math

def __run_rinex_predict(LONG, LAT, HEIGHT, OBJECT, DATA_DIR, MAX_DIST, START_TIME, END_TIME, special_body="Moon"):
    os.system('date')
    process_start = time.time()
    startime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    print("getGPSIONO Start at %s" % startime)

    # Moon experiment
    RED_TYPE = 'RI_G03'
    TIME_STEP = 300

    NUM_PROCESSORS = 1
    # Note: we set NUM_PROCESSORS = 1 as we are getting data from Geosciences 
    # Australia, which seems to have difficulty responding to a number of ftp
    # requests being received in parallel 
    # After the GPS data have been collected the system will increase the
    # number of processors for the final ionosphere modelling
    iono. process_ionosphere(time_step=TIME_STEP,
                             object=OBJECT,
                             special_body=special_body,
                             Lat=LAT,
                             Long=LONG,
                             Height=HEIGHT,
                             start_time=START_TIME,
                             end_time=END_TIME,
                             max_dist=MAX_DIST,
                             processing_option=RED_TYPE,
                             do_serial=0,
                             num_processors=NUM_PROCESSORS,
                             gps_data_directory=DATA_DIR)

    os.system('date')
    endtime = time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
    print("getGPSIONO End at %s" % endtime)
    print (' ')
    process_end = time.time()
    duration = (process_end - process_start)/60.0
    print("getGPSIONO Total run time: %7.2f minutes" % duration)

def __checkmake_outputdir():
    testoutdir = os.environ.get("ALBUS_TESTCASE_OUTPUT", "/albus_waterhole")
    if os.path.exists(testoutdir):
        outputhiddendir = os.path.join(testoutdir, 'datadumps')  
        if not os.path.exists(outputhiddendir):
            os.mkdir(outputhiddendir)
    else:
        raise RuntimeError("%s must be a valid directory -- are you running inside Docker, check mount path?" % testoutdir)
    return outputhiddendir

if __name__ == "__main__":
    # MEEREKAT telescope location
    # mean of MeerKAT_Cartesian_coordinate.csv coordinates
    LONG="21:26:35.736"
    LAT="-30:42:44.838"
    HEIGHT=1059.662443

    # UHF
    START_TIME="2021/06/22 17:26:42.7"
    END_TIME="2021/06/22 21:21:20.2"
    OBJECT="MeerKat_Moon_Jun_22_UHF"
    DATA_DIR = os.path.join(__checkmake_outputdir(), 'MeerKat_3C286_test_Moon_Jun_22_UHF')

    
    special_body="Moon"
    MAX_DIST = 350E3
    __run_rinex_predict(LONG, LAT, HEIGHT, OBJECT, DATA_DIR, MAX_DIST, START_TIME, END_TIME, special_body=special_body)
