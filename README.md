# 🔴 CrimsonTrace

> **AI-Powered Fraud Detection System for Financial Networks**

CrimsonTrace is an intelligent fraud detection platform that combines graph analytics, machine learning, and behavioral pattern recognition to identify suspicious activities and fraud rings in financial transaction networks.

---

## 🎯 Overview

Financial fraud is evolving rapidly, with sophisticated networks using layering, cycling, and shell accounts to hide illicit activities. CrimsonTrace tackles this challenge head-on by:

- **Building transaction graphs** from raw CSV data
- **Detecting complex fraud patterns** like cycles, fan-in/out, and layered shells
- **Scoring accounts** using Graph Neural Networks (GNN) and rule-based algorithms
- **Identifying fraud rings** and their interconnected members
- **Flagging rapid money movement** and velocity-based anomalies

---

## ✨ Key Features

### 🕸️ Graph-Based Analysis
Transforms transaction data into directed graphs to reveal hidden relationships and money flow patterns.

### 🧠 GNN-Powered Scoring
Leverages Graph Convolutional Networks to compute suspicion scores based on network topology and node features.

### 🔍 Multi-Pattern Detection
- **Cycle Detection**: Identifies circular money flows (A → B → C → A)
- **Fan-In/Fan-Out**: Detects accounts receiving from or sending to many counterparties
- **Layered Shells**: Finds intermediate accounts used for money laundering
- **Velocity Flags**: Catches rapid receive-then-send patterns

### 📊 Comprehensive Reporting
Returns detailed JSON responses with:
- Suspicious accounts ranked by risk score
- Fraud ring memberships and patterns
- Processing time and summary statistics

---

## 🏗️ Architecture

```
crimsonTrace-backend/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── routes/
│   │   └── analyze.py          # /analyze endpoint
│   ├── services/
│   │   ├── graph_builder.py    # CSV → NetworkX graph
│   │   ├── detector.py         # Pattern detection algorithms
│   │   ├── gnn_engine.py       # Graph Neural Network inference
│   │   ├── scorer.py           # Suspicion scoring logic
│   │   └── analyzer.py         # Main analysis orchestration
│   ├── models/
│   │   └── schemas.py          # Pydantic response models
│   └── utils/
│       └── helpers.py          # Utility functions
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment config
└── .gitignore                  # Git ignore rules
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/bhoomika1705126/crimson_trace.git
   cd crimson_trace
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**
   ```bash
   uvicorn app.main:app --reload
   ```

4. **Access the API**
   - API: `http://localhost:8000`
   - Docs: `http://localhost:8000/docs`

---

## 📡 API Usage

### Endpoint: `POST /api/analyze`

Upload a CSV file with transaction data to analyze fraud patterns.

**Request:**
```bash
curl -X POST "http://localhost:8000/api/analyze" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@transactions.csv"
```

**CSV Format:**
```csv
transaction_id,sender_id,receiver_id,amount,timestamp
TX001,ACC001,ACC002,1000.00,2024-01-15 10:30:00
TX002,ACC002,ACC003,950.00,2024-01-15 11:00:00
```

**Response:**
```json
{
  "suspicious_accounts": [
    {
      "account_id": "ACC001",
      "suspicion_score": 85.5,
      "detected_patterns": ["cycle_length_3", "fan_out"],
      "ring_id": "RING_001"
    }
  ],
  "fraud_rings": [
    {
      "ring_id": "RING_001",
      "member_accounts": ["ACC001", "ACC002", "ACC003"],
      "pattern_type": "cycle_length_3",
      "risk_score": 82.3
    }
  ],
  "summary": {
    "total_accounts_analyzed": 150,
    "suspicious_accounts_flagged": 12,
    "fraud_rings_detected": 3,
    "processing_time_seconds": 2.45
  }
}
```

---

## 🧪 Detection Algorithms

### 1. **Cycle Detection**
Identifies circular transaction patterns where money flows back to the originating account through intermediaries.

### 2. **Fan-In/Fan-Out**
Flags accounts that interact with an unusually high number of distinct counterparties within a short time window (72 hours).

### 3. **Layered Shell Detection**
Discovers chains of low-activity intermediate accounts used to obscure the origin or destination of funds.

### 4. **Multi-Hop Exposure**
Finds accounts within 2 hops of known suspicious accounts, expanding the investigation radius.

### 5. **Velocity Analysis**
Detects rapid money movement where an account receives funds and immediately sends them out (within 10 minutes).

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | FastAPI |
| **Graph Processing** | NetworkX |
| **Machine Learning** | PyTorch, PyTorch Geometric |
| **Data Processing** | Pandas |
| **Deployment** | Render |

---

## 🌐 Deployment

### Deploy to Render

1. Push your code to GitHub
2. Connect your repo to [Render](https://render.com)
3. Render will auto-detect `render.yaml` and deploy
4. Your API will be live at `https://your-app.onrender.com`

---

## 🤝 Contributing

We welcome contributions! Whether it's bug fixes, new detection algorithms, or performance improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👥 Team

Built with ❤️ by the CrimsonTrace team for hackathon submission.

---


**⚡ CrimsonTrace - Detecting fraud before it spreads.**
