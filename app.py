import streamlit as st
import pandas as pd
import joblib

# Load model and encoders
model = joblib.load("random_forest_model.pkl")
feature_names = joblib.load("feature_names.pkl")
label_encoders = joblib.load("label_encoders.pkl")

# Optional banner image
st.image("https://i.imgur.com/FORzQZP.png", use_column_width=True)

# Title
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>📊 Bank Term Deposit Prediction</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Enter customer details below to predict whether they will subscribe to a term deposit.</p>", unsafe_allow_html=True)
st.markdown("---")

# Input form
with st.form("prediction_form"):
    st.subheader("🧍‍♂️ Customer Profile")
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("🎂 Age", min_value=18, max_value=100, step=1)
        job = st.selectbox("💼 Job", label_encoders['job'].classes_)
        marital = st.selectbox("❤️ Marital Status", label_encoders['marital'].classes_)
        education = st.selectbox("🎓 Education", label_encoders['education'].classes_)
        default = st.selectbox("💳 Default on Credit?", label_encoders['default'].classes_)
        housing = st.selectbox("🏠 Housing Loan?", label_encoders['housing'].classes_)
        loan = st.selectbox("📄 Personal Loan?", label_encoders['loan'].classes_)

    with col2:
        contact = st.selectbox("📞 Contact Type", label_encoders['contact'].classes_)
        month = st.selectbox("🗓️ Last Contact Month", label_encoders['month'].classes_)
        day_of_week = st.selectbox("📆 Day of Week", label_encoders['day_of_week'].classes_)
        campaign = st.number_input("📣 Campaign Contacts", min_value=0, step=1)
        pdays = st.number_input("📅 Days Since Last Contact", min_value=-1, step=1)
        previous = st.number_input("🔁 Previous Contacts", min_value=0, step=1)
        poutcome = st.selectbox("📊 Previous Outcome", label_encoders['poutcome'].classes_)

    st.subheader("📈 Economic Indicators")
    emp_var_rate = st.number_input("📉 Employment Variation Rate", format="%.2f")
    cons_price_idx = st.number_input("💰 Consumer Price Index", format="%.2f")
    cons_conf_idx = st.number_input("📉 Consumer Confidence Index", format="%.2f")
    euribor3m = st.number_input("🏦 Euribor 3 Month Rate", format="%.3f")
    nr_employed = st.number_input("👨‍💼 Number of Employees", format="%.1f")

    st.markdown(" ")
    submitted = st.form_submit_button("🚀 Predict")

# Prediction logic
if submitted:
    # Prepare input data
    input_data = {
        "age": age,
        "job": job,
        "marital": marital,
        "education": education,
        "default": default,
        "housing": housing,
        "loan": loan,
        "contact": contact,
        "month": month,
        "day_of_week": day_of_week,
        "campaign": campaign,
        "pdays": pdays,
        "previous": previous,
        "poutcome": poutcome,
        "emp.var.rate": emp_var_rate,
        "cons.price.idx": cons_price_idx,
        "cons.conf.idx": cons_conf_idx,
        "euribor3m": euribor3m,
        "nr.employed": nr_employed
    }

    input_df = pd.DataFrame([input_data])

    # Label encoding
    for col, encoder in label_encoders.items():
        if col in input_df.columns:
            if input_df[col][0] in encoder.classes_:
                input_df[col] = encoder.transform(input_df[col])
            else:
                st.error(f"⚠️ '{input_df[col][0]}' not seen in training for column '{col}'. Please select valid input.")
                st.stop()

    # Ensure correct feature order
    input_df = input_df[feature_names]

    # Predict
    prediction = model.predict(input_df)[0]

    # Output
    st.markdown("---")
    if prediction == 1:
        st.success("✅ The customer is likely to **subscribe** to a term deposit!")
        st.balloons()
    else:
        st.warning("❌ The customer is **not likely** to subscribe.")
