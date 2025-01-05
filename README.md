# zipLine
- a file sync tool

# Overview
this is a backbone for self hosted image and videos sync tool, designed to sync images and videos between Android and Linux

# Prerequisites
- docker (required)
- python (required)
- git (optional for developement)
- vscode with dev containers (optional for development)

# Installation
To run production server:
    
    docker build -t zipline-prod target=prod .
    docker run -itd -v .:/app zipline-prod

To run development server:

    docker build -t zipline-dev target=dev .
    docker run -it -v .:/app zipline-dev

To run in dev container:

    VS Code > Command Palette > Dev Containers: Reopen in Container
