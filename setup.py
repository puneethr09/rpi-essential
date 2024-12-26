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

    # Install Docker
    print("Installing Docker...")
    run_command("curl -fsSL https://get.docker.com -o get-docker.sh")
    run_command("sh get-docker.sh")
    run_command("sudo usermod -aG docker $USER")

    # Install build-essential for compiling software
    print("Installing build-essential...")
    run_command("sudo apt-get install -y build-essential")

    # Install network tools
    print("Installing network tools...")
    run_command("sudo apt-get install -y net-tools")

    # Install htop for system monitoring
    print("Installing htop...")
    run_command("sudo apt-get install -y htop")

    # Install tmux for terminal multiplexing
    print("Installing tmux...")
    run_command("sudo apt-get install -y tmux")

    # Install zsh and oh-my-zsh for an enhanced shell experience
    print("Installing zsh and oh-my-zsh...")
    run_command("sudo apt-get install -y zsh")
    run_command("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"")

    # Install Glances for system monitoring
    print("Installing Glances...")
    run_command("sudo pip3 install glances")

    # Add any other installations or configurations here

if __name__ == "__main__":
    main()
