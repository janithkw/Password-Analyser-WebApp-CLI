# Password Security Checker

A Python application to check if a password has been compromised using the **HaveIBeenPwned API** with k-anonymity encryption.

## Features

✅ **Privacy-First Design**: Only sends the first 5 characters of your password's SHA-1 hash to the API
✅ **Two Interfaces**: CLI for terminal use and web interface for browser use
✅ **Real-time Checking**: Instant feedback on password security
✅ **Resilient API Calls**: Automatic retry logic for network failures
✅ **Detailed Results**: Shows how many times a password has appeared in breaches

## How It Works

The application uses the k-anonymity security model:
1. Your password is hashed using SHA-1
2. Only the **first 5 characters** of the hash are sent to HaveIBeenPwned API
3. The API returns all hashes matching those 5 characters
4. The application compares the remaining characters locally
5. Your actual password never leaves your computer

## Installation

### Prerequisites
- Python 3.8+
- uv (modern Python package manager - installed automatically)

### Quick Setup (Recommended)

```bash
# Navigate to project directory
cd Password-Analyser

# Run the setup script
chmod +x setup.sh
./setup.sh
```

The setup script will:
✅ Install uv if not present  
✅ Create a virtual environment in `.venv/`  
✅ Install all dependencies  

### Manual Setup

If you prefer to set up manually:

```bash
# Create virtual environment
uv venv .venv

# Activate environment
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate     # On Windows

# Install dependencies
uv pip install -r requirements.txt
```

## Usage

### Activate the Environment

Before running either version, activate the virtual environment:

```bash
source .venv/bin/activate  # On Linux/macOS
.venv\Scripts\activate     # On Windows
```

### CLI Version

Run the command-line interface:

```bash
python password_analyser.py
```

Then enter passwords when prompted:
```
==================================================
Password Security Checker
Powered by HaveIBeenPwned API
==================================================

Enter password to check (or 'quit' to exit): mypassword123
Checking password...
🔴 Password found 3 times in breach database!

Enter password to check (or 'quit' to exit): quit
Goodbye!
```

### Web Version

Start the Flask web server (with environment activated):

```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

**Features:**
- Modern, responsive UI
- Toggle password visibility
- Real-time security feedback
- Shows breach count for compromised passwords

## Project Structure

```
Password-Analyser/
├── .venv/                 # Virtual environment (auto-created)
├── templates/
│   └── index.html         # Web UI
├── password_analyser.py    # CLI application
├── app.py                  # Flask web application
├── pyproject.toml          # Project configuration
├── requirements.txt        # Python dependencies
├── setup.sh               # Setup script (run once)
├── SETUP.md               # Detailed setup guide
├── .gitignore             # Git ignore rules
└── README.md              # This file
```

## API Information

This project uses the **HaveIBeenPwned Pwned Passwords API**:
- **Endpoint**: https://api.pwnedpasswords.com/range/{hash_prefix}
- **Documentation**: https://haveibeenpwned.com/API/v3
- **Data Source**: Aggregated from known security breaches

## Security Notes

🔒 **Your password is never sent to any external service**
- Only the first 5 characters of the SHA-1 hash are sent
- This design prevents even the API from knowing your full password hash
- Uses HTTPS for all communications
- No data is logged or stored

## Error Handling

The application gracefully handles:
- Network timeouts
- API rate limiting (with automatic retry)
- Invalid responses
- Connection errors

## Example Results

| Password | Status | Message |
|----------|--------|---------|
| MyP@ssw0rd! | Safe | ✅ Not found in breach database |
| password123 | Compromised | ⚠️ Found 3,645,804 times |
| 123456 | Compromised | ⚠️ Found 4,929,113 times |

## Environment Management

This project uses **uv** for fast and efficient package management:

```bash
# Activate environment
source .venv/bin/activate

# Install a new package
uv pip install <package-name>

# Update requirements
uv pip freeze > requirements.txt

# Deactivate environment
deactivate
```

**Why uv?**
- ⚡ ~10x faster than pip
- 📦 Parallel package downloads
- 🔒 Better caching and security
- 🌍 Cross-platform compatible

## Future Enhancements

- [ ] Password strength meter
- [ ] Suggest stronger passwords
- [ ] Database of common passwords
- [ ] Docker containerization
- [ ] Batch password checking
- [ ] Password history checking

## License

MIT License - Feel free to use this project for educational purposes.

## Disclaimer

This tool is provided for educational and security auditing purposes. Always use strong, unique passwords and enable two-factor authentication on important accounts. The password checking is only as good as the HaveIBeenPwned database; absence of evidence is not evidence of absence.

---

**Created**: February 2026
**Powered by**: HaveIBeenPwned API
