# 📈 AI Stock Research Platform

An AI-powered multi-agent stock research system that scans NIFTY stocks, identifies technical opportunities, performs AI-driven chart analysis, ranks candidates, and generates interactive dashboards for investment research.

---

## 🚀 Features

### Market Data Analysis
- Yahoo Finance Integration
- Historical OHLCV Data
- NIFTY Benchmark Comparison
- NIFTY 50 / NIFTY 500 Support

### Technical Indicators
- RSI
- SMA 20
- SMA 50
- SMA 200
- Volume Analysis
- Relative Strength (RS)
- ATR (Average True Range)

### Pattern Detection Engine
- Breakout Detection
- Support Detection
- Resistance Detection
- Pattern Scoring

### Risk Analysis
- ATR Based Risk Classification
- Low Risk Detection
- Medium Risk Detection
- High Risk Detection

### Ranking Engine
Stocks are ranked based on:

- Technical Score
- Relative Strength
- Trend Strength
- Volume Confirmation
- Risk Rating
- Breakout Confirmation

### AI Technical Analyst
Using Local LLMs through Ollama:

- Bull Flag Detection
- Double Bottom Detection
- Ascending Triangle Detection
- Breakout Identification
- Trend Analysis
- Confidence Scoring
- Natural Language Reasoning

### Reporting
- Excel Reports
- JSON Reports
- Elite Picks Report
- Breakout Report
- Interactive HTML Dashboard

---

# 🏗️ Architecture

```text
NIFTY 500
    ↓
Market Data Agent
    ↓
Indicator Agent
    ↓
Pattern Agent
    ↓
Scoring Agent
    ↓
Ranking Agent
    ↓
Top Candidates
    ↓
AI Technical Analyst
    ↓
Dashboard + Reports
```

---

# 📂 Project Structure

```text
StockPatternScanner/

├── agents/
│   ├── ai_technical_agent.py
│   ├── benchmark_agent.py
│   ├── dashboard_agent.py
│   ├── decision_agent.py
│   ├── indicator_agent.py
│   ├── market_data.py
│   ├── pattern_agent.py
│   ├── ranking_agent.py
│   └── scoring_agent.py
│
├── patterns/
│   ├── breakout.py
│   ├── double_bottom.py
│   └── bull_flag.py
│
├── utils/
│   ├── atr.py
│   ├── breakout_confirmation.py
│   ├── relative_strength.py
│   ├── risk.py
│   ├── support_resistance.py
│   ├── trend_strength.py
│   └── volume.py
│
├── templates/
│   └── dashboard.html
│
├── data/
│   ├── nifty50.csv
│   └── nifty500.csv
│
├── reports/
│   ├── excel/
│   ├── json/
│   └── html/
│
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>

cd StockPatternScanner
```

---

## 2. Create Virtual Environment

### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

### Linux / Mac

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🤖 Ollama Setup

The AI Technical Analyst requires a local LLM.

Install Ollama:

Official Site:

https://ollama.com

---

## Verify Installation

```bash
ollama --version
```

---

## Pull Recommended Model

### Option 1 (Recommended)

```bash
ollama pull qwen3:14b
```

### Option 2

```bash
ollama pull llama3.1:8b
```

---

## Start Ollama

```bash
ollama serve
```

Expected:

```text
Listening on 127.0.0.1:11434
```

---

# 📊 Configure Scan Universe

Edit:

```text
data/nifty50.csv
```

or

```text
data/nifty500.csv
```

Format:

```csv
symbol
RELIANCE.NS
TCS.NS
INFY.NS
SBIN.NS
```

---

# ▶️ Run Application

```bash
python app.py
```

---

# 📁 Generated Reports

## Excel

```text
reports/excel/

scan_20260617.xlsx

top20_20260617.xlsx

elite_20260617.xlsx
```

---

## JSON

```text
reports/json/

top20.json

ai_analysis.json

top_picks.json
```

---

## HTML Dashboard

```text
reports/html/

dashboard_20260617.html
```

Automatically opens in browser after scan completion.

---

# 📈 Dashboard Features

### Summary Cards

- Total Stocks
- Strong Buy
- Buy
- Elite Picks

### Top Ranked Stocks

Displays:

- Final Score
- Decision
- Relative Strength
- Risk Rating
- AI Pattern
- AI Confidence
- AI Trend

### Elite Picks

Displays:

- Confirmed Breakouts
- High Scoring Stocks
- AI Analysis

### AI Technical Analysis

Displays:

- Pattern Detected
- Trend
- Confidence
- AI Reasoning

---

# 🧠 AI Technical Analysis Example

```json
{
    "patterns": [
        "Bull Flag"
    ],
    "confidence": 80,
    "trend": "Bullish",
    "reasoning": "Price is forming higher lows beneath resistance while maintaining strong momentum."
}
```

---

# 📋 Scoring Framework

| Component | Weight |
|------------|---------|
| Technical Patterns | High |
| Relative Strength | Medium |
| Trend Strength | Medium |
| Volume Confirmation | Medium |
| Risk Rating | Medium |
| Breakout Confirmation | High |

---

# 📌 Elite Pick Criteria

A stock becomes an Elite Pick when:

```text
Breakout Confirmed == True

AND

Final Score >= 85
```

---

# 🛠️ Technologies Used

### Backend

- Python
- Pandas
- NumPy

### Market Data

- Yahoo Finance (yfinance)

### AI

- Ollama
- Qwen3 14B
- Llama 3.1

### Reporting

- OpenPyXL
- Jinja2

### Dashboard

- HTML
- CSS

---

# 🔮 Future Enhancements

## Phase 1

- Market Structure Agent
- Swing High/Low Detection
- AI Consensus Engine

## Phase 2

- Financial Analysis Agent
- News Sentiment Agent
- Risk Assessment Agent

## Phase 3

- AI Investment Committee
- Portfolio Construction Agent
- Automated Research Reports

---

# Example Output

```text
1. LT.NS         | 100 | STRONG BUY
2. SBIN.NS       | 100 | STRONG BUY
3. DIVISLAB.NS   | 100 | STRONG BUY
```

---


## Landing Page
![Landing Page](https://github.com/prathameshbhirud/ClauseAI/blob/main/images/landing_page.JPG)

# Disclaimer

This project is for educational and research purposes only.

It does not constitute financial advice, investment advice, or trading recommendations.

Always conduct your own research before investing.