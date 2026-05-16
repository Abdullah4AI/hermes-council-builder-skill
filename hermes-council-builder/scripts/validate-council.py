#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate Hermes council profiles exist and have core files.")
    parser.add_argument("profiles_root", help="Usually ~/.hermes/profiles")
    parser.add_argument("profiles", nargs="+")
    args = parser.parse_args()
    root = Path(args.profiles_root).expanduser()
    ok = True
    for name in args.profiles:
        base = root / name
        required = [base, base / "SOUL.md", base / "PROFILE.md", base / "workspace" / name]
        missing = [path for path in required if not path.exists()]
        if missing:
            ok = False
            print(f"FAIL {name}: missing " + ", ".join(str(path) for path in missing))
        else:
            print(f"OK {name}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
