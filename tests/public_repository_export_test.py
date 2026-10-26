#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
import hashlib
import json
import pathlib
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]


def run(kind: str, name: str) -> pathlib.Path:
    out = ROOT / "build" / name
    subprocess.run(["python3", str(ROOT / "scripts/export-public-repositories.py"), kind, str(out)], check=True)
    return out


def tree_digest(root: pathlib.Path) -> str:
    value = hashlib.sha256()
    for path in sorted(item for item in root.rglob("*") if item.is_file()):
        value.update(path.relative_to(root).as_posix().encode())
        value.update(path.read_bytes())
    return value.hexdigest()


runtime_a, runtime_b = run("runtime", "public-runtime-a"), run("runtime", "public-runtime-b")
catalog_a, catalog_b = run("catalog", "public-catalog-a"), run("catalog", "public-catalog-b")
assert tree_digest(runtime_a) == tree_digest(runtime_b)
assert tree_digest(catalog_a) == tree_digest(catalog_b)
assert not (runtime_a / "web").exists()
assert not (runtime_a / "openspec").exists()
assert not (catalog_a / "src").exists()
assert not (catalog_a / ".vercel").exists()
assert not (catalog_a / ".env.local").exists()
for root, kind in ((runtime_a, "runtime"), (catalog_a, "catalog")):
    inventory = json.loads((root / "PUBLIC-SOURCE-INVENTORY.json").read_text())
    assert inventory["kind"] == kind
    assert len(inventory["files"]) > 10
    for forbidden in (b"-----BEGIN " + b"PRIVATE KEY-----", b"VERCEL_TOKEN" + b"=", b"CONVEX_DEPLOY_KEY" + b"="):
        assert all(forbidden not in path.read_bytes() for path in root.rglob("*") if path.is_file())
print("PASS: deterministic allowlisted runtime/catalog exports and forbidden-boundary checks")
