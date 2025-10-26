#!/usr/bin/env python3
"""
Validation script for StockSentinel GitHub App configuration files.
This script validates the app manifest and example configurations.
"""

import json
import yaml
import sys
import os


def validate_app_manifest(file_path):
    """Validate the GitHub App manifest file."""
    print(f"Validating app manifest: {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            manifest = yaml.safe_load(f)
        
        # Check required fields
        required_fields = ['name', 'description', 'url', 'default_permissions']
        missing_fields = [field for field in required_fields if field not in manifest]
        
        if missing_fields:
            print(f"❌ Missing required fields: {', '.join(missing_fields)}")
            return False
        
        # Validate permissions structure
        if not isinstance(manifest['default_permissions'], dict):
            print("❌ default_permissions must be a dictionary")
            return False
        
        # Validate events
        if 'default_events' in manifest:
            if not isinstance(manifest['default_events'], list):
                print("❌ default_events must be a list")
                return False
        
        print("✓ App manifest is valid!")
        print(f"  - Name: {manifest['name']}")
        print(f"  - Description: {manifest['description']}")
        print(f"  - Permissions: {', '.join(manifest['default_permissions'].keys())}")
        if 'default_events' in manifest:
            print(f"  - Events: {', '.join(manifest['default_events'])}")
        
        return True
        
    except yaml.YAMLError as e:
        print(f"❌ YAML parsing error: {e}")
        return False
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False


def validate_stock_config(file_path):
    """Validate the example stock configuration file."""
    print(f"\nValidating stock configuration: {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            config = json.load(f)
        
        # Check required fields
        if 'stocks' not in config:
            print("❌ Missing 'stocks' field")
            return False
        
        if not isinstance(config['stocks'], list):
            print("❌ 'stocks' must be a list")
            return False
        
        # Validate each stock
        for idx, stock in enumerate(config['stocks']):
            if 'symbol' not in stock:
                print(f"❌ Stock at index {idx} missing 'symbol' field")
                return False
        
        print("✓ Stock configuration is valid!")
        print(f"  - Stocks tracked: {len(config['stocks'])}")
        if config['stocks']:
            symbols = [s['symbol'] for s in config['stocks']]
            print(f"  - Symbols: {', '.join(symbols)}")
        
        return True
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False


def validate_gitignore(file_path):
    """Validate the .gitignore file."""
    print(f"\nValidating .gitignore: {file_path}")
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        
        # Check for important patterns
        important_patterns = ['*.pem', '.env', 'secrets/', 'node_modules/']
        found_patterns = [p for p in important_patterns if p in content]
        
        if len(found_patterns) == len(important_patterns):
            print("✓ .gitignore contains all important security patterns!")
            print(f"  - Patterns: {', '.join(important_patterns)}")
            return True
        else:
            missing = set(important_patterns) - set(found_patterns)
            print(f"⚠ Missing some important patterns: {', '.join(missing)}")
            return True  # Still valid, just a warning
            
    except Exception as e:
        print(f"❌ Validation error: {e}")
        return False


def main():
    """Run all validations."""
    print("=" * 60)
    print("StockSentinel Configuration Validation")
    print("=" * 60)
    
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    validations = [
        ('.github/app.yml', validate_app_manifest),
        ('examples/stock-config.json', validate_stock_config),
        ('.gitignore', validate_gitignore),
    ]
    
    all_valid = True
    for file_path, validator in validations:
        full_path = os.path.join(base_dir, file_path)
        if os.path.exists(full_path):
            if not validator(full_path):
                all_valid = False
        else:
            print(f"\n⚠ File not found: {file_path}")
            all_valid = False
    
    print("\n" + "=" * 60)
    if all_valid:
        print("✓ All validations passed!")
        print("=" * 60)
        return 0
    else:
        print("❌ Some validations failed!")
        print("=" * 60)
        return 1


if __name__ == '__main__':
    sys.exit(main())
