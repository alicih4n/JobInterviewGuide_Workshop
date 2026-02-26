import json

# --- Update JobInterviewLLMSession.ipynb ---
file1 = '/Users/alicihanozdemir/Documents/AllCodingProjects/CSCN8010/JobInterviewGuide_Workshop/JobInterviewGuide_Workshop/JobInterviewLLMSession.ipynb'
with open(file1, 'r') as f:
    nb1 = json.load(f)

header_cell = {
    "cell_type": "markdown",
    "id": "header_01",
    "metadata": {},
    "source": [
        "# Job Interview Guide Workshop - Simulated Session\n",
        "**Group 2 Members:**\n",
        "- Ali Cihan Ozdemir (9091405)\n",
        "- Lohith Reddy Danda (9054470)\n",
        "- Note: Group member Roshan did not participate in this session.\n"
    ]
}

# Insert header at top
nb1['cells'].insert(0, header_cell)

# Simplify Q5 (Cell 16 now, previously 15)
for cell in nb1['cells']:
    if "Question 5:" in "".join(cell.get('source', [])):
        cell['source'] = [
            "## LLM\n",
            "Correct.\n",
            "\n",
            "**Question 5:** You want to scale your data so that all features have a mean of 0 and a standard deviation of 1. You apply `StandardScaler` to your entire dataset before splitting it into training and testing sets. Why is this a bad idea?\n",
            "A) It takes too long to compute on the full dataset.\n",
            "B) It causes an error because `train_test_split` expects unscaled data.\n",
            "C) It causes \"Data Leakage\" because information from the test set (its mean and variance) leaks into the training process.\n",
            "D) It changes the number of features in your dataset.\n",
            "E) Scaling is only needed for Deep Learning, not traditional ML.\n"
        ]
    if "Question 13:" in "".join(cell.get('source', [])):
        cell['source'] = [
            "## LLM\n",
            "Correct.\n",
            "\n",
            "**Question 13:** In the K-Nearest Neighbors (KNN) algorithm, how does the model decide which points are the \"nearest\" neighbors?\n",
            "A) It uses a decision tree to split the data.\n",
            "B) It randomly picks $k$ points from the training set.\n",
            "C) It calculates the correlation coefficient between features.\n",
            "D) It calculates a distance metric, most commonly the Euclidean distance (straight-line distance) between data points.\n",
            "E) It fits a line of best fit and checks the residuals.\n"
        ]

with open(file1, 'w') as f:
    json.dump(nb1, f, indent=1)

# --- Update JobInterviewGuide_Workshop.ipynb ---
file2 = '/Users/alicihanozdemir/Documents/AllCodingProjects/CSCN8010/JobInterviewGuide_Workshop/JobInterviewGuide_Workshop/JobInterviewGuide_Workshop.ipynb'
with open(file2, 'r') as f:
    nb2 = json.load(f)

nb2['cells'].insert(0, header_cell)

with open(file2, 'w') as f:
    json.dump(nb2, f, indent=1)
