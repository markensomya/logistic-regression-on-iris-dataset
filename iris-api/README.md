# 🌸 Iris Flower Classification

A machine learning web app that predicts the species of an Iris flower based on its measurements, built with **Logistic Regression**, **FastAPI**, and a simple **HTML frontend**.

## Demo

Enter sepal and petal measurements → get the predicted species (Setosa, Versicolor, or Virginica).

## Project Structure

```
iris-api/
├── main.py            # FastAPI backend
├── model.pkl          # Trained logistic regression model
├── requirements.txt   # Python dependencies
└── static/
    └── index.html     # Frontend UI
```

## Tech Stack

- Python
- Scikit-learn (Logistic Regression)
- FastAPI
- Uvicorn
- HTML / CSS / JavaScript

## Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/your-username/iris-flower-classification.git
cd iris-flower-classification
```

**2. Create and activate virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Run the server**
```bash
uvicorn main:app --reload
```

**5. Open in browser**
```
http://127.0.0.1:8000
```

## API Endpoint

`POST /predict`

Request body:
```json
{
  "sepal_length": 5.1,
  "sepal_width": 3.5,
  "petal_length": 1.4,
  "petal_width": 0.2
}
```

Response:
```json
{
  "prediction": "setosa"
}
```

## Model

Trained on the classic [Iris dataset](https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html) using Logistic Regression from scikit-learn with an 75/25 train-test split.
