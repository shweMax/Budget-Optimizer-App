import streamlit as st
import pandas as pd
import pickle
import os
import matplotlib.pyplot as plt

# ---------------------------- #
#       Streamlit Setup       #
# ---------------------------- #
st.set_page_config(page_title="Budget Optimiser", page_icon="💰")
st.title("💰 Budget Optimiser")
st.markdown("Use ML models or simple rules to plan your monthly budget smartly.")

# ---------------------------- #
#     Define Categories & %   #
# ---------------------------- #
recommended_percentages = {
    'Housing': 0.30,
    'Transportation': 0.10,
    'Food': 0.10,
    'Utilities': 0.05,
    'Entertainment': 0.05,
    'Savings': 0.20
}

model_categories = ['Housing', 'Transportation', 'Food',
                    'Utilities', 'Entertainment', 'Savings']

# ---------------------------- #
#           Tabs              #
# ---------------------------- #
tab1, tab2 = st.tabs(["📊 Model-Based Prediction", "📐 Rule-Based Suggestion"])

# ---------------------------- #
#     Tab 1: Model-Based      #
# ---------------------------- #
with tab1:
    st.subheader("Predict Budget Allocation using Trained ML Model")

    area_type = st.selectbox("Select Area Type", ["Rural", "Urban"])

    # Load model
    model_path = f"model/{area_type.lower()}_model.pkl"
    if not os.path.exists(model_path):
        st.error(f"Model not found at {model_path}")
        st.stop()

    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Input financial details
    st.markdown("### 📥 Enter Your Financial Details:")
    income = st.number_input("Income", min_value=0.0, format="%.2f")
    housing_exp = st.number_input("Housing Expense", min_value=0.0, format="%.2f")
    transport_exp = st.number_input("Transportation Expense", min_value=0.0, format="%.2f")
    food_exp = st.number_input("Food Expense", min_value=0.0, format="%.2f")
    utilities_exp = st.number_input("Utilities Expense", min_value=0.0, format="%.2f")
    entertainment_exp = st.number_input("Entertainment Expense", min_value=0.0, format="%.2f")
    savings = st.number_input("Savings", min_value=0.0, format="%.2f")

    if st.button("Predict Budget Allocation"):
        input_data = pd.DataFrame([{
            'Income': income,
            'HousingExpense': housing_exp,
            'TransportationExpense': transport_exp,
            'FoodExpense': food_exp,
            'UtilitiesExpense': utilities_exp,
            'EntertainmentExpense': entertainment_exp,
            'Savings': savings
        }])

        prediction = model.predict(input_data)[0]

        results_df = pd.DataFrame({
            'Category': model_categories,
            'Amount (₹)': prediction
        })

        st.markdown("### 📊 Predicted Budget Allocation:")
        st.dataframe(results_df.style.format({'Amount (₹)': '₹ {:.2f}'}), use_container_width=True)

        #pie-chart
        # Pie Chart
        fig1, ax1 = plt.subplots()
        colors = ['#66b3ff', '#ff9999', '#99ff99', '#ffcc99', '#c2c2f0', '#ffb3e6']  # Optional: define consistent color palette
        ax1.pie(prediction, labels=model_categories, autopct='%1.1f%%', startangle=90, colors=colors)
        ax1.axis('equal')
        ax1.set_title("Predicted Budget Allocation", fontsize=14, pad=30)
        plt.subplots_adjust(top=0.85)
        st.pyplot(fig1)

        # Warning if savings are negative

        if prediction[-1] < 0:
            st.warning("⚠️ Negative savings predicted. Consider reducing some expenses.")



# ---------------------------- #
#     Tab 2: Rule-Based       #
# ---------------------------- #
with tab2:
    st.subheader("Simple Budget Suggestion Based on Income")

    # Let user choose Urban or Rural
    rule_area_type = st.selectbox("Select Area Type", ["Rural", "Urban"], key="rule_area")

    # Set rules based on type
    if rule_area_type == "Rural":
        budget_percentages = {
            'Housing': 0.25,
            'Transportation': 0.10,
            'Food': 0.15,
            'Utilities': 0.05,
            'Entertainment': 0.05,
            'Savings': 0.40
        }
    else:  # Urban
        budget_percentages = {
            'Housing': 0.35,
            'Transportation': 0.15,
            'Food': 0.15,
            'Utilities': 0.05,
            'Entertainment': 0.10,
            'Savings': 0.20
        }

    # Input income
    income_only = st.number_input("Enter your Monthly Income (₹)", min_value=0.0, format="%.2f", key="income_only")

    if st.button("Get Suggested Budget Allocation", key="suggest"):
        if income_only == 0:
            st.warning("Please enter a valid income.")
        else:
            recommended = {category: income_only * pct for category, pct in budget_percentages.items()}
            budget_df = pd.DataFrame(list(recommended.items()), columns=['Category', 'Recommended Amount (₹)'])

            st.markdown(f"### 💡 Suggested Allocation for **{rule_area_type}**:")
            st.dataframe(budget_df.style.format({'Recommended Amount (₹)': '₹ {:.2f}'}), use_container_width=True)

            st.markdown("🔹 This is based on custom rules for rural vs urban lifestyle budgeting.")
