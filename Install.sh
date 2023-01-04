#!/bin/zsh

PythonVersion=$(python3 -V 2>&1 | grep -Po '(?<=Python )(.+)')
echo $PythonVersion

if [[ -z "$PythonVersion" ]]
then
    echo "Installing Python3!"
    #sudo yum install -y python3
fi
# Check for Python3
  # If not:
    # Install Python3

# Check for HomeBrew.
  # If not:
    # Install HomeBrew.

# Mandatory Dependency Installs..
#brew install ffmpeg
#python3 pip install -r requirements.txt