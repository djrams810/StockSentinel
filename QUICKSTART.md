# StockSentinel Quick Start Guide

Get started with StockSentinel in 5 minutes! This guide will help you install and configure the GitHub App for stock monitoring.

## 🚀 Quick Installation

### Step 1: Create the GitHub App

1. Visit: https://github.com/settings/apps/new
2. Click **"Create GitHub App from manifest"**
3. Copy and paste the contents from [.github/app.yml](.github/app.yml)
4. Click **"Create"**

### Step 2: Install the App

1. After creation, click **"Install App"**
2. Select your account or organization
3. Choose repositories to monitor
4. Click **"Install"**

### Step 3: Configure Stock Tracking

1. Copy the example configuration:
   ```bash
   cp examples/stock-config.json .stocksentinel.json
   ```

2. Edit `.stocksentinel.json` with your stock symbols:
   ```json
   {
     "stocks": [
       {
         "symbol": "AAPL",
         "name": "Apple Inc.",
         "alerts": {
           "price_above": 200,
           "price_below": 150,
           "percent_change": 5
         }
       }
     ]
   }
   ```

3. Commit and push:
   ```bash
   git add .stocksentinel.json
   git commit -m "Configure stock tracking"
   git push
   ```

## 📊 What Happens Next?

Once configured, StockSentinel will:

- ✓ Monitor your specified stocks
- ✓ Create issues when price thresholds are reached
- ✓ Generate pull requests with updated data
- ✓ Send notifications (if configured)

## 🔧 Configuration Options

### Environment Variables

Create a `.env` file (use `.env.example` as template):

```bash
# Copy example
cp .env.example .env

# Edit with your values
GITHUB_APP_ID=your_app_id
STOCK_SYMBOLS=AAPL,GOOGL,MSFT
```

### Stock Alert Settings

In your `.stocksentinel.json`:

- **price_above**: Alert when price exceeds this value
- **price_below**: Alert when price falls below this value
- **percent_change**: Alert on percentage change threshold

## 📝 Example Use Cases

### Monitor Tech Stocks

```json
{
  "stocks": [
    {"symbol": "AAPL", "alerts": {"percent_change": 5}},
    {"symbol": "GOOGL", "alerts": {"percent_change": 5}},
    {"symbol": "MSFT", "alerts": {"percent_change": 5}}
  ]
}
```

### Price Threshold Alerts

```json
{
  "stocks": [
    {
      "symbol": "TSLA",
      "alerts": {
        "price_above": 300,
        "price_below": 200
      }
    }
  ]
}
```

### Market Hours Only

```json
{
  "alert_settings": {
    "market_hours_only": true,
    "update_frequency": "hourly"
  }
}
```

## ✅ Verify Installation

1. **Check App Installation**:
   - Go to repository Settings → Integrations
   - Verify StockSentinel is listed

2. **Test Configuration**:
   ```bash
   python3 scripts/validate.py
   ```

3. **Check Permissions**:
   - App should have read/write access to issues and PRs
   - Verify webhook events are subscribed

## 🆘 Troubleshooting

### App Not Found

**Problem**: App doesn't appear in repository settings

**Solution**:
- Ensure app is installed on the correct account
- Check repository is included in installation
- Verify you have admin access

### No Alerts Generated

**Problem**: Stock price changes but no issues created

**Solution**:
- Verify `.stocksentinel.json` is in repository root
- Check alert thresholds are appropriate
- Review app permissions (needs write access to issues)

### Validation Errors

**Problem**: Configuration validation fails

**Solution**:
```bash
# Run validation to see errors
python3 scripts/validate.py

# Check JSON syntax
python3 -m json.tool .stocksentinel.json

# Check YAML syntax
python3 -c "import yaml; yaml.safe_load(open('.github/app.yml'))"
```

## 📚 Next Steps

- **Customize Alerts**: Adjust thresholds in `.stocksentinel.json`
- **Add More Stocks**: Expand your tracking list
- **Set Up Webhooks**: Configure external notifications
- **Review Documentation**: Read [INSTALLATION.md](INSTALLATION.md) for details

## 🤝 Getting Help

- **Issues**: Report bugs or request features
- **Discussions**: Ask questions in GitHub Discussions
- **Documentation**: Check [README.md](README.md) and [INSTALLATION.md](INSTALLATION.md)
- **Contributing**: See [CONTRIBUTING.md](CONTRIBUTING.md)

## 📖 Additional Resources

- [GitHub Apps Documentation](https://docs.github.com/apps)
- [Full Installation Guide](INSTALLATION.md)
- [Example Configurations](examples/)
- [Contributing Guidelines](CONTRIBUTING.md)

---

**Time to First Alert**: ~5 minutes after setup
**Difficulty**: Beginner friendly
**Requirements**: GitHub account with repository access

Happy monitoring! 📈
