from flask import Flask, render_template, request, jsonify
import requests
import hashlib
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

app = Flask(__name__)


def check_password(password):
    """
    Check if password has been compromised using HaveIBeenPwned API.
    Uses k-anonymity: sends only first 5 chars of hash to API.
    
    Args:
        password (str): Password to check
        
    Returns:
        dict: {
            'is_pwned': bool,
            'count': int (number of times found, 0 if safe),
            'message': str
        }
    """
    try:
        # Hash the password using SHA-1
        hashed = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        prefix = hashed[:5]
        suffix = hashed[5:]
        
        # Set up resilient requests with retry strategy
        session = requests.Session()
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"],
            backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        
        # Query Pwned Passwords API with only the prefix
        url = f"https://api.pwnedpasswords.com/range/{prefix}"
        headers = {'User-Agent': 'PasswordAnalyzer'}
        
        response = session.get(url, headers=headers, timeout=5)
        response.raise_for_status()
        
        # Check if the suffix appears in the response
        hashes = response.text.splitlines()
        for hash_line in hashes:
            hash_suffix, count = hash_line.split(':')
            if hash_suffix == suffix:
                return {
                    'is_pwned': True,
                    'count': int(count),
                    'message': f'⚠️ Password found {count} times in breach database!'
                }
        
        return {
            'is_pwned': False,
            'count': 0,
            'message': '✅ Password is safe - not found in breach database.'
        }
        
    except requests.exceptions.RequestException as e:
        return {
            'is_pwned': None,
            'count': 0,
            'message': f'❌ Error checking password: {str(e)}'
        }


@app.route('/')
def index():
    """Render the main page."""
    return render_template('index.html')


@app.route('/api/check', methods=['POST'])
def check():
    """API endpoint to check password."""
    data = request.get_json()
    password = data.get('password', '').strip()
    
    if not password:
        return jsonify({'error': 'Password is required'}), 400
    
    result = check_password(password)
    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
