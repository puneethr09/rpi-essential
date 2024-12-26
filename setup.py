import os
import subprocess


def run_command(command):
    """Run a shell command."""
    result = subprocess.run(command, shell=True, check=True, text=True)
    return result


def is_command_available(command):
    """Check if a command is available on the system."""
    result = subprocess.run(
        f"command -v {command}",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return result.returncode == 0


def main():
    # Update and upgrade the system
    print("Updating and upgrading the system...")
    run_command("sudo apt-get update && sudo apt-get upgrade -y")

    # Install essential packages
    if not is_command_available("git"):
        print("Installing git...")
        run_command("sudo apt-get install -y git")
    else:
        print("Git is already installed.")

    if not is_command_available("vim"):
        print("Installing vim...")
        run_command("sudo apt-get install -y vim")
    else:
        print("Vim is already installed.")

    if not is_command_available("curl"):
        print("Installing curl...")
        run_command("sudo apt-get install -y curl")
    else:
        print("Curl is already installed.")

    # Install Python and pip
    if not is_command_available("python3"):
        print("Installing Python...")
        run_command("sudo apt-get install -y python3")
    else:
        print("Python is already installed.")

    if not is_command_available("pip3"):
        print("Installing pip...")
        run_command("sudo apt-get install -y python3-pip")
    else:
        print("Pip is already installed.")

    # Configure Git
    print("Configuring Git...")
    run_command("git config --global user.name 'Puneeth'")
    run_command("git config --global user.email 'Puneethr09@gmail.com'")

    # Check if Docker is installed
    if not is_command_available("docker"):
        print("Installing Docker...")
        run_command("curl -fsSL https://get.docker.com -o get-docker.sh")
        run_command("sh get-docker.sh")
        run_command("sudo usermod -aG docker $USER")
    else:
        print("Docker is already installed.")

    # Install build-essential for compiling software
    if not is_command_available("gcc"):
        print("Installing build-essential...")
        run_command("sudo apt-get install -y build-essential")
    else:
        print("Build-essential is already installed.")

    # Install network tools
    if not is_command_available("ifconfig"):
        print("Installing net-tools...")
        run_command("sudo apt-get install -y net-tools")
    else:
        print("Net-tools are already installed.")

    # Install htop for system monitoring
    if not is_command_available("htop"):
        print("Installing htop...")
        run_command("sudo apt-get install -y htop")
    else:
        print("Htop is already installed.")

    # Install tmux for terminal multiplexing
    if not is_command_available("tmux"):
        print("Installing tmux...")
        run_command("sudo apt-get install -y tmux")
    else:
        print("Tmux is already installed.")

    # Install Glances using apt
    if not is_command_available("glances"):
        print("Installing Glances...")
        run_command("sudo apt-get install -y glances")
    else:
        print("Glances is already installed.")

    # Install VNC server
    if not is_command_available("vncserver"):
        print("Installing VNC server...")
        run_command("sudo apt-get install -y realvnc-vnc-server")
    else:
        print("VNC server is already installed.")

    # Install UFW for firewall management
    if not is_command_available("ufw"):
        print("Installing UFW...")
        run_command("sudo apt-get install -y ufw")
        run_command("sudo ufw allow ssh")
        run_command("sudo ufw enable")
    else:
        print("UFW is already installed.")

    # Install FFmpeg for media processing
    if not is_command_available("ffmpeg"):
        print("Installing FFmpeg...")
        run_command("sudo apt-get install -y ffmpeg")
    else:
        print("FFmpeg is already installed.")

    # Install Nginx web server
    if not is_command_available("nginx"):
        print("Installing Nginx...")
        run_command("sudo apt-get install -y nginx")
    else:
        print("Nginx is already installed.")

    # Add any other installations or configurations here


if __name__ == "__main__":
    main()
# Install zsh and oh-my-zsh for an enhanced shell experience
if not is_command_available("zsh"):
    print("Installing zsh...")
    run_command("sudo apt-get install -y zsh")
else:
    print("Zsh is already installed.")

oh_my_zsh_dir = os.path.expanduser("~/.oh-my-zsh")
if not os.path.exists(oh_my_zsh_dir):
    print("Installing Oh My Zsh...")
    run_command(
        'sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"'
    )
else:
    print("Oh My Zsh is already installed.")
# Install zsh-autosuggestions plugin
zsh_autosuggestions_dir = os.path.expanduser(
    "~/.oh-my-zsh/custom/plugins/zsh-autosuggestions"
)
if not os.path.exists(zsh_autosuggestions_dir):
    print("Installing zsh-autosuggestions...")
    run_command(
        "git clone https://github.com/zsh-users/zsh-autosuggestions "
        + zsh_autosuggestions_dir
    )
else:
    print("Updating zsh-autosuggestions...")
    try:
        run_command(f"cd {zsh_autosuggestions_dir} && git pull")
    except subprocess.CalledProcessError:
        print(
            "Could not update zsh-autosuggestions, but continuing with existing installation"
        )  # Update .zshrc to include the plugin

def check_line_in_file(filename, line):
    """Check if a line exists in a file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return line in file.read()
    return False

# Update .zshrc to include the plugin
zshrc_path = os.path.expanduser("~/.zshrc")
content_to_add = [
    "plugins=(git zsh-autosuggestions)",
    "ZSH_AUTOSUGGEST_HIGHLIGHT_STYLE='fg=yellow'",
    "source $ZSH_CUSTOM/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh"
]

print("Configuring .zshrc...")
with open(zshrc_path, "a") as zshrc_file:
    for line in content_to_add:
        if not check_line_in_file(zshrc_path, line):
            zshrc_file.write(f"\n{line}")
            print(f"Added configuration: {line}")
        else:
            print(f"Configuration already exists: {line}")
