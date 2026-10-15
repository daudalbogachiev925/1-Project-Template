import json
import sys

BLOCKING = {"Critical", "Major"}
ERROR_CODES = {
    "LineLength", "MissingSpace", "NestedTernaryOperator",
    "MagicNumber", "UsingHardcodePath",
}

def main(path):
    with open(path, encoding="utf-8") as f:
        report = json.load(f)
    issues = report.get("issues", [])
    blocking = [i for i in issues if i.get("severity") in BLOCKING
                or i.get("code") in ERROR_CODES]
    if blocking:
        for i in blocking:
            print(f"{i['file']}:{i.get('start_line','?')} [{i.get('severity')}] {i.get('message')}")
        sys.exit(1)
    print(f"BSL check passed ({len(issues)} warnings)")

if __name__ == "__main__":
    main(sys.argv[1])
