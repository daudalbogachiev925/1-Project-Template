import argparse
import subprocess
import shutil
from pathlib import Path

DEFAULT_PLATFORM = "C:/Program Files/1cv8/8.3.24.1548/bin/1cv8.exe"
DEFAULT_PLATFORM84 = "C:/Program Files/1cv8/8.3.24.1548/bin/1cv8.exe"

def find_platform(version="8.3"):
    candidates = Path("C:/Program Files/1cv8").glob(f"{version}*")
    for c in candidates:
        exe = c / "bin" / "1cv8.exe"
        if exe.exists():
            return str(exe)
    return DEFAULT_PLATFORM

def build(src_dir, out_dir, platform=None, config="Config.xml"):
    platform = platform or find_platform()
    src = Path(src_dir).resolve()
    out = Path(out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)

    cmd = [
        platform, "DESIGNER",
        "/F", str(out),
        "/LoadConfigFromFiles", str(src),
        "/UpdateDBCfg",
        "/Out", str(out / "build.log"),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print("BUILD FAILED")
        print(result.stdout)
        print(result.stderr)
        raise SystemExit(1)
    print(f"Build OK -> {out}")
    return out

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--src", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--platform", default=None)
    args = p.parse_args()
    build(args.src, args.out, args.platform)
