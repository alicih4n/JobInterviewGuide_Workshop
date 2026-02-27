# 🧠📚 Job Interview Guide Workshop & LLM Simulation

**Course:** CSCN8010 - Applied AI & Machine Learning  
**Group 2 Members:** 
- Ali Cihan Ozdemir (9091405)
- Lohith Reddy Danda (9054470)

> **⚠️ Important Notice:** Group member Roshan did not attend the laboratory session and provided zero contribution to this project.

---

## 📖 Project Overview
This repository contains a comprehensive **Job Interview Guide Workshop** and an **LLM-simulated Technical Interview Session**. The project evaluates our theoretical and practical mastery of foundational Machine Learning concepts, including:
- Supervised vs. Unsupervised Learning paradigms.
- Feature Scaling and proper **Train/Validation/Test Splits**.
- Preventing insidious **Data Leakage** through strict Pipeline architectures.
- Parametric models (Linear & Logistic Regression) and their metrics (R², MSE, Cross-Entropy).
- Non-parametric models (K-Nearest Neighbors, Decision Trees) and Hyperparameter Tuning.

---

## 🗂️ Repository Structure
| File | Description |
| :--- | :--- |
| `JobInterviewLLMSession.ipynb` | A Markdown-based Jupyter Notebook simulating a robust 15-question technical interview with an LLM. Includes behavioral assessments, evaluation metrics, and study gap identifications. |
| `JobInterviewGuide_Workshop.ipynb` | The core workshop notebook containing targeted python code implementations. Features leak-proof cross-validation pipelines, visually rich linear residual analysis via `seaborn`, and KNN hyperparameter sweeps. |
| `requirements.txt` | Explicit Python dependency map for stable execution. |
| `Submission_Text.md` | Executive summary for direct submission routing. |

---

## 🚀 Getting Started

Follow these step-by-step instructions to set up the environment and run the notebooks on your local machine.

### 1️⃣ Prerequisites
Ensure you have the following installed:
- [Python 3.8+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/downloads)

### 2️⃣ Clone the Repository
Open your terminal (or Command Prompt) and clone this repository:
```bash
git clone https://github.com/alicih4n/JobInterviewGuide_Workshop.git
cd JobInterviewGuide_Workshop
```

### 3️⃣ Create a Virtual Environment
It is highly recommended to use a virtual environment to isolate the project's dependencies from your global Python environment.

**On macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```cmd
python -m venv venv
venv\Scripts\activate
```

### 4️⃣ Install Dependencies
With your virtual environment active, install the required libraries:
```bash
pip install --upgrade pip
pip install -r requirements.txt
pip install jupyter  # Installs the Jupyter Notebook server
```

### 5️⃣ Run the Notebooks
Launch the Jupyter instance:
```bash
jupyter notebook
```
This will open a new tab in your default web browser. From there, you can navigate to and open:
- `JobInterviewGuide_Workshop.ipynb` (To execute and review the ML code and visualizations)
- `JobInterviewLLMSession.ipynb` (To read the transcript of the simulated technical assessment)

---

## 📊 Visualizations
The code within the heavily commented `JobInterviewGuide_Workshop.ipynb` employs `seaborn` and `matplotlib` to dynamically generate highly readable graphics, including:
- **Residual tracking arrays** for Linear estimators.
- **Accuracy distribution graphs** matching cross-validated KNN states.
- **Pruned Decision logic trees** preventing node variance collapse.
