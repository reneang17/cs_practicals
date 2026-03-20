# Python CS & Data Science Practicals

Welcome to the Python section of the project! This directory contains a variety of Python-based computer science exercises, small logic games, and fundamental data science and machine learning implementations.

## 🚀 Projects Included

### Data Science & Machine Learning
- **[K-Means Clustering](./kmeans/)** - Unsupervised learning algorithm implementation.
- **[Linear Regression](./linear_regression/)** - Basic regression techniques.
- **[Logistic Regression](./logistic_regression/)** - Classification methods.
- **[Neural Networks](./neural_networks/)** - Foundational deep learning concepts.

### Computer Science & Games
- **[Blackjack](./black_jack/)** - A simple card game implementation.
- **[Connect 4](./connet_4/)** - The classic grid-based connection game.
- **[Hangman](./hangman/)** - A word-guessing game (includes a local dictionary, `words.text`).
- **[Minesweeper](./minesweeper/)** - Grid-based logic game.
- **[Spell Checker](./spell_checker/)** - Algorithm to process and correct spelling using data structures like Tries.
- **[Sudoku](./sudoku/)** - Sudoku solver and generator (includes board graphics and text boards).
- **[Tic-Tac-Toe](./tic-tac-toe/)** - Simple zero-sum game implementation.

---

## 🛠 Setup & Installation

To run the provided Jupyter notebooks and scripts, you'll want to install the necessary dependencies (`numpy`, `pandas`, `pytest`, `jupyter`).

1. **Ensure you have a virtual environment at the root (or create one here):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the requirements:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install the local library (for shared `Utils` and modules):**
   ```bash
   pip install -e .
   ```

4. **Launch Jupyter Notebook (if exploring the `.ipynb` files):**
   ```bash
   jupyter notebook
   ```

## 🧪 Running Tests

This directory includes tests for the core utilities and shared components. You can run them using `pytest` from this directory:

```bash
PYTHONPATH=. pytest
```
