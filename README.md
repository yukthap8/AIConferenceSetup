# Welcome to the AI Conference Test Repo

This repository is designed to help you test your Python environment setup. It includes a simple Python script that you can run to verify that everything is working correctly.

## Getting Started

Follow these steps to run the test script:

### 1. Open Terminal

This is usually found at the top left of the IDE or can be opened via the IDE's menu (often under View > Terminal or similar).

If you're on Windows, open a terminal as instructed above. After, click the plus symbol on the right and open a Git Bash terminal. You may be prompted to install the Windows Subsystem for Linux (WSL) extension. This is necessary to the demonstration.

### 2. Create a Virtual Environment

Navigate to the directory where you cloned this repository and create a virtual environment. This will help isolate the Python environment for this project from other Python projects on your system.

You can create a virtual environment using the following command in your terminal:
```bash
python3 -m venv venv
```

This will create a new virtual environment in a folder named `venv` in the current directory.

### 3. Activate the Virtual Environment

Before you can start using the virtual environment, you need to activate it. 

For both MacOS and Windows WSL, use the following command:

```bash
source venv/bin/activate
```

### 4. Run the Test Script

Now you're ready to run the test script. You can do this with the following command:

```bash
python test_setup.py
```
If the program is successful, it will print to the terminal. If there is an error, it might be because of the interpreter you have selected. If you encounter serious errors, refer to the [FISD AI Engineers](https://join.slack.com/t/fisdaiengineers/shared_invite/zt-2u9uipuvm-Db1YvBvZ~5CSMLtAEZLvIQ) channel for help.

### 5. Deactivate the Virtual Environment

Once you're done with your work, it's a good practice to deactivate your virtual environment. You can do this with the following command:

```bash
deactivate
```
This will deactivate your virtual environment and return you to your system's default Python environment.