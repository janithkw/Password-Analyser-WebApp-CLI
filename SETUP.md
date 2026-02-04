# Setup Guide - UV Environment

This project uses **uv** - a fast, efficient Python package manager and virtual environment tool.

## Prerequisites

- Python 3.8 or higher
- uv (will be installed automatically if not present)

## Quick Setup

### Automatic Setup (Recommended)

```bash
./setup.sh
```

This script will:
- Check if uv is installed (install if needed)
- Create a virtual environment in `.venv/`
- Install all dependencies from `requirements.txt`

### Manual Setup

1. **Create virtual environment:**
   ```bash
   uv venv .venv
   ```

2. **Activate the environment:**
   ```bash
   # On Linux/macOS
   source .venv/bin/activate
   
   # On Windows
   .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   uv pip install -r requirements.txt
   ```

## Running the Application

### CLI Version
```bash
source .venv/bin/activate
python password_analyser.py
```

### Web Version
```bash
source .venv/bin/activate
python app.py
```
Then open `http://localhost:5000` in your browser.

## Project Structure

```
Password-Analyser/
├── .venv/                   # Virtual environment (auto-created)
├── templates/
│   └── index.html          # Web UI
├── password_analyser.py     # CLI application
├── app.py                  # Flask web application
├── pyproject.toml          # Project configuration
├── requirements.txt        # Dependencies
├── setup.sh               # Setup script
├── .gitignore             # Git ignore rules
└── README.md              # Main documentation
```

## What Gets Ignored

The `.gitignore` file automatically excludes:
- Virtual environment: `.venv/`, `venv/`
- Python cache: `__pycache__/`, `*.pyc`, `*.egg-info/`
- IDE files: `.vscode/`, `.idea/`
- UV lock file: `uv.lock`
- Environment files: `.env`, `.env.local`
- OS files: `.DS_Store`, `Thumbs.db`

## Deactivating the Environment

```bash
deactivate
```

## Installing New Dependencies

With the environment activated:
```bash
uv pip install <package-name>
```

Then update `requirements.txt`:
```bash
uv pip freeze > requirements.txt
```

## Troubleshooting

### uv command not found
```bash
pip install uv
```

### Virtual environment creation fails
```bash
rm -rf .venv
uv venv .venv
source .venv/bin/activate
```

### Module not found errors
Make sure the virtual environment is activated:
```bash
source .venv/bin/activate
```

### API connection issues
- Check your internet connection
- The HaveIBeenPwned API may be rate-limited
- The application retries automatically

## Performance Notes

UV is significantly faster than pip:
- ✅ ~10x faster dependency resolution
- ✅ Parallel package downloads
- ✅ Better caching mechanisms
- ✅ Cross-platform compatibility

## More Information

- **uv Documentation**: https://docs.astral.sh/uv/
- **HaveIBeenPwned API**: https://haveibeenpwned.com/API/v3
- **Flask Documentation**: https://flask.palletsprojects.com/

---

**Setup Complete!** 🎉

Your environment is ready. Start checking passwords securely!
