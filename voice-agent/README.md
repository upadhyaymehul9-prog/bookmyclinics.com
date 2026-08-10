# Voice Calling Agent

This service places outbound voice calls to customers and reads a product announcement script using Twilio.

## 1) Setup

1. Create a Twilio account and buy a voice-enabled phone number.
2. Copy `.env.example` to `.env`.
3. Fill in your Twilio credentials and default product message values.

```bash
cp .env.example .env
npm install
```

## 2) Run

```bash
npm start
```

Server starts at `http://localhost:3000`.

## 3) Check configuration

```bash
curl http://localhost:3000/health
```

## 4) Place a call

```bash
curl -X POST http://localhost:3000/call \
  -H "Content-Type: application/json" \
  -d '{
    "to": "+15550001111",
    "customerName": "Alex",
    "productName": "BookMyClinics",
    "companyName": "BookMyClinics Team",
    "productPitch": "We help people find and book trusted clinics in minutes."
  }'
```

## Request body fields

- `to` (required): customer phone number in E.164 format (example: `+15550001111`)
- `customerName` (optional): customer name used in greeting
- `productName` (optional): product name, fallback is `DEFAULT_PRODUCT_NAME`
- `companyName` (optional): caller/company name, fallback is `DEFAULT_COMPANY_NAME`
- `productPitch` (optional): custom product sentence, fallback is `DEFAULT_PRODUCT_PITCH`
- `from` (optional): override caller ID; defaults to `TWILIO_FROM_NUMBER`

## Notes

- Make sure Twilio voice calling is enabled on your account.
- If you use a trial Twilio account, the destination number must be verified first.
