# Simple Clock Android App

A simple clock Android application built with Python using the `pyandroid-dev` library.

## Features

- Digital clock display showing current time (HH:MM:SS)
- Clean, minimalist UI with dark theme
- Built entirely with Python
- Automatic APK building via GitHub Actions

## Requirements

- Python 3.9+
- pyandroid-dev
- pyjnius
- buildozer (for building APK)

## Installation

### Install dependencies

```bash
pip install -r requirements.txt
```

## Building the APK

### Local Build

To build the APK locally:

```bash
buildozer android debug
```

The APK will be generated in the `bin/` directory.

### GitHub Actions Build

This repository is configured with GitHub Actions to automatically build the APK when you push to the `main` branch or any `release/**` branch.

1. Push your changes to the repository
2. Go to the "Actions" tab in your GitHub repository
3. Wait for the build to complete
4. Download the APK from the "Artifacts" section

## Project Structure

```
clock-android-app/
├── main.py                 # Main application code
├── buildozer.spec         # Buildozer configuration
├── requirements.txt       # Python dependencies
├── .github/
│   └── workflows/
│       └── build-apk.yml # GitHub Actions workflow
└── README.md             # This file
```

## How It Works

The app uses:
- **pyandroid-dev**: Python library for Android app development
- **pyjnius**: Python-Java bridge for accessing Android APIs
- **Buildozer**: Tool for packaging Python apps as Android APK

The clock updates every second and displays the current time in a large, easy-to-read format.

## Development

### Running locally (non-Android)

You can test the basic functionality on your computer:

```bash
python main.py
```

Note: The UI components will only work on Android devices. On desktop, it will print the time to the console.

## GitHub Actions Workflow

The workflow automatically:
1. Sets up the build environment (Python, Java, Android SDK)
2. Installs all dependencies
3. Builds the APK using Buildozer
4. Uploads the APK as an artifact

You can manually trigger the workflow from the Actions tab or it will run automatically on push to main/release branches.

## License

MIT License

## Author

Built with ❤️ using pyandroid-dev
