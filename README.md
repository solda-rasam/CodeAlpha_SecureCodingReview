# CodeAlpha - Secure Coding Review (Vulnerability Assessment & Remediation)

A comprehensive security audit project demonstrating the identification, analysis, and professional remediation of common web application vulnerabilities (specifically SQL Injection and Cross-Site Scripting - XSS) within a Python Flask backend. Developed as part of the **CodeAlpha** Cyber Security Internship.

## 📋 Table of Contents
- [Overview](#-overview)
- [Project Architecture](#-project-architecture)
- [Vulnerabilities Identified](#-vulnerabilities-identified)
- [Remediation Strategy](#-remediation-strategy)
- [Installation & Setup](#-installation--setup)
- [How to Run the Audit & Apps](#-how-to-run-the-audit--apps)
- [Secure vs Vulnerable Comparison](#-secure-vs-vulnerable-comparison)

---

## 🔍 Overview
This project showcases a complete backend "Before & After" security lifecycle of a Flask-based application architecture. It features:
1. A **Vulnerable Application Backend** suffering from critical input-validation and query-concatenation flaws.
2. An **Automated Code Auditing Tool** designed to scan source scripts for insecure function calls and dangerous code patterns.
3. A patched, **Secure Application Backend** implementing industry-standard security mitigations (Parameterized queries and strict input processing).

## 📁 Project Architecture
```text
CodeAlpha_SecureCodingReview/
│
├── vulnerable_app.py   # Flask backend containing SQLi and XSS vulnerabilities
├── secure_app.py       # Patched Flask backend using secure coding practices
├── audit_tool.py       # Automated Python script that scans code files for security risks
└── README.md           # Comprehensive project documentation

```
## 🛡️ Vulnerabilities Identified & Remediation
### 1. SQL Injection (SQLi)
 * **The Risk:** User input from credentials fields was directly concatenated into raw SQL command strings. An attacker could bypass authentication logic entirely by injecting malicious SQL payloads (e.g., ' OR '1'='1).
 * **Insecure Code Pattern (vulnerable_app.py):**
   ```python
   cursor.execute(f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'")
   
   ```
 * **Remediation (secure_app.py):** Implemented **Parameterized Queries (Prepared Statements)** using standard database placeholders (?), strictly isolating execution logic from user-supplied data inputs.
### 2. Cross-Site Scripting (XSS)
 * **The Risk:** The backend processed user-submitted comments dynamically without escaping or encoding special HTML characters, allowing potential execution of unverified JavaScript payloads (<script>alert('XSS')</script>).
 * **Insecure Code Pattern (vulnerable_app.py):**
   ```python
   # Dynamic string rendering without safe context encoding or escaping
   
   ```
 * **Remediation (secure_app.py):** Enforced strict HTML context encoding and sanitization rules to render any raw script tags completely harmless to the client application.
## 🚀 Installation & Setup
 1. **Clone the Repository:**
```bash
git clone [https://github.com/solda-rasam/CodeAlpha_SecureCodingReview.git](https://github.com/solda-rasam/CodeAlpha_SecureCodingReview.git)
cd CodeAlpha_SecureCodingReview

```
 2. **Install Dependencies:**
```bash
pip install flask

```
## 💻 How to Run the Audit & Apps
### Step 1: Run the Automated Source Code Auditor
Execute the automated analysis tool against your backend scripts to locate insecure programming patterns:
```bash
python audit_tool.py

```
*Expected Output:* Flags critical query-handling flaws and lists dynamic functions located inside vulnerable_app.py.
### Step 2: Initialize and Test the Applications
Launch the application instances to evaluate server routing behaviors.
*Note: Since these scripts are optimized for raw security analysis and POST-method validation, attempting a direct browser GET connection on the /login route will yield a standard 405 Method Not Allowed server response, confirming that the restricted security policies are actively processing parameters.*
 * **To run the Vulnerable Backend instance:**
   ```bash
   python vulnerable_app.py
   
   ```
 * **To run the Secured Patched instance:**
   ```bash
   python secure_app.py
   
   ```
## 📊 Secure vs Vulnerable Comparison
| Feature / Attack Vector | vulnerable_app.py | secure_app.py | Mitigation Mechanism |
|---|---|---|---|
| **SQL Authentication Bypass** | ❌ Vulnerable | Secured | Parameterized SQL Binding (?) |
| **Script Payload Injection** | ❌ Vulnerable | Secured | Strict HTML Context Encoding |
| **Source Automated Scanning** | ⚠️ Risks Detected | Passed | Backend Refactoring & Hardening |
*Disclaimer: This repository is intended strictly for instructional use, educational review, and authorized security training assessments.*
```

