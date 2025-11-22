#!/usr/bin/env python3
"""
Release automation script for BAUERGROUP Hargassner Integration.

This script automates the release process by:
1. Validating version format
2. Updating version in all relevant files
3. Creating git commit and tag
4. Pushing to remote repository

Usage:
    python release.py [version]
    python release.py 0.1.1

If no version is provided, it will prompt for one.
"""

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Optional


class Colors:
    """ANSI color codes for terminal output."""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

    @classmethod
    def supports_color(cls) -> bool:
        """Check if terminal supports colors."""
        return (
            hasattr(sys.stdout, 'isatty') and sys.stdout.isatty() and
            os.environ.get('TERM') != 'dumb'
        )


def print_success(message: str) -> None:
    """Print success message in green."""
    if Colors.supports_color():
        print(f"{Colors.GREEN}✓ {message}{Colors.NC}")
    else:
        print(f"[OK] {message}")


def print_error(message: str) -> None:
    """Print error message in red."""
    if Colors.supports_color():
        print(f"{Colors.RED}✗ {message}{Colors.NC}")
    else:
        print(f"[ERROR] {message}")


def print_info(message: str) -> None:
    """Print info message in yellow."""
    if Colors.supports_color():
        print(f"{Colors.YELLOW}ℹ {message}{Colors.NC}")
    else:
        print(f"[INFO] {message}")


def print_step(message: str) -> None:
    """Print step message in blue."""
    if Colors.supports_color():
        print(f"{Colors.BLUE}▶ {message}{Colors.NC}")
    else:
        print(f">>> {message}")


