#!/bin/bash
# Release script for BAUERGROUP Hargassner Integration
# Usage: ./release.sh [version]
# Example: ./release.sh 0.1.1

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() { echo -e "${GREEN}✓ $1${NC}"; }
print_error() { echo -e "${RED}✗ $1${NC}"; }
print_info() { echo -e "${YELLOW}ℹ $1${NC}"; }

# Get version from parameter or ask user
if [ -z "$1" ]; then
    echo "Enter version number (e.g., 0.1.0):"
    read VERSION
else
    VERSION=$1
fi

# Validate version format (basic check)
if ! [[ $VERSION =~ ^[0-9]+\.[0-9]+\.[0-9]+$ ]]; then
    print_error "Invalid version format. Use semantic versioning (e.g., 0.1.0)"
    exit 1
fi

print_info "Starting release process for version v$VERSION"
echo ""

# Check for uncommitted changes
if ! git diff-index --quiet HEAD --; then
    print_error "You have uncommitted changes. Please commit or stash them first."
    git status --short
    exit 1
fi

print_success "No uncommitted changes found"

# Update version in manifest.json
print_info "Updating manifest.json version to $VERSION..."
if command -v jq &> /dev/null; then
    # Use jq if available (better JSON handling)
    jq --arg version "$VERSION" '.version = $version' custom_components/bauergroup_hargassnerintegration/manifest.json > manifest.tmp && mv manifest.tmp custom_components/bauergroup_hargassnerintegration/manifest.json
    print_success "Updated manifest.json using jq"
else
    # Fallback to sed
    sed -i.bak "s/\"version\": \".*\"/\"version\": \"$VERSION\"/" custom_components/bauergroup_hargassnerintegration/manifest.json
    rm -f custom_components/bauergroup_hargassnerintegration/manifest.json.bak
    print_success "Updated manifest.json using sed"
fi

# Update version in SCHNELLSTART.md
print_info "Updating SCHNELLSTART.md version to $VERSION..."
sed -i.bak "s/\*\*Version:\*\* .*/\*\*Version:\*\* $VERSION/" SCHNELLSTART.md
rm -f SCHNELLSTART.md.bak
print_success "Updated SCHNELLSTART.md"

# Git add changes
print_info "Staging version changes..."
git add custom_components/bauergroup_hargassnerintegration/manifest.json SCHNELLSTART.md
print_success "Staged manifest.json and SCHNELLSTART.md"

# Commit changes
print_info "Committing version bump..."
git commit -m "chore: Bump version to v$VERSION" || {
    print_info "No changes to commit (version already up to date)"
}

# Create git tag
print_info "Creating git tag v$VERSION..."
if git rev-parse "v$VERSION" >/dev/null 2>&1; then
    print_error "Tag v$VERSION already exists!"
    echo "Do you want to delete and recreate it? (y/n)"
    read -r response
    if [[ "$response" =~ ^[Yy]$ ]]; then
        git tag -d "v$VERSION"
        print_success "Deleted existing tag v$VERSION"
    else
        print_error "Aborted: Tag already exists"
        exit 1
    fi
fi

git tag -a "v$VERSION" -m "Release version v$VERSION"
print_success "Created tag v$VERSION"

# Push to remote
echo ""
print_info "Ready to push to remote repository"
echo "This will push:"
echo "  - Latest commits to main branch"
echo "  - Tag v$VERSION"
echo ""
echo "Continue? (y/n)"
read -r response

if [[ "$response" =~ ^[Yy]$ ]]; then
    print_info "Pushing to remote..."

    # Push commits
    git push origin main
    print_success "Pushed commits to main branch"

    # Push tag
    git push origin "v$VERSION"
    print_success "Pushed tag v$VERSION"

    echo ""
    print_success "Release v$VERSION completed successfully!"
    echo ""
    print_info "Next steps:"
    echo "  1. Create a GitHub release at: https://github.com/bauer-group/IP-HargassnerIntegration/releases/new?tag=v$VERSION"
    echo "  2. Wait for HACS to recognize the new version"
    echo "  3. Test installation via HACS"
else
    print_info "Push cancelled. You can push manually later with:"
    echo "  git push origin main"
    echo "  git push origin v$VERSION"
fi

echo ""
print_success "Done!"
