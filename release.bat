@echo off
REM Release script for BAUERGROUP Hargassner Integration
REM Usage: release.bat [version]
REM Example: release.bat 0.1.1

setlocal enabledelayedexpansion

REM Get version from parameter or ask user
if "%~1"=="" (
    set /p VERSION="Enter version number (e.g., 0.1.0): "
) else (
    set VERSION=%~1
)

REM Validate version format (basic check)
echo %VERSION% | findstr /R "^[0-9][0-9]*\.[0-9][0-9]*\.[0-9][0-9]*$" >nul
if errorlevel 1 (
    echo [ERROR] Invalid version format. Use semantic versioning (e.g., 0.1.0)
    exit /b 1
)

echo.
echo [INFO] Starting release process for version v%VERSION%
echo.

REM Check for uncommitted changes
git diff-index --quiet HEAD -- 2>nul
if errorlevel 1 (
    echo [ERROR] You have uncommitted changes. Please commit or stash them first.
    git status --short
    exit /b 1
)

echo [OK] No uncommitted changes found
echo.

REM Update version in manifest.json
echo [INFO] Updating manifest.json version to %VERSION%...
powershell -Command "(Get-Content custom_components\bauergroup_hargassnerintegration\manifest.json) -replace '\"version\": \".*\"', '\"version\": \"%VERSION%\"' | Set-Content custom_components\bauergroup_hargassnerintegration\manifest.json"
if errorlevel 1 (
    echo [ERROR] Failed to update manifest.json
    exit /b 1
)
echo [OK] Updated manifest.json

REM Update version in SCHNELLSTART.md
echo [INFO] Updating SCHNELLSTART.md version to %VERSION%...
powershell -Command "(Get-Content SCHNELLSTART.md) -replace '\*\*Version:\*\* .*', '**Version:** %VERSION%' | Set-Content SCHNELLSTART.md"
if errorlevel 1 (
    echo [ERROR] Failed to update SCHNELLSTART.md
    exit /b 1
)
echo [OK] Updated SCHNELLSTART.md
echo.

REM Git add changes
echo [INFO] Staging version changes...
git add custom_components\bauergroup_hargassnerintegration\manifest.json SCHNELLSTART.md
if errorlevel 1 (
    echo [ERROR] Failed to stage changes
    exit /b 1
)
echo [OK] Staged manifest.json and SCHNELLSTART.md

REM Commit changes
echo [INFO] Committing version bump...
git commit -m "chore: Bump version to v%VERSION%"
if errorlevel 1 (
    echo [INFO] No changes to commit (version already up to date)
)
echo.

REM Check if tag already exists
git rev-parse v%VERSION% >nul 2>&1
if not errorlevel 1 (
    echo [WARNING] Tag v%VERSION% already exists!
    set /p RECREATE="Do you want to delete and recreate it? (y/n): "
    if /i "!RECREATE!"=="y" (
        git tag -d v%VERSION%
        echo [OK] Deleted existing tag v%VERSION%
    ) else (
        echo [ERROR] Aborted: Tag already exists
        exit /b 1
    )
)

REM Create git tag
echo [INFO] Creating git tag v%VERSION%...
git tag -a v%VERSION% -m "Release version v%VERSION%"
if errorlevel 1 (
    echo [ERROR] Failed to create tag
    exit /b 1
)
echo [OK] Created tag v%VERSION%
echo.

REM Push to remote
echo [INFO] Ready to push to remote repository
echo This will push:
echo   - Latest commits to main branch
echo   - Tag v%VERSION%
echo.
set /p PUSH="Continue? (y/n): "

if /i "%PUSH%"=="y" (
    echo [INFO] Pushing to remote...
    echo.

    REM Push commits
    git push origin main
    if errorlevel 1 (
        echo [ERROR] Failed to push commits
        exit /b 1
    )
    echo [OK] Pushed commits to main branch

    REM Push tag
    git push origin v%VERSION%
    if errorlevel 1 (
        echo [ERROR] Failed to push tag
        exit /b 1
    )
    echo [OK] Pushed tag v%VERSION%
    echo.

    echo [SUCCESS] Release v%VERSION% completed successfully!
    echo.
    echo [INFO] Next steps:
    echo   1. Create a GitHub release at: https://github.com/bauer-group/IP-HargassnerIntegration/releases/new?tag=v%VERSION%
    echo   2. Wait for HACS to recognize the new version
    echo   3. Test installation via HACS
) else (
    echo [INFO] Push cancelled. You can push manually later with:
    echo   git push origin main
    echo   git push origin v%VERSION%
)

echo.
echo [SUCCESS] Done!

endlocal
