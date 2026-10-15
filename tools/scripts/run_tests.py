import subprocess
import sys
from pathlib import Path

def run(epf, ib, user="", password=""):
    cmd = [
        "1cv8.exe", "ENTERPRISE",
        "/F", ib,
        "/Execute", epf,
        "/C", "vanessa",
        "/Out", "test.log",
    ]
    if user:
        cmd += ["/N", user]
    if password:
        cmd += ["/P", password]
    result = subprocess.run(cmd, capture_output=True, text=True)
    log = Path("test.log").read_text(encoding="utf-8", errors="ignore") if Path("test.log").exists() else ""
    if "FAIL" in log or result.returncode != 0:
        print(log)
        sys.exit(1)
    print("Tests OK")

if __name__ == "__main__":
    run("tools/vanessa/vanessa-automation.epf", "./ib")
