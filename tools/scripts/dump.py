import argparse
import subprocess
from pathlib import Path

def find_platform(version="8.3"):
    for c in Path("C:/Program Files/1cv8").glob(f"{version}*"):
        exe = c / "bin" / "1cv8.exe"
        if exe.exists():
            return str(exe)
    return None

def dump(ib_path, out_dir, user="", password="", platform=None):
    platform = platform or find_platform()
    out = Path(out_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    cmd = [
        platform, "DESIGNER",
        "/F", ib_path,
        "/DumpConfigToFiles", str(out),
        "/Out", str(out / "dump.log"),
    ]
    if user:
        cmd += ["/N", user]
    if password:
        cmd += ["/P", password]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(result.stdout, result.stderr)
        raise SystemExit(1)
    print(f"Dump OK -> {out}")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--ib", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--user", default="")
    p.add_argument("--password", default="")
    args = p.parse_args()
    dump(args.ib, args.out, args.user, args.password)
