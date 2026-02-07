# Hand Gesture Game

Control games using hand gestures detected through your webcam. Built with MediaPipe, OpenCV, and PyAutoGUI.

## Features

- Real-time hand tracking via webcam
- Gesture-based keyboard controls:
  - **Jump**: Raise hand to upper third of screen (↑)
  - **Roll/Duck**: Lower hand to bottom third of screen (↓)
  - **Move Left**: Shift hand left (←)
  - **Move Right**: Shift hand right (→)

## Requirements

- Python 3.11 (recommended)
- Windows
- Webcam

## Installation

1. Clone the repository:
```powershell
git clone <repository-url>
cd Hand_gesture_game
```

2. Create virtual environment:
```powershell
python -m venv venv
```

3. Activate virtual environment:
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

4. Install dependencies:
```powershell
python -m pip install -r requirements.txt
```

## Usage

Run the gesture detection:
```powershell
python gesture_hand.py
```

Press `q` to quit.

## Notes

- If MediaPipe fails to install, use Python 3.11 and recreate the virtual environment
- Ensure proper lighting for better hand detection
- Adjust `min_detection_confidence` in code if needed

## Author

Avnav Teotia

## License

MIT
