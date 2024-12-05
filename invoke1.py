import os

genus_dir = "/nas/nas_v1/Innovus_trials/users/sneha/newflowpattern/1.0/blockname/SYNTH/username/run1/scripts"
innovus_dir = "/nas/nas_v1/Innovus_trials/users/sneha/newflowpattern/1.0/blockname/PD1/username/run1/scripts"

# Function to ask for permission and execute the script
def run_script(path, script):
    if input(f"Do you want to run {script}? (yes/no): ").lower() == "yes":
        os.chdir(path)
        os.system(f"source ./{script}")
        print(f"{script} executed successfully.")

# Run scripts
run_script(genus_dir, "synth_make.csh")
run_script(innovus_dir, "fplan_make.csh")
run_script(innovus_dir, "place_make.csh")
run_script(innovus_dir, "cts_make.csh")
run_script(innovus_dir, "route.csh")
