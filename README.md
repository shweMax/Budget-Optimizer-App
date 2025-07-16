# 💰 Budget Optimizer App

[![Streamlit](https://img.shields.io/badge/Streamlit-App-orange?logo=streamlit)](https://budget-optimizer-app-lc8cszgmwbs7fmxdc4ps3d.streamlit.app/)
[![GitHub license](https://img.shields.io/github/license/shweMax/Budget-Optimizer-App)](https://github.com/shweMax/Budget-Optimizer-App)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)

---

## 📌 Project Overview

**Budget Optimizer App** is an interactive Streamlit web app that helps users allocate their monthly budget more effectively. It uses machine learning models trained on rural and urban spending datasets to provide intelligent suggestions for budget distribution across various categories like housing, food, transportation, and more.

---

## 🚀 Live Demo

🔗 **Try it here:**  
[https://budget-optimizer-app-lc8cszgmwbs7fmxdc4ps3d.streamlit.app/](https://budget-optimizer-app-lc8cszgmwbs7fmxdc4ps3d.streamlit.app/)

---

## 🧠 Features

- 📊 Intelligent budget optimization using ML models
- 🏙️ Supports both rural and urban budget predictions
- 📈 Pie chart visualization of suggested allocations
- ✅ Clean and minimal UI with Streamlit
- 🗂️ Easy to use: just input income and expenses

---

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Backend**: Python, scikit-learn
- **Data Handling**: Pandas, NumPy
- **Visualization**: Matplotlib
- **Model Storage**: Pickle (`.pkl` files)

---

## 🧾 Input Parameters

| Parameter              | Description                          |
|------------------------|--------------------------------------|
| `Income`               | Monthly income                       |
| `HousingExpense`       | Estimated housing cost               |
| `TransportationExpense`| Estimated transport cost             |
| `FoodExpense`          | Food and groceries cost              |
| `UtilitiesExpense`     | Bills and utilities                  |
| `EntertainmentExpense` | Leisure and hobbies                  |
| `Savings`              | Expected savings                     |

---

## 📦 Installation & Running Locally

### ✅ Requirements

Make sure you have Python 3.8+ and Git installed.

### 🔧 Setup

```bash
git clone https://github.com/shweMax/Budget-Optimizer-App.git
cd Budget-Optimizer-App
pip install -r requirements.txt
streamlit run app.py

