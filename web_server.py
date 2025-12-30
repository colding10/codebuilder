#!/usr/bin/env python3
"""
Flask web server for CodeBuilder - Science Olympiad Cipher Test Generator
"""

from flask import Flask, render_template, request, jsonify, send_file
from generator import *
from cli import *
import json
import os

app = Flask(__name__, static_folder=".", template_folder=".")


@app.route("/")
def index():
    """Serve the main HTML page"""
    return send_file("web_ui.html")


@app.route("/api/generate", methods=["POST"])
def generate_test():
    """Generate a cipher test based on the provided configuration"""
    try:
        data = request.json
        test_name = data.get("testName", "Test")
        preset = data.get("preset", "all")
        custom_count = int(data.get("customCount", 100))

        # Generate test questions based on preset
        if preset == "all":
            question_list = generate_all_types_exam()
        elif preset == "national":
            question_list = generate_national_exam()
        elif preset == "regional":
            question_list = generate_regional_exam()
        elif preset == "aristo":
            question_list = ["1 2"] * custom_count
        elif preset == "patristo":
            question_list = ["2 2"] * custom_count
        else:
            return jsonify({"error": "Invalid preset"}), 400

        n = len(question_list)

        # Generate quotes
        quotes = genQuotes(n + 1)

        # Build test structure
        test = {"TEST.0": header(n, test_name)}
        test["CIPHER.0"] = gen_rand_mono(0, quotes[len(quotes) - 1], False, 0)

        # Generate each cipher question
        for i in range(n):
            question = question_list[i].split(" ")
            test[f"CIPHER.{i + 1}"] = generate_question(question, i, quotes)

        # Save to file
        output_dir = "CodeTests"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        output_path = os.path.join(output_dir, f"{test_name}.json")
        with open(output_path, "w") as file:
            file.write(json.dumps(test, indent=2))

        return jsonify(
            {
                "success": True,
                "message": f"Test '{test_name}' generated successfully!",
                "filename": f"{test_name}.json",
                "questionCount": n,
                "path": output_path,
            }
        )

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/ciphers", methods=["GET"])
def get_ciphers():
    """Return list of supported ciphers"""
    ciphers = [
        {
            "id": 1,
            "name": "Aristocrat",
            "description": "Monoalphabetic substitution with spaces",
        },
        {
            "id": 2,
            "name": "Patristocrat",
            "description": "Monoalphabetic without spaces",
        },
        {"id": 3, "name": "Affine Cipher", "description": "Linear mathematical substitution"},
        {"id": 4, "name": "Atbash", "description": "Simple reverse alphabet", "new": True},
        {"id": 5, "name": "Caesar Cipher", "description": "Fixed shift substitution"},
        {"id": 6, "name": "Vigenère Cipher", "description": "Polyalphabetic keyword cipher"},
        {"id": 7, "name": "Hill Cipher (2×2)", "description": "Matrix-based encryption"},
        {"id": 8, "name": "Hill Cipher (3×3)", "description": "Advanced matrix encryption"},
        {"id": 9, "name": "Xenocrypt", "description": "Spanish aristocrat"},
        {"id": 10, "name": "Baconian Cipher", "description": "Binary A/B encoding"},
        {"id": 11, "name": "RSA", "description": "Public key cryptography"},
        {"id": 12, "name": "Morbit Cipher", "description": "Morse code with digits"},
        {"id": 13, "name": "Pollux Cipher", "description": "Morse with random mappings"},
        {"id": 14, "name": "Porta Cipher", "description": "Polyalphabetic tableau"},
        {
            "id": 15,
            "name": "Running-Key",
            "description": "Continuous text as key",
            "new": True,
        },
        {"id": 16, "name": "Rail Fence", "description": "Transposition cipher"},
        {
            "id": 17,
            "name": "Checkerboard",
            "description": "Polybius square cipher",
            "new": True,
        },
    ]
    return jsonify(ciphers)


@app.route("/api/tests", methods=["GET"])
def list_tests():
    """List all generated tests"""
    try:
        output_dir = "CodeTests"
        if not os.path.exists(output_dir):
            return jsonify([])

        tests = []
        for filename in os.listdir(output_dir):
            if filename.endswith(".json"):
                filepath = os.path.join(output_dir, filename)
                with open(filepath, "r") as f:
                    data = json.load(f)
                    test_info = data.get("TEST.0", {})
                    tests.append(
                        {
                            "filename": filename,
                            "title": test_info.get("title", filename),
                            "count": test_info.get("count", 0),
                        }
                    )

        return jsonify(tests)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/api/download/<filename>", methods=["GET"])
def download_test(filename):
    """Download a generated test file"""
    try:
        # Prevent path traversal by restricting to a simple base filename
        safe_filename = os.path.basename(filename)
        if safe_filename != filename:
            return jsonify({"error": "Invalid filename"}), 400

        filepath = os.path.join("CodeTests", safe_filename)
        if os.path.exists(filepath):
            return send_file(filepath, as_attachment=True)
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    print("=" * 60)
    print("CodeBuilder - Science Olympiad Cipher Test Generator")
    print("2025-2026 Season - Web Interface")
    print("=" * 60)
    print("\nServer starting...")
    print("Access the web interface at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    print("=" * 60)
    app.run(debug=True, host="0.0.0.0", port=5000)
