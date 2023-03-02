#!/bin/bash
#SBATCH -t 24:00:00
#SBATCH -n 32



# Define the input directory and ORCA command
input_dir="."

# Loop over the ORCA scripts in the input directory and run each script
for filename in ${input_dir}/*.inp; do
    # Run the ORCA script using the ORCA command
    $(which orca) ${filename}
    wait

    # Print a message to the console indicating the filename and completion status
    if [ $? -eq 0 ]; then
        echo "ORCA script ${filename} completed successfully."
    else
        echo "ORCA script ${filename} encountered an error."
    fi
done
