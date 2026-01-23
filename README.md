# Namastox Workflow E2E Tester

This script automates the End-to-End (E2E) testing of workflows within the **Namastox** platform. It simulates a real user by logging in, creating a new study (RA), and automatically processing tasks and decisions for a workflow selected by you.

## 📋 Prerequisites

Ensure you have **Python 3.x** installed. You will need to install the required libraries:

```bash
pip install pytest playwright python-dotenv
```

## ⚙️ Configuration (Recommended)

To avoid entering your credentials manually every time you run the test, create a file named .env in the root directory of the project with the following content:

```bash
NAMASTOX_USER=your_username
NAMASTOX_PASSWORD=your_password
```
## How to Run the Test
```bash
pytest -s
```

