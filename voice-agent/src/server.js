const express = require("express");
const dotenv = require("dotenv");
const twilio = require("twilio");

dotenv.config();

const app = express();
app.use(express.json());

const PORT = Number(process.env.PORT || 3000);
const REQUIRED_ENV_VARS = [
  "TWILIO_ACCOUNT_SID",
  "TWILIO_AUTH_TOKEN",
  "TWILIO_FROM_NUMBER",
];

function missingEnvVars() {
  return REQUIRED_ENV_VARS.filter((name) => !process.env[name]);
}

function buildVoiceMessage({
  customerName,
  productName,
  companyName,
  productPitch,
}) {
  const introName = customerName ? `Hello ${customerName}.` : "Hello.";

  return [
    introName,
    `This is an automated call from ${companyName}.`,
    `We want to let you know about ${productName}.`,
    productPitch,
    "If you are interested, please reply to our team and we will help you get started.",
    "Thank you for your time. Goodbye.",
  ].join(" ");
}

function buildTwimlMessage(message) {
  const response = new twilio.twiml.VoiceResponse();
  response.say(
    {
      voice: "alice",
      language: "en-US",
    },
    message
  );
  response.pause({ length: 1 });
  response.hangup();
  return response.toString();
}

app.get("/health", (_, res) => {
  const missing = missingEnvVars();

  res.status(200).json({
    ok: missing.length === 0,
    message:
      missing.length === 0
        ? "Voice calling agent is configured."
        : "Voice calling agent is missing required environment variables.",
    missingEnvVars: missing,
  });
});

app.post("/call", async (req, res) => {
  const missing = missingEnvVars();
  if (missing.length > 0) {
    return res.status(500).json({
      ok: false,
      error: "Missing required environment variables.",
      missingEnvVars: missing,
    });
  }

  const {
    to,
    customerName = "",
    productName = process.env.DEFAULT_PRODUCT_NAME || "our product",
    companyName = process.env.DEFAULT_COMPANY_NAME || "our team",
    productPitch =
      process.env.DEFAULT_PRODUCT_PITCH ||
      "It helps you solve everyday business needs quickly and efficiently.",
    from = process.env.TWILIO_FROM_NUMBER,
  } = req.body || {};

  if (!to) {
    return res.status(400).json({
      ok: false,
      error: "Missing required field: to",
    });
  }

  try {
    const client = twilio(
      process.env.TWILIO_ACCOUNT_SID,
      process.env.TWILIO_AUTH_TOKEN
    );

    const message = buildVoiceMessage({
      customerName,
      productName,
      companyName,
      productPitch,
    });

    const twiml = buildTwimlMessage(message);

    const call = await client.calls.create({
      from,
      to,
      twiml,
    });

    return res.status(201).json({
      ok: true,
      callSid: call.sid,
      status: call.status,
      to,
      from,
      message,
    });
  } catch (error) {
    return res.status(500).json({
      ok: false,
      error: "Failed to create outbound call.",
      details: error.message,
    });
  }
});

app.listen(PORT, () => {
  console.log(`Voice calling agent listening on port ${PORT}`);
});
