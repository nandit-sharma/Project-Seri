# SERI - Screen Element Recognition and Interaction

A Python application that automatically detects and clicks on specific UI elements on your screen.

## Features

- Template matching-based target detection
- Configurable detection confidence threshold
- Automated mouse clicking at detected positions
- Adjustable detection interval and click delays

## Installation

1. Clone or download this repository
2. Install Python 3.7 or higher
3. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Edit `src/config.py` to adjust:

- **CONFIDENCE_THRESHOLD**: Detection confidence level (0.0-1.0)
- **INTERVAL**: Check frequency in seconds
- **CLICK_DELAY**: Delay after clicking in seconds
- **TARGET_IMAGE_PATH**: Path to the target image file

## Usage

1. Place a screenshot of the target UI element in `assets/target.png`
2. Adjust settings in `src/config.py` as needed
3. Run the program:

```bash
python src/main.py
```

## Safety

- The program includes a failsafe: move your mouse to any corner of the screen to stop
- Press Ctrl+C to interrupt the program

## Project Structure

```
seri/
├── assets/           # Target image files
├── src/              # Source code
├── dist/             # PyInstaller distribution (auto-generated)
├── build/            # PyInstaller build files (auto-generated)
├── requirements.txt  # Python dependencies
├── README.md         # This file
└── .gitignore        # Git ignore rules
```

## Creating Standalone Executable

To create a standalone executable using PyInstaller:

```bash
pip install pyinstaller
pyinstaller --onefile --add-data "assets:assets" src/main.py
```

The executable will be created in the `dist/` folder.

## Troubleshooting

- **Target not detected**: Ensure the target image is clear and has good contrast
- **Incorrect clicks**: Adjust the `CONFIDENCE_THRESHOLD` in config.py
- **Performance issues**: Increase `INTERVAL` to reduce CPU usage

## License

This project is provided as-is for personal use.
