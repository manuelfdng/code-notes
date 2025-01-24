#!/bin/bash

# Output file
output_file="sql_scripts.txt"

# Loop through all SQL scripts in the current directory
for script in *.sql; do
    # Check if there are any SQL scripts in the directory
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

echo "SQL scripts have been written to $output_file"