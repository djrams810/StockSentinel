# Contributing to StockSentinel

Thank you for your interest in contributing to StockSentinel! This document provides guidelines for contributing to the project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [Development Setup](#development-setup)
- [Making Changes](#making-changes)
- [Testing](#testing)
- [Submitting Changes](#submitting-changes)
- [GitHub App Development](#github-app-development)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment for all contributors.

## Getting Started

1. **Fork the Repository**: Click the "Fork" button at the top of this repository
2. **Clone Your Fork**: 
   ```bash
   git clone https://github.com/YOUR-USERNAME/StockSentinel.git
   cd StockSentinel
   ```
3. **Add Upstream Remote**:
   ```bash
   git remote add upstream https://github.com/djrams810/StockSentinel.git
   ```

## Development Setup

### Prerequisites

- Git
- Python 3.8+ (for validation scripts)
- PyYAML library: `pip install pyyaml`
- A GitHub account
- Basic understanding of GitHub Apps

### Initial Setup

1. **Create a Branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Install Dependencies** (if implementing webhook server):
   ```bash
   # For Python
   pip install -r requirements.txt
   
   # For Node.js
   npm install
   ```

3. **Configure Environment**:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## Making Changes

### File Organization

- `.github/` - GitHub App manifest and workflows
- `scripts/` - Validation and utility scripts
- `examples/` - Example configurations
- `docs/` - Additional documentation

### Coding Guidelines

1. **App Manifest** (`.github/app.yml`):
   - Follow YAML syntax
   - Add comments for complex configurations
   - Test with validation script before committing

2. **Documentation**:
   - Keep README.md up to date
   - Add examples for new features
   - Use clear, concise language

3. **Scripts**:
   - Include docstrings for functions
   - Add error handling
   - Make scripts executable with proper shebang

### Commit Messages

Use clear, descriptive commit messages:

```
feat: add support for custom alert thresholds
fix: correct webhook signature validation
docs: update installation guide with troubleshooting
test: add validation for stock configuration
```

Prefixes:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `test`: Adding or updating tests
- `refactor`: Code refactoring
- `chore`: Maintenance tasks

## Testing

### Validation

Before committing, run the validation script:

```bash
python3 scripts/validate.py
```

This checks:
- GitHub App manifest syntax
- Example configuration files
- .gitignore completeness

### Manual Testing

1. **Test App Manifest**:
   - Create a test GitHub App using the manifest
   - Verify all permissions are granted
   - Check webhook events are subscribed

2. **Test Configurations**:
   - Validate JSON/YAML syntax
   - Test with real stock symbols
   - Verify alert thresholds work correctly

## Submitting Changes

### Pull Request Process

1. **Update Your Fork**:
   ```bash
   git fetch upstream
   git rebase upstream/main
   ```

2. **Run Validation**:
   ```bash
   python3 scripts/validate.py
   ```

3. **Push Changes**:
   ```bash
   git push origin feature/your-feature-name
   ```

4. **Create Pull Request**:
   - Go to your fork on GitHub
   - Click "New Pull Request"
   - Provide a clear description of changes
   - Reference any related issues

### Pull Request Guidelines

- **Title**: Clear and descriptive
- **Description**: Explain what and why
- **Testing**: Describe testing performed
- **Screenshots**: Include for UI changes
- **Breaking Changes**: Clearly document

### Review Process

1. Maintainers will review your PR
2. Address feedback and comments
3. Make requested changes
4. Once approved, PR will be merged

## GitHub App Development

### Permissions

When adding new features that require permissions:

1. Update `.github/app.yml` with new permissions
2. Document why the permission is needed
3. Test with minimal permissions first
4. Update INSTALLATION.md with permission details

### Webhook Events

When adding new webhook event handlers:

1. Add event to `default_events` in app.yml
2. Document the event handler behavior
3. Test event delivery and processing
4. Add error handling for webhook failures

### Security Considerations

- Never commit private keys or secrets
- Use environment variables for sensitive data
- Validate all input from webhooks
- Follow GitHub's security best practices
- Test permission scopes thoroughly

### Testing GitHub Apps

1. **Create Test App**:
   - Use manifest to create a test app
   - Install on test repository
   - Test all event handlers

2. **Test Webhooks**:
   - Use GitHub's webhook testing tools
   - Verify signature validation
   - Test error handling

3. **Test Permissions**:
   - Verify read/write operations
   - Test permission boundaries
   - Check rate limiting

## Documentation

### What to Document

- New features and configurations
- API changes or additions
- Breaking changes
- Installation requirements
- Examples and use cases

### Documentation Style

- Use Markdown formatting
- Include code examples
- Add screenshots when helpful
- Keep language simple and clear
- Update table of contents

## Questions or Problems?

- **Issues**: Open an issue for bugs or feature requests
- **Discussions**: Use GitHub Discussions for questions
- **Security**: Email security issues privately to maintainers

## License

By contributing, you agree that your contributions will be licensed under the same license as the project.

---

Thank you for contributing to StockSentinel! 🚀
