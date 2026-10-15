import subprocess
from pathlib import Path

def find_platform(version="8.3"):
    for c in Path("C:/Program Files/1cv8").glob(f"{version}*"):
        exe = c / "bin" / "1cv8.exe"
        if exe.exists():
            return str(exe)
    return None

def create_ib(ib_path, platform=None):
    platform = platform or find_platform()
    Path(ib_path).mkdir(parents=True, exist_ok=True)
    cmd = [platform, "CREATEINFOBASE", f"File={ib_path}"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout, result.stderr)
        raise SystemExit(1)
    print(f"IB created -> {ib_path}")

if __name__ == "__main__":
    create_ib("./ib")
