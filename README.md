# Hand Gesture Game

This small project uses MediaPipe and OpenCV to detect hand gestures from your webcam and simulate keyboard events (via PyAutoGUI) for simple game controls.

Requirements
- Python 3.11 recommended
- Windows

Quick start

PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
python gesture_hand.py
```

To create the virtual environment and install dependencies:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

Notes
- If `mediapipe` fails to install on your Python version, install Python 3.11 and recreate the venv.
