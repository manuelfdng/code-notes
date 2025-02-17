// sanity-check.js
const codespaceName = process.env.CODESPACE_NAME;
const flaskPort = process.env.FLASK_PORT || "5000";

if (!codespaceName) {
  console.error("❌ ERROR: CODESPACE_NAME is not set. Make sure you're running this inside GitHub Codespaces.");
  process.exit(1);
}

const targetUrl = `https://${codespaceName}-${flaskPort}.app.github.dev`;

console.log("✅ Sanity check passed!");
console.log(`CODESPACE_NAME: ${codespaceName}`);
console.log(`Flask API Target URL: ${targetUrl}`);