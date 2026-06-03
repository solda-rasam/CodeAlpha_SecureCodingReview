import sys

def perform_code_review(file_path):
    print(f"[*] Starting Security Audit on: {file_path}...\n")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        return

    vulnerabilities_found = 0

    for line_num, line in enumerate(lines, 1):
        
        if "execute(" in line and ("f\"" in line or "query" in line or "f'" in line):
            print(f"[!] CRITICAL: Potential SQL Injection found at line {line_num}!")
            print(f"    Code: {line.strip()}")
            print(f"    Recommendation: Use parameterized queries instead of string formatting.\n")
            vulnerabilities_found += 1

       
        if "render_template_string(" in line:
            print(f"[!] HIGH: Potential Cross-Site Scripting (XSS) found at line {line_num}!")
            print(f"    Code: {line.strip()}")
            print(f"    Recommendation: Use standard render_template() with auto-escaping.\n")
            vulnerabilities_found += 1

    print(f"[*] Audit Complete. Total Vulnerabilities Found: {vulnerabilities_found}")

if __name__ == "__main__":
    perform_code_review("vulnerable_app.py")