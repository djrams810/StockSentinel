# Scripts

This directory contains utility scripts for the StockSentinel project.

## Available Scripts

### validate.py

Validates configuration files for StockSentinel.

**Usage**:
```bash
python3 scripts/validate.py
```

**What it validates**:
- `.github/app.yml` - GitHub App manifest
- `examples/stock-config.json` - Example stock configuration
- `.gitignore` - Security patterns

**Requirements**:
- Python 3.6+
- PyYAML: `pip install pyyaml`

**Output**:
- ✓ Success messages for valid configurations
- ❌ Error messages for invalid configurations
- Exit code 0 on success, 1 on failure

## Adding New Scripts

When adding new scripts to this directory:

1. **Make it executable**:
   ```bash
   chmod +x scripts/your-script.sh
   ```

2. **Add shebang**:
   ```bash
   #!/usr/bin/env python3
   # or
   #!/bin/bash
   ```

3. **Document it**:
   - Add usage instructions
   - List requirements
   - Provide examples

4. **Update this README**:
   - Add script to the list above
   - Describe what it does
   - Include usage examples

## Common Use Cases

### Before Committing

Run validation to ensure all configurations are correct:
```bash
python3 scripts/validate.py
```

### Testing Changes

After modifying configuration files:
```bash
python3 scripts/validate.py
```

### Continuous Integration

Add validation to your CI pipeline:
```yaml
- name: Validate configurations
  run: python3 scripts/validate.py
```

## Troubleshooting

### Missing Dependencies

If you get import errors:
```bash
pip install pyyaml
```

### Permission Denied

Make scripts executable:
```bash
chmod +x scripts/*.py
```

### Path Issues

Run scripts from the repository root:
```bash
cd /path/to/StockSentinel
python3 scripts/validate.py
```
