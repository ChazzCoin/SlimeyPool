#!/bin/bash

# Check if Homebrew is installed
if ! command -v brew > /dev/null; then
    echo "Homebrew not found, installing..."

    # Check if system is running on M1
    if uname -a | grep -q "arm64"; then
        echo "Detected M1 architecture, installing Homebrew for M1..."
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/main/install.sh)"
    else
        echo "Detected Intel architecture, installing Homebrew for Intel..."
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi
else
    echo "Homebrew already installed."
fi

# Check if Python3 is installed
if ! command -v python3 > /dev/null; then
    echo "Python3 not found, installing..."
    brew install python3
else
    echo "Python3 already installed."
fi

# Update PATH environment variable
echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile


# Mandatory Dependency Installs..
brew install ffmpeg
ffmpeg -version
python3 pip install -r requirements.txt