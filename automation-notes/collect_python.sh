#!/bin/bash

# Output file
output_file="python_scripts.txt"

# Loop through all Python scripts in the current directory
for script in *.py; do
    # Check if there are any Python scripts in the directory
    if [[ -e "$script" ]]; then
        # Append the script name to the output file
        echo "$script:" >> "$output_file"
        echo -e "\n\n" >> "$output_file"
        
        # Append the script contents to the output file
        cat "$script" >> "$output_file"
        
        # Add two new lines after the script
        echo -e "\n\n" >> "$output_file"
    fi
done

echo "Python scripts have been written to $output_file"

