# GitHub App Installation Guide

This guide provides detailed instructions for installing the StockSentinel GitHub App.

## Prerequisites

- A GitHub account (personal or organization)
- Repository admin access where you want to install the app
- Basic understanding of GitHub Apps and webhooks

## Installation Methods

### Method 1: Using GitHub App Manifest (Recommended)

GitHub App manifests allow you to create a pre-configured app with a single click.

1. **Navigate to GitHub Apps Creation Page**:
   ```
   https://github.com/settings/apps/new
   ```
   
   Or for organizations:
   ```
   https://github.com/organizations/YOUR-ORG/settings/apps/new
   ```

2. **Register from Manifest**:
   - Look for the "From manifest" option
   - Copy the entire contents of `.github/app.yml` from this repository
   - Paste it into the manifest field
   - Click "Create GitHub App from manifest"

3. **Complete Registration**:
   - GitHub will parse the manifest and create the app
   - You'll be redirected to the app settings page
   - Note your App ID and generate a private key for authentication

### Method 2: Manual Configuration

If you prefer to configure the app manually:

1. **Create New GitHub App**:
   - Go to Settings → Developer settings → GitHub Apps → New GitHub App

2. **Basic Information**:
   - **App name**: StockSentinel (or your preferred name)
   - **Description**: A GitHub App for monitoring and analyzing stock market data
   - **Homepage URL**: https://github.com/djrams810/StockSentinel
   - **Webhook URL**: (Optional) Your webhook endpoint URL
   - **Webhook secret**: (Optional) A secure random string

3. **Permissions**:
   Configure the following repository permissions:
   - **Contents**: Read
   - **Issues**: Read & Write
   - **Pull requests**: Read & Write
   - **Metadata**: Read

4. **Subscribe to Events**:
   - Issues
   - Pull request
   - Push
   - Repository

5. **Create the App**:
   - Click "Create GitHub App"
   - Generate and download a private key

## Post-Installation Setup

### 1. Install App on Repositories

After creating the app:

1. Navigate to your GitHub App settings
2. Click "Install App" in the left sidebar
3. Select your account or organization
4. Choose repositories:
   - All repositories, or
   - Only select repositories
5. Click "Install"

### 2. Generate Authentication Credentials

For programmatic access:

1. In your app settings, scroll to "Private keys"
2. Click "Generate a private key"
3. Download and securely store the `.pem` file
4. Note your App ID from the app settings

### 3. Configure Webhook (Optional)

If you're using webhooks:

1. Set up a webhook endpoint (server) to receive events
2. Update the webhook URL in app settings
3. Set a webhook secret for security
4. Verify webhook deliveries in the app settings

## Verification

To verify successful installation:

1. **Check Installations**:
   - Go to your repository settings
   - Navigate to "Integrations" → "GitHub Apps"
   - Verify StockSentinel is listed

2. **Test Permissions**:
   - Try creating an issue in the repository
   - Verify the app can read repository contents
   - Check webhook deliveries (if configured)

## Updating Permissions

To update app permissions after installation:

1. Modify `.github/app.yml` with new permissions
2. Update app settings manually in GitHub
3. Users will need to accept the new permissions

## Troubleshooting

### App Not Appearing in Repository

- Verify the app is installed on the correct account/organization
- Check that the repository is included in the installation
- Ensure you have admin access to the repository

### Permission Denied Errors

- Review the app's current permissions in settings
- Ensure required permissions are granted
- Re-install the app if permissions were updated

### Webhook Not Receiving Events

- Verify webhook URL is accessible from GitHub servers
- Check webhook secret matches in your server configuration
- Review webhook delivery logs in app settings

## Security Best Practices

1. **Private Key Security**:
   - Never commit private keys to repositories
   - Store keys in secure environment variables
   - Rotate keys periodically

2. **Webhook Security**:
   - Always use HTTPS for webhook URLs
   - Validate webhook signatures
   - Use a strong webhook secret

3. **Permissions**:
   - Request only necessary permissions
   - Regularly audit app access
   - Remove unused installations

## Additional Resources

- [GitHub Apps Documentation](https://docs.github.com/apps)
- [GitHub Apps API Reference](https://docs.github.com/rest/apps)
- [Webhook Events and Payloads](https://docs.github.com/webhooks/event-payloads)
- [GitHub App Manifest Documentation](https://docs.github.com/apps/sharing-github-apps/registering-a-github-app-from-a-manifest)

## Support

For issues or questions about installation:

1. Check this guide first
2. Review GitHub's official documentation
3. Open an issue in this repository
4. Contact the repository maintainer

---

**Last Updated**: October 2025
**Version**: 1.0.0
