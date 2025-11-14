# Gemini TTS API Setup and Pricing

This reference covers how to obtain and configure your Gemini API key for TTS usage, and details about pricing for Gemini Text-to-Speech.

**Official Documentation**: 
- [Gemini API Keys](https://ai.google.dev/gemini-api/docs/api-key)
- [Gemini API Pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Cloud Text-to-Speech Pricing](https://cloud.google.com/text-to-speech/pricing)

## Obtaining an API Key

### Step 1: Access Google AI Studio

1. Navigate to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google Account credentials

### Step 2: Create API Key

1. Click on the "Get API Key" button (usually at the top-right corner)
2. Review and accept the terms of service
3. Choose to create the API key in an existing Google Cloud project or create a new one
4. Once generated, copy your API key immediately
5. **Important**: Store your API key securely - you won't be able to view it again after closing the dialog

### Step 3: Store API Key Securely

**Never commit API keys to version control!** Use one of these secure storage methods:

#### Option 1: macOS Keychain (Recommended for this project)

Store your API key in macOS Keychain using the `security` command:

```bash
security add-generic-password \
  -a "production" \
  -s "GEMINI_API_KEY" \
  -w "your_api_key_here"
```

Retrieve it when needed:

```bash
export GEMINI_API_KEY=$(security find-generic-password -a "production" -s "GEMINI_API_KEY" -w)
```

#### Option 2: Environment Variables (Development)

**macOS/Linux (Bash):**
```bash
# Add to ~/.bashrc
export GEMINI_API_KEY="your_api_key_here"

# Apply changes
source ~/.bashrc
```

**macOS (Zsh):**
```bash
# Add to ~/.zshrc
export GEMINI_API_KEY="your_api_key_here"

# Apply changes
source ~/.zshrc
```

**Windows:**
1. Search for "Environment Variables" in Windows search
2. Click "Edit the system environment variables"
3. In System Properties, click "Environment Variables"
4. Under "User variables," click "New"
5. Variable name: `GEMINI_API_KEY`
6. Variable value: Your API key
7. Click "OK" to save

#### Option 3: Google Cloud Authentication (For Cloud TTS Client)

If using the Cloud Text-to-Speech client library instead of GenAI SDK:

```bash
gcloud auth application-default login
```

This uses Google Cloud application default credentials instead of an API key.

## Verifying API Key Setup

Test that your API key is properly configured:

```bash
# Check if environment variable is set
echo $GEMINI_API_KEY

# Test with a simple API call (GenAI SDK)
# See go-examples.md for test code
```

## API Key Security Best Practices

1. **Never share API keys publicly**
   - Don't commit keys to Git repositories
   - Don't include keys in screenshots or documentation
   - Don't share keys via email or chat

2. **Use API key restrictions** (if available)
   - Restrict keys to specific IP addresses when possible
   - Limit keys to specific applications or referrers
   - Use separate keys for development and production

3. **Rotate keys regularly**
   - Generate new keys periodically
   - Revoke old keys when no longer needed
   - Update keys in your secure storage locations

4. **Monitor usage**
   - Regularly check API usage in Google Cloud Console
   - Set up alerts for unusual activity
   - Review billing statements

## Pricing for Gemini TTS

### Token-Based Pricing (Gemini API)

Gemini TTS uses token-based pricing when accessed through the Gemini API:

**Text Input Pricing:**
- **Standard Mode**: $0.10 per 1 million tokens (text/image/video input)
- **Batch Mode**: $0.05 per 1 million tokens (text/image/video input)

**Audio Output Pricing:**
- **Standard Mode**: Pricing varies - check current documentation
- **Batch Mode**: Typically lower cost per request

**Note:** Token consumption depends on the length of input text. Check current pricing page for exact rates.

### Cloud Text-to-Speech API Pricing

When using the Cloud Text-to-Speech API directly (separate from Gemini API):

#### Standard (Neural2) Voices
- **First 0 to 4 million characters**: $0.000016 per character (~$16 per 1M characters)
- **Next 4 to 40 million characters**: $0.000013 per character (~$13 per 1M characters)
- **Over 40 million characters**: $0.000011 per character (~$11 per 1M characters)

#### Premium (Wavenet/Studio) Voices
- **First 0 to 4 million characters**: $0.000016 per character (~$16 per 1M characters)
- **Next 4 to 40 million characters**: $0.000013 per character (~$13 per 1M characters)
- **Over 40 million characters**: $0.000011 per character (~$11 per 1M characters)

#### Gemini TTS Voices
Pricing may vary - check current [Cloud Text-to-Speech pricing page](https://cloud.google.com/text-to-speech/pricing) for latest rates.

### Cost Calculation Examples

**Example 1: Generate 1000 characters of speech**
- Characters: 1,000
- Cost (Standard tier): 1,000 × $0.000016 = **$0.016** (1.6 cents)

**Example 2: Generate 100,000 characters of speech**
- Characters: 100,000
- Cost (Standard tier): 100,000 × $0.000016 = **$1.60**

**Example 3: Generate 1 million characters of speech**
- Characters: 1,000,000
- Cost (Standard tier): 1,000,000 × $0.000016 = **$16.00**

**Example 4: Generate 5 million characters (volume discount)**
- First 4M: 4,000,000 × $0.000016 = $64.00
- Next 1M: 1,000,000 × $0.000013 = $13.00
- **Total: $77.00**

### Free Tier and Usage Limits

Google provides a free tier for Text-to-Speech with usage limits. Check the current free tier limits in the [official pricing documentation](https://cloud.google.com/text-to-speech/pricing).

**Important:** Free tier limits may:
- Have monthly character limits (typically first X million characters free)
- Apply to specific voice types
- Change over time - always check current documentation

### Factors Affecting Cost

1. **Text Length**: Longer text = more characters = higher cost
2. **Voice Type**: Standard vs Premium vs Gemini TTS may have different rates
3. **API Choice**: Gemini API vs Cloud TTS API may have different pricing models
4. **Volume Discounts**: Higher usage typically receives tiered pricing discounts

### Cost Optimization Tips

1. **Cache Results**: Store generated audio files to avoid regenerating identical content
2. **Batch Requests**: If processing multiple texts, batch requests where supported
3. **Choose Appropriate Voice**: Standard voices may cost less than premium options
4. **Monitor Usage**: Set up usage alerts in Google Cloud Console
5. **Optimize Text Length**: Break long texts appropriately, avoid unnecessary characters

## Billing and Usage Monitoring

### View Usage in Google Cloud Console

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Navigate to "APIs & Services" > "Dashboard"
3. Select your project
4. View API usage metrics and billing

### Set Up Billing Alerts

1. Go to "Billing" in Google Cloud Console
2. Navigate to "Budgets & alerts"
3. Create a budget with alerts
4. Set thresholds for spending notifications

### API Quotas and Rate Limits

Check current rate limits and quotas:
- Navigate to "APIs & Services" > "Quotas"
- View per-minute, per-day, and per-project limits
- Request quota increases if needed

## Character Count Guidelines

When estimating costs, remember:
- Spaces count as characters
- Punctuation counts as characters
- SSML tags count as characters
- Multi-byte characters (e.g., Chinese, Japanese) count per character

## References

- [Gemini API - API Keys Documentation](https://ai.google.dev/gemini-api/docs/api-key)
- [Gemini API - Pricing Documentation](https://ai.google.dev/gemini-api/docs/pricing)
- [Cloud Text-to-Speech Pricing](https://cloud.google.com/text-to-speech/pricing)
- [Google AI Studio](https://aistudio.google.com/)
- [Google Cloud Console](https://console.cloud.google.com/)

## Quick Reference

**API Key Setup:**
```bash
# Store in macOS Keychain
security add-generic-password -a "production" -s "GEMINI_API_KEY" -w "your_key"

# Retrieve
export GEMINI_API_KEY=$(security find-generic-password -a "production" -s "GEMINI_API_KEY" -w)
```

**Pricing (Cloud TTS - Standard tier):**
- **Per Character**: ~$0.000016 (first 4M characters)
- **Per 1M Characters**: ~$16
- **Volume Discounts**: Available for higher usage

**Useful Links:**
- [Get API Key](https://aistudio.google.com/app/apikey)
- [View Pricing](https://cloud.google.com/text-to-speech/pricing)
- [Monitor Usage](https://console.cloud.google.com/)

