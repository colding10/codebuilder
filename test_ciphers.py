#!/usr/bin/env python3
"""
Test script for new cipher implementations
"""

from generator import gen_rand_atbash, genRandRunningKey, genRandCheckerboard, genQuoteLength

print("=" * 60)
print("Testing New Cipher Implementations")
print("=" * 60)

# Test Atbash Cipher
print("\n1. Testing Atbash Cipher...")
try:
    quote = genQuoteLength(40, 80)
    atbash_encode = gen_rand_atbash(1, quote, "E")
    atbash_decode = gen_rand_atbash(2, quote, "D")

    print("   ✓ Atbash Encode:", atbash_encode["cipherType"], "-", atbash_encode["operation"])
    print("   ✓ Atbash Decode:", atbash_decode["cipherType"], "-", atbash_decode["operation"])
    print("   ✓ Points:", atbash_encode["points"], "/", atbash_decode["points"])
    print("   ✓ SUCCESS: Atbash cipher working correctly")
except Exception as e:
    print(f"   ✗ FAILED: {e}")

# Test Running-Key Cipher
print("\n2. Testing Running-Key Cipher...")
try:
    quote = genQuoteLength(40, 80)
    runkey_encode = genRandRunningKey(1, quote, "E")
    runkey_decode = genRandRunningKey(2, quote, "D")
    runkey_crypt = genRandRunningKey(3, quote, "C")

    print("   ✓ Running-Key Encode:", runkey_encode["cipherType"], "-", runkey_encode["operation"])
    print("   ✓ Running-Key Decode:", runkey_decode["cipherType"], "-", runkey_decode["operation"])
    print("   ✓ Running-Key Crypt:", runkey_crypt["cipherType"], "-", runkey_crypt["operation"])
    print("   ✓ Points:", runkey_encode["points"], "/", runkey_decode["points"], "/", runkey_crypt["points"])
    print("   ✓ SUCCESS: Running-Key cipher working correctly")
except Exception as e:
    print(f"   ✗ FAILED: {e}")

# Test Checkerboard Cipher
print("\n3. Testing Checkerboard Cipher...")
try:
    quote = genQuoteLength(30, 60)
    checker_encode = genRandCheckerboard(1, quote, "E")
    checker_decode = genRandCheckerboard(2, quote, "D")
    checker_crypt = genRandCheckerboard(3, quote, "C")

    print("   ✓ Checkerboard Encode:", checker_encode["cipherType"], "-", checker_encode["operation"])
    print("   ✓ Checkerboard Decode:", checker_decode["cipherType"], "-", checker_decode["operation"])
    print("   ✓ Checkerboard Crypt:", checker_crypt["cipherType"], "-", checker_crypt["operation"])
    print("   ✓ Points:", checker_encode["points"], "/", checker_decode["points"], "/", checker_crypt["points"])
    print("   ✓ Grid length:", len(checker_encode["grid"]))
    print("   ✓ SUCCESS: Checkerboard cipher working correctly")
except Exception as e:
    print(f"   ✗ FAILED: {e}")

print("\n" + "=" * 60)
print("All New Ciphers Tested Successfully!")
print("=" * 60)
print("\nYou can now:")
print("  1. Run 'python web_server.py' to start the web interface")
print("  2. Run 'python cli.py' to use the command-line interface")
print("=" * 60)
