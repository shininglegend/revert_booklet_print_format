# Revert Booklet Print Format
This takes a pdf that has been put into a format for printing in a booklet (ie, where the first and last pages are on the same page) and converts it to a normal pdf. It expects the actual page one to be on the right-hand side of the first page, page 2 to be on the left-hand side of the second page, page 3 to be on the right-hand side of the third page, etc.

# Installation Instructions

This guide will help you set up and run this script. If you encounter any issues, please check the [Troubleshooting](#troubleshooting) section below or search for your specific error message online.

## Prerequisites

1. Ensure [Python is installed](https://wiki.python.org/moin/BeginnersGuide/Download) (Python 3.8 or higher recommended) and up to date.

2. [Clone this repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) to a folder on your machine.

## Setup

3. Open a terminal/command prompt and [navigate to the project folder](https://tutorials.codebar.io/command-line/introduction/tutorial.html)

4. Create a virtual environment:
   - On Windows:
     ```bash
     python -m venv venv
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     ```

5. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

6. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Script

7. With the virtual environment activated, run the script:
   ```bash
   python splitpdf.py
   ```

## Troubleshooting

- If you see "python not found", make sure Python is added to your system's PATH
- If pip install fails, try upgrading pip first: `python -m pip install --upgrade pip`
- If you get a "ModuleNotFoundError", make sure your virtual environment is activated and requirements are installed

## Deactivating the Virtual Environment

When you're done, you can deactivate the virtual environment:
```bash
deactivate
```