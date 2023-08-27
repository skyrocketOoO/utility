#!/bin/bash

# Function to get the command using the most CPU
get_most_cpu_command() {
  # Get the top process by CPU usage and extract the command
  top_process="$(top -b -n 1 | awk 'NR == 8 && $9 > 95 {print $12}')"
  echo "$top_process"
}

# Infinite loop to monitor CPU usage every 5 seconds
while true; do
  # Get the command with the most CPU usage
  most_cpu_command=$(get_most_cpu_command)

  # Check if most_cpu_command is not empty
  if [ -n "$most_cpu_command" ]; then
    # Print the command and current CPU usage percentage
    echo "$(date) - Most CPU Usage: $most_cpu_command" >> ~/most_cpu.out
  fi

  # Sleep for 5 seconds before the next iteration
  sleep 5
done