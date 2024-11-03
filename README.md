# RealTimeKeyLogger

This project is a simple, real-time keylogger built in Python for educational purposes. The program captures keystrokes and logs them in a text file in real-time, with each keypress recorded on a new line.

> **Disclaimer**: This tool is designed purely for educational purposes to understand logging techniques in Python. Unauthorized use of this tool may violate privacy laws and is strictly prohibited.

## Project Features

- **Real-Time Logging**: Records keystrokes in real-time, appending each keypress to a log file (`key_log.txt`) as it occurs.
- **Simple Console Output**: Displays each keystroke on the console while also logging to the file.
- **Session Management**: Logs the start and end times of each session.

## Requirements

- Python 3.x
- `pynput` library (for capturing keystrokes)

## Setup

1. Clone the repository or download the files.
2. Install the required library by running:
- bash
   pip install pynput


To start logging keystrokes, run the Python script : python Keylogger.py on your bash.


## Usage

Each keystroke will be logged to key_log.txt in real-time, with a new line for each key. Special keys like space, enter, and backspace are represented in brackets, e.g., 
[SPACE].
