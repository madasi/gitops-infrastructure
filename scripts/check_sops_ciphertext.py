#!/usr/bin/env python3
"""Check SOPS YAML files for expected metadata and encrypted payload values.

This validates file structure only. It never invokes SOPS or decrypts values.
"""

from pathlib import Path

import yaml


def is_ciphertext(value: object) -> bool:
    return isinstance(value, str) and value.startswith("ENC[")


def payload_leaves(value: object):
    if isinstance(value, dict):
        for child in value.values():
            yield from payload_leaves(child)
    elif isinstance(value, list):
        for child in value:
            yield from payload_leaves(child)
    else:
        yield value


def check_file(path: Path) -> list[str]:
    errors = []
    try:
        document = yaml.safe_load(path.read_text(encoding="utf-8"))
    except (OSError, yaml.YAMLError) as error:
        return [f"{path}: cannot parse YAML ({error})"]

    if not isinstance(document, dict):
        return [f"{path}: expected a YAML mapping"]

    metadata = document.get("sops")
    if not isinstance(metadata, dict):
        errors.append(f"{path}: missing SOPS metadata mapping")
        return errors

    age_recipients = metadata.get("age")
    if not isinstance(age_recipients, list) or not age_recipients:
        errors.append(f"{path}: missing SOPS age recipient metadata")
    elif any(
        not isinstance(recipient, dict)
        or not isinstance(recipient.get("recipient"), str)
        or not isinstance(recipient.get("enc"), str)
        for recipient in age_recipients
    ):
        errors.append(f"{path}: malformed SOPS age recipient metadata")

    if not is_ciphertext(metadata.get("mac")):
        errors.append(f"{path}: missing encrypted SOPS integrity metadata")
    if not isinstance(metadata.get("version"), str):
        errors.append(f"{path}: missing SOPS version metadata")

    payload = {key: value for key, value in document.items() if key != "sops"}
    leaves = list(payload_leaves(payload))
    if not leaves:
        errors.append(f"{path}: no encrypted payload values found")
    elif any(not is_ciphertext(value) for value in leaves):
        errors.append(f"{path}: found payload value(s) that are not SOPS ciphertext")

    return errors


def main() -> int:
    files = sorted(
        path
        for path in Path(".").rglob("*.sops.yaml")
        if ".git" not in path.parts and path.name != ".sops.yaml"
    )
    files += sorted(
        path
        for path in Path(".").rglob("*.sops.yml")
        if ".git" not in path.parts and path.name != ".sops.yml"
    )
    if not files:
        print("No SOPS YAML files found.")
        return 1

    errors = [error for path in files for error in check_file(path)]
    if errors:
        print("\n".join(errors))
        return 1

    print(f"Validated SOPS metadata and encrypted payloads in {len(files)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
