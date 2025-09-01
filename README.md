# Scroller - Grant and Subvention Research Tool

A comprehensive tool for researching grants and subventions from French, European, and Colombian sources.

## Features
- Multi-source grant research (French, European, Colombian)
- Real-time data from official APIs
- Excel export functionality
- URL validation and fixing
- Advanced filtering and analysis

## Installation

### Windows Users
1. Download the project
2. Double-click `Simple_Launcher.bat`
3. Wait for automatic setup and launch

### Mac/Linux Users
1. Download the project
2. Open Terminal and navigate to project folder
3. Run: `chmod +x "Launch_Scroller(mac).sh"`
4. Run: `./Launch_Scroller\(mac\).sh`

## Manual Installation
```bash
pip install streamlit requests pandas openpyxl beautifulsoup4 feedparser
streamlit run app.py
```

## Usage
1. Select search type (Visual Arts, Innovation, etc.)
2. Enter keywords and select regions
3. Click "Search for Subventions"
4. Export results to Excel
5. Use URL validation tools if needed

## Requirements
- Python 3.8+
- Internet connection for API access
- See `requirements.txt` for full dependencies

## Project Structure
```
Scroller/
├── app.py                     # Main Streamlit application
├── api.py                     # Core API integration
├── requirements.txt           # Python dependencies
├── Simple_Launcher.bat       # Windows launcher
├── Launch_Scroller(mac).sh   # Mac/Linux launcher
└── data/                     # Configuration files
```

## Contributing
This is a professional grant research tool. For support or customization, contact the development team.

## License
Proprietary software - All rights reserved.
