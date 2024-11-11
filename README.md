# Welcome to AI Conference Test Repo

This repository is designed to help you test your Python environment setup. It includes a simple Python script that you can run to verify that everything is working correctly.

## Getting Started

Follow these steps to run the test script:

### 1. Open Terminal

If you're on a Mac, you can find Terminal in Applications > Utilities > Terminal.

If you're on Windows, we recommend using the Windows Subsystem for Linux (WSL). You can open a WSL terminal by typing `wsl` in the Windows search bar and hitting enter.

### 2. Create a Virtual Environment

Navigate to the directory where you cloned this repository and create a virtual environment. This will help isolate the Python environment for this project from other Python projects on your system.

You can create a virtual environment using the following command:

```bash
python3 -m venv venv
```

This will create a new virtual environment in a folder named `venv` in the current directory.

### 3. Activate the Virtual Environment

Before you can start using the virtual environment, you need to activate it. 

On MacOS and Linux, use the following command:

```bash
source venv/bin/activate
```

On Windows, if you're using WSL, the command is the same. If you're using Command Prompt or PowerShell, use this command instead:

```bash
.\venv\Scripts\activate
```

### 4. Run the Test Script

Now you're ready to run the test script. You can do this with the following command:

```bash
python test_setup.py
```