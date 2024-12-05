import subprocess
import os


genus_dir = "/nas/nas_v1/Innovus_trials/users/harshinii/newflowpattern/1.0/blockname/SYNTH/username/run1/scripts"
innovus_dir = "/nas/nas_v1/Innovus_trials/users/harshinii/newflowpattern/1.0/blockname/PD1/username/run1/scripts"

os.chdir(genus_dir)

# Define the command to invoke genus

genus_command = ("source ./synth_make.csh" )

subprocess.run(genus_command, shell=True)

os.chdir(innovus_dir)

# Define the command to invoke innovus
run_fplan = ("source ./fplan_make.csh")

# Run the command
subprocess.run(run_fplan, shell=True)

run_place = ("source ./place_make.csh")
subprocess.run(run_place, shell=True)


run_cts = ("source ./cts_make.csh")
subprocess.run(run_cts, shell=True)


run_route = ("source ./route_make.csh")
subprocess.run(run_route, shell=True)



