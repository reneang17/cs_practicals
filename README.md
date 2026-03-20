# CS Practicals 🚀

Welcome to the `cs_practicals` repository! This project serves as a comprehensive collection of fundamental computer science exercises, small logic games, and data science implementations. 

The repository is divided into two main language tracks, each containing specialized projects designed to help practice and demonstrate core software engineering skills—from machine learning basics to advanced frontend / backend concepts.

---

## 📁 Repository Structure

### 🐍 [Python Practicals](./python/)
The Python directory contains a variety of data science, machine learning, and logic-based game implementations.
- **Data Science & ML:** K-Means Clustering, Linear Regression, Logistic Regression, Neural Networks.
- **Games & Algorithms:** Blackjack, Connect 4, Hangman, Minesweeper, Spell Checker (Tries), Sudoku, Tic-Tac-Toe.
- 👉 *[View Python README for setup and details](./python/README.md)*

### 🟨 [JavaScript Exercises](./javascript/)
The JavaScript directory focuses on core Vanilla JS and Node.js concepts frequently asked in junior and mid-level frontend interviews.
- **Async & APIs:** Async Fetch with Exponential Backoff Retries.
- **Performance:** Custom Debounce & Throttle implementations.
- **Patterns:** Event Emitter (Publish-Subscribe pattern).
- **DOM & UI:** Recursive Virtual DOM Builder.
- **Concurrency & Backend:** Async Task Queues and a Vanilla HTTP Server built from scratch.
- 👉 *[View JavaScript README for setup and details](./javascript/README.md)*

---

## 🛠 General Setup

Each major directory has its own isolated environment requirements.

**For Python:**
```bash
cd python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -e .
```

**For JavaScript:**
```bash
cd javascript/project_name
npm install
npm start
```

*See the individual READMEs inside each folder for deep-dive instructions on running the code, tests, and demos!*