def run_command(cmd: list[str], check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    """
    Run a shell command.

    Args:
        cmd: Command to run as list of arguments
        check: Whether to raise exception on non-zero exit code
        capture: Whether to capture output

    Returns:
        CompletedProcess object
    """
    try:
        if capture:
            result = subprocess.run(cmd, check=check, capture_output=True, text=True)
        else:
            result = subprocess.run(cmd, check=check)
        return result
    except subprocess.CalledProcessError as e:
        print_error(f"Command failed: {' '.join(cmd)}")
        if e.stderr:
            print(e.stderr)
        raise


def validate_version(version: str) -> bool:
    """
    Validate version format (semantic versioning).

    Args:
        version: Version string to validate

    Returns:
        True if valid, False otherwise
    """
    pattern = r'^\d+\.\d+\.\d+$'
    return bool(re.match(pattern, version))


def check_git_status() -> bool:
    """
    Check if there are uncommitted changes.

    Returns:
        True if working directory is clean, False otherwise
    """
    result = run_command(['git', 'diff-index', '--quiet', 'HEAD', '--'], check=False)
    return result.returncode == 0


def get_current_branch() -> str:
    """Get current git branch name."""
    result = run_command(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
    return result.stdout.strip()


def tag_exists(tag: str) -> bool:
    """Check if a git tag exists."""
    result = run_command(['git', 'rev-parse', tag], check=False)
    return result.returncode == 0


def update_manifest_version(version: str) -> None:
    """
    Update version in manifest.json.

    Args:
        version: New version string
    """
    manifest_path = Path('custom_components/bauergroup_hargassnerintegration/manifest.json')

    with open(manifest_path, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    manifest['version'] = version

    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
        f.write('\n')  # Add newline at end of file

    print_success(f"Updated {manifest_path}")


def update_schnellstart_version(version: str) -> None:
    """
    Update version in SCHNELLSTART.md.

    Args:
        version: New version string
    """
    schnellstart_path = Path('SCHNELLSTART.md')

    with open(schnellstart_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update version line
    content = re.sub(
        r'\*\*Version:\*\* .+',
        f'**Version:** {version}',
        content
    )

    with open(schnellstart_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print_success(f"Updated {schnellstart_path}")


def update_project_summary_version(version: str) -> None:
    """
    Update version in PROJECT_SUMMARY.md if it exists.

    Args:
        version: New version string
    """
    summary_path = Path('PROJECT_SUMMARY.md')

    if not summary_path.exists():
        return

    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update version line
    content = re.sub(
        r'\*\*Version:\*\* .+',
        f'**Version:** {version}',
        content
    )

    # Also update version in metadata if present
    content = re.sub(
        r'Version: .+',
        f'Version: {version}',
        content
    )

    with open(summary_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print_success(f"Updated {summary_path}")


def update_readme_badges(version: str) -> None:
    """
    Update version badge in README.md if it exists.

    Args:
        version: New version string
    """
    readme_path = Path('README.md')

    if not readme_path.exists():
        return

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Update version badge if present
    content = re.sub(
        r'!\[Version\]\(https://img\.shields\.io/badge/version-[\d.]+',
        f'![Version](https://img.shields.io/badge/version-{version}',
        content
    )

    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print_success(f"Updated {readme_path}")


def update_all_versions(version: str) -> list[Path]:
    """
    Update version in all relevant files.

    Args:
        version: New version string

    Returns:
        List of updated file paths
    """
    print_step(f"Updating version to {version} in all files...")

    updated_files = []

    # Update manifest.json
    update_manifest_version(version)
    updated_files.append(Path('custom_components/bauergroup_hargassnerintegration/manifest.json'))

    # Update SCHNELLSTART.md
    update_schnellstart_version(version)
    updated_files.append(Path('SCHNELLSTART.md'))

    # Update PROJECT_SUMMARY.md (if exists)
    update_project_summary_version(version)
    if Path('PROJECT_SUMMARY.md').exists():
        updated_files.append(Path('PROJECT_SUMMARY.md'))

    # Update README.md badges (if exists)
    update_readme_badges(version)
    if Path('README.md').exists():
        updated_files.append(Path('README.md'))

    return updated_files


def create_release(version: str, push: bool = True) -> None:
    """
    Create a release with the given version.

    Args:
        version: Version string (e.g., "0.1.1")
        push: Whether to push to remote
    """
    print()
    print_info(f"Starting release process for version v{version}")
    print()

    # Validate version format
    if not validate_version(version):
        print_error(f"Invalid version format: {version}")
        print_error("Version must follow semantic versioning (e.g., 0.1.0)")
        sys.exit(1)

    # Check for uncommitted changes
    if not check_git_status():
        print_error("You have uncommitted changes. Please commit or stash them first.")
        run_command(['git', 'status', '--short'], capture=False)
        sys.exit(1)

    print_success("No uncommitted changes found")
    print()

    # Update all version references
    updated_files = update_all_versions(version)
    print()

    # Stage all updated files
    print_step("Staging updated files...")
    for file_path in updated_files:
        run_command(['git', 'add', str(file_path)])
    print_success(f"Staged {len(updated_files)} files")
    print()

    # Commit changes
    print_step("Committing version bump...")
    commit_msg = f"chore: Bump version to v{version}"
    result = run_command(['git', 'commit', '-m', commit_msg], check=False)

    if result.returncode == 0:
        print_success(f"Created commit: {commit_msg}")
    else:
        print_info("No changes to commit (version already up to date)")
    print()

    # Handle existing tag
    tag_name = f"v{version}"
    if tag_exists(tag_name):
        print_error(f"Tag {tag_name} already exists!")
        response = input("Do you want to delete and recreate it? (y/n): ").strip().lower()
        if response == 'y':
            run_command(['git', 'tag', '-d', tag_name])
            print_success(f"Deleted existing tag {tag_name}")
        else:
            print_error("Aborted: Tag already exists")
            sys.exit(1)

    # Create tag
    print_step(f"Creating git tag {tag_name}...")
    tag_msg = f"Release version v{version}"
    run_command(['git', 'tag', '-a', tag_name, '-m', tag_msg])
    print_success(f"Created tag {tag_name}")
    print()

    # Push to remote
    if push:
        print_info("Ready to push to remote repository")
        print("This will push:")
        print(f"  - Latest commits to {get_current_branch()} branch")
        print(f"  - Tag {tag_name}")
        print()

        response = input("Continue? (y/n): ").strip().lower()

        if response == 'y':
            print_step("Pushing to remote...")
            print()

            # Push commits
            branch = get_current_branch()
            run_command(['git', 'push', 'origin', branch], capture=False)
            print_success(f"Pushed commits to {branch} branch")
            print()

            # Push tag
            run_command(['git', 'push', 'origin', tag_name], capture=False)
            print_success(f"Pushed tag {tag_name}")
            print()

            print_success(f"Release v{version} completed successfully!")
            print()
            print_info("Next steps:")
            print(f"  1. Create a GitHub release at: https://github.com/bauer-group/IP-HargassnerIntegration/releases/new?tag={tag_name}")
            print("  2. Wait for HACS to recognize the new version")
            print("  3. Test installation via HACS")
        else:
            print_info("Push cancelled. You can push manually later with:")
            print(f"  git push origin {get_current_branch()}")
            print(f"  git push origin {tag_name}")
    else:
        print_info("Skipping push (use --push to push automatically)")
        print_info("You can push manually with:")
        print(f"  git push origin {get_current_branch()}")
        print(f"  git push origin {tag_name}")

    print()
    print_success("Done!")


def main() -> None:
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Release automation script for BAUERGROUP Hargassner Integration",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python release.py 0.1.1
  python release.py 0.2.0 --no-push
  python release.py --help
        """
    )

    parser.add_argument(
        'version',
        nargs='?',
        help='Version number (e.g., 0.1.0)'
    )

    parser.add_argument(
        '--no-push',
        action='store_true',
        help='Do not push to remote (only create local commit and tag)'
    )

    args = parser.parse_args()

    # Get version from argument or prompt
    version = args.version
    if not version:
        version = input("Enter version number (e.g., 0.1.0): ").strip()

    if not version:
        print_error("Version is required")
        sys.exit(1)

    # Create release
    try:
        create_release(version, push=not args.no_push)
    except KeyboardInterrupt:
        print()
        print_error("Aborted by user")
        sys.exit(1)
    except Exception as e:
        print()
        print_error(f"Release failed: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
