# Publishing to PyPI

This guide explains how to publish svg2png-clipboard to PyPI.

## Prerequisites

1. Create accounts:
   - [PyPI account](https://pypi.org/account/register/)
   - [Test PyPI account](https://test.pypi.org/account/register/) (optional, for testing)

2. Install publishing tools:
   ```bash
   pip install --upgrade build twine
   ```

3. Configure PyPI credentials (recommended: use API tokens)
   ```bash
   # Create ~/.pypirc file
   cat > ~/.pypirc << EOF
   [distutils]
   index-servers =
       pypi
       testpypi

   [pypi]
   username = __token__
   password = pypi-YOUR-API-TOKEN-HERE

   [testpypi]
   username = __token__
   password = pypi-YOUR-TEST-API-TOKEN-HERE
   EOF
   
   chmod 600 ~/.pypirc
   ```

## Publishing Steps

### 1. Update Version

Edit `pyproject.toml` and update the version number:
```toml
version = "0.1.1"  # Increment as needed
```

### 2. Clean Previous Builds

```bash
rm -rf dist/ build/ *.egg-info/
```

### 3. Build the Package

```bash
python -m build
```

This creates:
- `dist/svg2png_clipboard-0.1.0.tar.gz` (source distribution)
- `dist/svg2png_clipboard-0.1.0-py3-none-any.whl` (wheel)

### 4. Test the Build (Optional)

```bash
# Check the package
twine check dist/*

# Test in a new virtual environment
python -m venv test-env
source test-env/bin/activate
pip install dist/svg2png_clipboard-0.1.0-py3-none-any.whl
svg2png-clipboard --help
deactivate
rm -rf test-env
```

### 5. Upload to Test PyPI (Optional)

```bash
twine upload --repository testpypi dist/*

# Test installation from Test PyPI
pip install --index-url https://test.pypi.org/simple/ svg2png-clipboard
```

### 6. Upload to PyPI

```bash
twine upload dist/*
```

### 7. Verify Installation

Wait a few minutes, then:
```bash
pip install svg2png-clipboard
# or
pipx install svg2png-clipboard
```

## Version Management

Follow semantic versioning:
- MAJOR.MINOR.PATCH (e.g., 1.2.3)
- MAJOR: Breaking changes
- MINOR: New features (backwards compatible)
- PATCH: Bug fixes

## Checklist Before Publishing

- [ ] Update version in `pyproject.toml`
- [ ] Update CHANGELOG (if you have one)
- [ ] Ensure all tests pass
- [ ] Update documentation if needed
- [ ] Commit all changes
- [ ] Tag the release: `git tag v0.1.0`
- [ ] Push tags: `git push origin --tags`

## Troubleshooting

### "Invalid distribution file"
- Ensure you're using the latest `build` and `twine`
- Check that all required files are included in MANIFEST.in

### "Package name already exists"
- The name `svg2png-clipboard` must be unique on PyPI
- Consider alternative names like:
  - `svg2png-clip`
  - `svgclip2png`
  - `clipboard-svg2png`

### Authentication Issues
- Use API tokens instead of username/password
- Create tokens at https://pypi.org/manage/account/token/

## After Publishing

1. Create a GitHub release with the same version tag
2. Update README with PyPI badge:
   ```markdown
   [![PyPI version](https://badge.fury.io/py/svg2png-clipboard.svg)](https://badge.fury.io/py/svg2png-clipboard)
   ```