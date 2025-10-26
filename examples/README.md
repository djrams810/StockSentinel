# StockSentinel Example Usage

This directory contains example files to help you get started with StockSentinel.

## Files

### stock-config.json

Example configuration file showing how to set up stock monitoring with:
- Stock symbols to track
- Alert thresholds (price and percentage changes)
- Notification settings
- Integration options

## Usage

1. **Copy the example configuration**:
   ```bash
   cp examples/stock-config.json .stocksentinel.json
   ```

2. **Edit the configuration**:
   - Update stock symbols to track
   - Set appropriate alert thresholds
   - Configure notification preferences

3. **Commit to your repository**:
   ```bash
   git add .stocksentinel.json
   git commit -m "Add stock monitoring configuration"
   git push
   ```

4. **The GitHub App will**:
   - Read the configuration from your repository
   - Start monitoring the specified stocks
   - Create issues when alerts are triggered
   - Generate pull requests with updated data

## Configuration Options

### Stock Object

Each stock in the `stocks` array can have:

- `symbol`: Stock ticker symbol (required)
- `name`: Company name (optional)
- `alerts`: Alert configuration object with:
  - `price_above`: Create alert when price goes above this value
  - `price_below`: Create alert when price goes below this value
  - `percent_change`: Create alert on percentage change threshold

### Alert Settings

Global alert settings:

- `create_issues`: Whether to create GitHub issues for alerts
- `send_notifications`: Enable/disable notifications
- `update_frequency`: How often to check for updates (hourly, daily, etc.)
- `market_hours_only`: Only track during market hours

### Integrations

- `github_app`: Enable GitHub App integration
- `webhook_url`: Optional webhook endpoint for external notifications
- `data_source`: Data source type (api, csv, manual)

## Best Practices

1. **Start Small**: Begin with a few stocks and expand gradually
2. **Set Realistic Thresholds**: Avoid setting thresholds that trigger too frequently
3. **Review Alerts**: Regularly review and adjust alert settings
4. **Use Labels**: Apply labels to issues for better organization
5. **Archive Old Data**: Periodically clean up old alert issues

## Advanced Configuration

For more advanced use cases, you can:

- Use multiple configuration files for different portfolios
- Integrate with external data sources
- Customize issue templates
- Set up automated workflows with GitHub Actions

## Support

If you have questions about configuration:

1. Check the main README.md
2. Review INSTALLATION.md for setup help
3. Open an issue for specific questions
