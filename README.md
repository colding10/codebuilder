# CodeBuilder - Science Olympiad Cipher Test Generator

A comprehensive test generator for Science Olympiad CodeBusters events, supporting all ciphers from the 2025-2026 season rules.

Originally forked from <https://github.com/AC01010/codebuilder/tree/main>

## 🎉 What's New in 2025-2026 Season

### New Ciphers Added
- **Atbash Cipher** - Simple reverse alphabet substitution (A→Z, B→Y, etc.)
- **Running-Key Cipher** - Polyalphabetic cipher using continuous text as the key
- **Checkerboard Cipher** - Polybius square fractionating cipher (NEW for 2025-2026!)

### Modern Web Interface
- Beautiful, responsive web UI for easy test generation
- Real-time test generation with progress feedback
- Support for all 17 cipher types
- Multiple preset configurations

## 📋 Supported Ciphers

CodeBuilder now supports **17 different cipher types**:

1. **Aristocrat** - Monoalphabetic substitution with spaces
2. **Patristocrat** - Monoalphabetic substitution without spaces
3. **Affine Cipher** - Linear mathematical substitution (ax + b mod 26)
4. **Atbash** ⭐ NEW - Reverse alphabet substitution
5. **Caesar Cipher** - Fixed shift substitution
6. **Vigenère Cipher** - Polyalphabetic keyword cipher
7. **Hill Cipher (2×2)** - Matrix-based encryption
8. **Hill Cipher (3×3)** - Advanced matrix encryption
9. **Xenocrypt** - Spanish language aristocrat cipher
10. **Baconian Cipher** - Binary A/B encoding (multiple modes)
11. **RSA** - Public key cryptography
12. **Morbit Cipher** - Morse code with digit substitution
13. **Pollux Cipher** - Morse code with random digit mappings
14. **Porta Cipher** - Polyalphabetic tableau cipher
15. **Running-Key** ⭐ NEW - Continuous text as encryption key
16. **Rail Fence** - Transposition cipher with configurable rails
17. **Checkerboard** ⭐ NEW - Polybius square cipher

## 🚀 Getting Started

### Installation

1. Clone the repository or download the files
2. Install dependencies:
```bash
pip install -r requirements.txt
```

### Usage Options

#### Option 1: Web Interface (Recommended)

1. Start the web server:
```bash
python web_server.py
```

2. Open your browser and navigate to:
```
http://localhost:5000
```

3. Use the intuitive web interface to:
   - Enter a test name
   - Select a preset (All Types, National Level, Regional Level, etc.)
   - Generate your test with one click!

#### Option 2: Command Line Interface

Run the CLI tool:
```bash
python cli.py
```

Follow the prompts to:
1. Enter a test name
2. Select a preset:
   - `1` - All Types Exam (all 17 cipher types)
   - `2` - National Level Test (competition-weighted)
   - `3` - Regional Level Test (beginner-friendly)
   - `4` - Aristocrat Spam (custom count)
   - `5` - Patristocrat Spam (custom count)

## 📊 Test Presets

### All Types Exam
Includes at least one problem of every cipher type. Perfect for comprehensive practice.

### National Level Test
- Weighted toward harder ciphers
- Includes 10 Patristocrats
- Advanced cipher variations (Hill 3×3, Pollux, etc.)
- ~32 total questions

### Regional Level Test
- Beginner-friendly selection
- Focus on encode/decode operations
- Includes foundational ciphers
- ~21 total questions

### Aristocrat/Patristocrat Spam
- Custom number of questions
- Perfect for focused practice
- Great for beginners

## 🗂️ Output Format

Generated tests are saved in the `CodeTests/` directory as JSON files with the following structure:

```json
{
  "TEST.0": {
    "count": 30,
    "title": "Test Name",
    "questions": [1, 2, 3, ...],
    ...
  },
  "CIPHER.1": {
    "cipherType": "aristocrat",
    "cipherString": "Quote to encode/decode",
    "operation": "decode",
    "points": 250,
    "question": "<p>Solve this aristocrat.</p>",
    ...
  },
  ...
}
```

## 📁 Project Structure

```
codebuilder/
├── generator.py          # Core cipher generation functions
├── cli.py               # Command-line interface
├── web_server.py        # Flask web server (NEW)
├── web_ui.html          # Modern web interface (NEW)
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── CodeTests/          # Generated test output directory
├── quotes.txt          # Quote database (5.1MB)
├── spanish.json        # Spanish quotes for Xenocrypt
├── words.txt           # Word list for keys
├── 2x2hillwords        # Pre-computed 2×2 Hill keys
└── 3x3hillwords        # Pre-computed 3×3 Hill keys
```

## 🔧 Technical Details

### Dependencies
- `sympy==1.8` - For RSA prime generation and modular arithmetic
- `mpmath==1.3.0` - Mathematical computations
- `flask==3.0.0` - Web server framework

### Quote Database
- 40,000+ quotes for varied test content
- Automatic length filtering for each cipher type
- Spanish quotes for Xenocrypt problems

## 🎓 For Coaches and Students

### Best Practices

1. **Start with Regional Level** - Build foundational skills
2. **Progress to National Level** - Challenge advanced students
3. **Use Spam Modes** - Practice specific cipher types
4. **Review Generated Tests** - Verify difficulty matches your team's level

### Study Recommendations

- Master Aristocrats and Patristocrats first (most common)
- Practice Caesar and Affine for mathematical understanding
- Learn Vigenère before tackling Running-Key
- Study Hill cipher matrix operations separately
- Practice Morse-based ciphers (Morbit, Pollux) together

## 🌐 Web Interface Features

- **Responsive Design** - Works on desktop, tablet, and mobile
- **Visual Feedback** - See all 17 cipher types at a glance
- **Preset Selection** - Easy one-click test configuration
- **Real-time Generation** - Instant test creation
- **Download Support** - Save tests directly from browser

## 🏆 Science Olympiad 2025-2026

This generator is updated for the official 2025-2026 Science Olympiad CodeBusters rules, including all Division B and Division C ciphers.

Good luck to all competitors! 🎯
