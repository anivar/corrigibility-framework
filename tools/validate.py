#!/usr/bin/env python3
"""
Validator for Corrigibility Framework schemas.

Usage:
    python validate.py infrastructure manifest.json
    python validate.py assessment assessment.json
    python validate.py all directory/
"""

import json
import sys
from pathlib import Path
from urllib.request import urlopen
from urllib.error import URLError

# Schema URLs
SCHEMA_URLS = {
    "infrastructure": "https://indiastack.in/dpi/schema/infrastructure.json",
    "assessment": "https://indiastack.in/dpi/schema/corrigibility.json"
}

def load_json(path: str) -> dict:
    """Load JSON from file path."""
    with open(path, 'r') as f:
        return json.load(f)

def fetch_schema(schema_type: str) -> dict:
    """Fetch schema from URL or local cache."""
    # Try local first
    local_path = Path(__file__).parent.parent / "schema" / f"{schema_type}.json"
    if schema_type == "assessment":
        local_path = Path(__file__).parent.parent / "schema" / "corrigibility.json"

    if local_path.exists():
        return load_json(str(local_path))

    # Fetch from URL
    try:
        with urlopen(SCHEMA_URLS[schema_type]) as response:
            return json.loads(response.read().decode())
    except URLError as e:
        print(f"Error fetching schema: {e}")
        sys.exit(1)

def validate_required_fields(data: dict, required: list, path: str = "") -> list:
    """Check for required fields."""
    errors = []
    for field in required:
        if field not in data:
            errors.append(f"Missing required field: {path}{field}")
    return errors

def validate_infrastructure(data: dict) -> list:
    """Validate infrastructure manifest."""
    errors = []

    # Required top-level
    errors.extend(validate_required_fields(data, ["meta", "access"]))

    # meta.system_id and meta.lifecycle required
    if "meta" in data:
        errors.extend(validate_required_fields(
            data["meta"], ["system_id", "lifecycle"], "meta."
        ))

        # Validate lifecycle enum
        valid_lifecycle = ["active", "deprecated", "sunset", "archived"]
        if data["meta"].get("lifecycle") not in valid_lifecycle:
            errors.append(f"Invalid lifecycle value. Must be one of: {valid_lifecycle}")

    # access.offline_equivalent required
    if "access" in data:
        errors.extend(validate_required_fields(
            data["access"], ["offline_equivalent"], "access."
        ))

        if "offline_equivalent" in data["access"]:
            if not isinstance(data["access"]["offline_equivalent"], bool):
                errors.append("access.offline_equivalent must be boolean")

    return errors

def validate_assessment(data: dict) -> list:
    """Validate corrigibility assessment."""
    errors = []

    # Required top-level
    errors.extend(validate_required_fields(data, ["target", "assessed_by", "tests"]))

    # All five tests required
    if "tests" in data:
        required_tests = ["exit", "code", "audit", "govern", "fork"]
        errors.extend(validate_required_fields(
            data["tests"], required_tests, "tests."
        ))

        # Each test should have pass boolean
        for test in required_tests:
            if test in data["tests"]:
                if "pass" not in data["tests"][test]:
                    errors.append(f"tests.{test}.pass is required")
                elif not isinstance(data["tests"][test]["pass"], bool):
                    errors.append(f"tests.{test}.pass must be boolean")

    # Validate verdict if present
    if "verdict" in data:
        if "corrigible" in data["verdict"]:
            if not isinstance(data["verdict"]["corrigible"], bool):
                errors.append("verdict.corrigible must be boolean")

            # Check consistency
            if "tests" in data:
                all_pass = all(
                    data["tests"].get(t, {}).get("pass", False)
                    for t in ["exit", "code", "audit", "govern", "fork"]
                )
                if data["verdict"]["corrigible"] != all_pass:
                    errors.append(
                        "verdict.corrigible inconsistent with test results. "
                        "Corrigible requires all five tests to pass."
                    )

    return errors

def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)

    schema_type = sys.argv[1]
    target = sys.argv[2]

    if schema_type not in ["infrastructure", "assessment", "all"]:
        print(f"Unknown schema type: {schema_type}")
        print("Use: infrastructure, assessment, or all")
        sys.exit(1)

    if schema_type == "all":
        # Validate all JSON files in directory
        directory = Path(target)
        if not directory.is_dir():
            print(f"Not a directory: {target}")
            sys.exit(1)

        all_errors = {}
        for json_file in directory.glob("**/*.json"):
            data = load_json(str(json_file))

            # Guess type from content
            if "tests" in data:
                errors = validate_assessment(data)
            elif "meta" in data:
                errors = validate_infrastructure(data)
            else:
                errors = ["Unknown schema type"]

            if errors:
                all_errors[str(json_file)] = errors

        if all_errors:
            for file, errors in all_errors.items():
                print(f"\n{file}:")
                for error in errors:
                    print(f"  - {error}")
            sys.exit(1)
        else:
            print(f"All files valid in {target}")
            sys.exit(0)

    # Single file validation
    try:
        data = load_json(target)
    except json.JSONDecodeError as e:
        print(f"Invalid JSON: {e}")
        sys.exit(1)
    except FileNotFoundError:
        print(f"File not found: {target}")
        sys.exit(1)

    if schema_type == "infrastructure":
        errors = validate_infrastructure(data)
    else:
        errors = validate_assessment(data)

    if errors:
        print(f"Validation errors in {target}:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)
    else:
        print(f"Valid {schema_type}: {target}")
        sys.exit(0)

if __name__ == "__main__":
    main()
