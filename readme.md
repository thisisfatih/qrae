# QuantumSafeCipher-Prototype 🔒⚠️

**A single-file educational implementation of a lattice-based cryptographic scheme**  
_(Not secure - for learning purposes only)_

## 🚨 Critical Warning

**DO NOT USE FOR REAL CRYPTOGRAPHY**  
This is an experimental prototype demonstrating post-quantum cryptography concepts. It contains intentional vulnerabilities and lacks security reviews.

## 📖 Overview

Implements a simplified lattice-based cipher combining:

- **NTRU-inspired** polynomial arithmetic
- **Learning With Errors (LWE)** concepts
- Quantum-resistant design principles

## 📦 Features

- Single-file Python implementation
- Configurable parameters (for experimentation)
- Example encryption/decryption workflow
- Polynomial arithmetic demonstration

## ⚙️ Requirements

Python 3.6+
numpy (install with: pip install numpy)

## 🧪 Basic Usage

```bash
# Run demonstration (32-bit insecure version)
python3 quantumsafecipher.py
```

**Sample output:**

```text
⚠️ WARNING: THIS IMPLEMENTATION IS NOT SECURE ⚠️

Original message: [0 1 0 1]
Decrypted message: [0 1 0 1]

⚠️ REMINDER: DO NOT USE FOR ACTUAL SECURITY ⚠️
```

## 🔬 Educational Purpose

Use this to learn about:

- Lattice-based cryptography basics
- Polynomial ring operations
- Key generation/encryption/decryption flows
- Post-quantum cryptography concepts

## 🛑 Known Limitations

1. Tiny parameter sizes (insecure)
2. No error correction mechanisms
3. Vulnerable to multiple attacks
4. Unoptimized polynomial operations
5. No message encoding/decoding

## 📜 License

MIT License

---

**⚠️ Security Reminder:** This implementation has NOT been reviewed by cryptography experts. Real cryptographic systems require years of analysis and standardization. Always use established libraries like liboqs or OpenSSL for actual security needs.
