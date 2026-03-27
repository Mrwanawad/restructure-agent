# 🧠 Data Extraction Chatbot — Restructuring Agent

> Paste any messy, unstructured text and get back a clean, structured Python dictionary — powered by **Groq**.

🔗 **Live Demo:** [restructuring-agent.streamlit.app](https://restructuring-agent.streamlit.app/)

---

## 📌 Overview

The **Data Extraction Chatbot** is an AI-powered Streamlit app that transforms unstructured text — receipts, clinical notes, transcriptions, handwritten records, or any raw dump of information — into clean, structured Python dictionaries.

Under the hood, it uses **Groq** as the reasoning engine to intelligently detect fields, normalize values, and handle missing or ambiguous data — no predefined schema required.

---

## ✨ Features

- **Returns only structured data** — no noise, no filler, just clean key-value output
- **Automatically detects fields** — dates, names, amounts, items, totals, and more
- **Handles missing or uncertain values** — fills with `NULL` where data is absent
- **Normalizes numbers and formats** — consistent types and output formatting
- **Works on any domain** — medical notes, invoices, conversation logs, and beyond

---

## 🖥️ Demo

**Input** — raw unstructured text:
```
copay collected: $30.00
remaining balance: NULL
dr signature: S. Mitchell MD
notes: pt advised to reduce stress + increase water intake
```

**Output** — clean Python dictionary:
```json
{
  "provider": "Dr. Sarah Mitchell",
  "facility": "Family Clinic",
  "patient_name": "John B. Harrington",
  "dob": "1982-04-11",
  "visit_date": "2025-03-03",
  "chief_complaint": "back pain, headaches (ongoing ~3 weeks)",
  "vitals": {
    "weight_lbs": 187,
    "height": "5'11",
    "blood_pressure": "128/84",
    "pulse_bpm": 72,
    "temperature_f": 98.9
  },
  "medications": [
    {
      "name": "lisinopril",
      "dose_mg": 10
    }
  ],
  "copay_usd": 30.00,
  "remaining_balance": null,
  "notes": "pt advised to reduce stress and increase water intake"
}
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- A [Groq API key](https://console.groq.com/)

### Installation

```bash
# Clone the repository
git clone https://github.com/Mrwanawad/restructuring-agent.git
cd restructuring-agent

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory and add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Or, if deploying on Streamlit Cloud, add it via **Settings → Secrets**:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### Run Locally

```bash
streamlit run app.py
```

Then open your browser at `http://localhost:8501`.

---

## 🧱 Project Structure

```
restructuring-agent/
│
├── app.py                  # Main Streamlit application
├── agent.py                # Groq-powered extraction logic
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables
└── README.md
```

---

## 🔧 How It Works

1. **User pastes** any unstructured text into the input field
2. The text is sent to **Groq's LLM** via the Groq API
3. A structured prompt instructs the model to detect and extract all relevant fields
4. The model returns a clean **JSON/Python dictionary**
5. The result is displayed in a formatted **Output Dialog**

Groq's ultra-fast inference makes this feel near-instant even on large text blocks.

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI framework |
| `groq` | LLM API client (the reasoning brain) |
| `python-dotenv` | Environment variable management |

Install all with:

```bash
pip install -r requirements.txt
```

---

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**.

To deploy your own instance:

1. Fork this repository
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Connect your GitHub repo
4. Add your `GROQ_API_KEY` under **App Settings → Secrets**
5. Click **Deploy**

---

## 🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 👤 Author

Built with ❤️ using [Groq](https://groq.com/) + [Streamlit](https://streamlit.io/)
