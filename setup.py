
import os
import subprocess

def run_command(command):
    """Run a shell command."""
    result = subprocess.run(command, shell=True, check=True, text=True)
    return result

def main():
    # Update and upgrade the system
    print("Updating and upgrading the system...")
    run_command("sudo apt-get update && sudo apt-get upgrade -y")

    # Install essential packages
    print("Installing essential packages...")
    run_command("sudo apt-get install -y git vim curl")

    # Install Python and pip
    print("Installing Python and pip...")
    run_command("sudo apt-get install -y python3 python3-pip")

    # Install Node.js and npm
    print("Installing Node.js and npm...")
    run_command("curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -")
    run_command("sudo apt-get install -y nodejs")

    # Add any other installations or configurations here

if __name__ == "__main__":
    main()
