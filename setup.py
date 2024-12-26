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

    # Configure Git
    print("Configuring Git...")
    run_command("git config --global user.name 'Your Name'")
    run_command("git config --global user.email 'your.email@example.com'")

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
    print("Installing zsh...")
    run_command("sudo apt-get install -y zsh")

    oh_my_zsh_dir = os.path.expanduser("~/.oh-my-zsh")
    if not os.path.exists(oh_my_zsh_dir):
        print("Installing Oh My Zsh...")
        run_command("sh -c \"$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)\"")
    else:
        print("Oh My Zsh is already installed.")
    # Install Glances for system monitoring
    print("Installing Glances...")
    run_command("sudo pip3 install glances")

    # Install SSH server
    print("Installing SSH server...")
    run_command("sudo apt-get install -y openssh-server")

    # Install VNC server
    print("Installing VNC server...")
    run_command("sudo apt-get install -y realvnc-vnc-server")

    # Install UFW for firewall management
    print("Installing UFW...")
    run_command("sudo apt-get install -y ufw")
    run_command("sudo ufw allow ssh")
    run_command("sudo ufw enable")

    # Install FFmpeg for media processing
    print("Installing FFmpeg...")
    run_command("sudo apt-get install -y ffmpeg")

    # Install Nginx web server
    print("Installing Nginx...")
    run_command("sudo apt-get install -y nginx")

    # Add any other installations or configurations here

if __name__ == "__main__":
    main()