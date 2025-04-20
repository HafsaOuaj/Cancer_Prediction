# Cancer Prediction using Machine Learning and Streamlit

Welcome to the **Cancer Prediction** project! This project leverages **machine learning** algorithms to predict the likelihood of cancer based on a dataset of clinical features. The model is deployed as a **Streamlit web application**, allowing users to interact with the model and input their own data for real-time predictions.

![Cancer Prediction](https://github.com/HafsaOuaj/Cancer_Prediction/assets/99544208/3a77b45b-cf28-4003-90d4-4b081bd29e2e)

## ⚙️ Features

- **Predict Cancer Type**: The web app predicts whether a tumor is malignant or benign based on clinical data using machine learning.
- **User Input**: Users can input new data to predict the cancer status, enabling personalized predictions.
- **Interactive Visualization**: The app provides real-time updates and visualizations for better understanding and decision-making.
- **Model Explanation**: Get insights into the underlying machine learning model used for prediction.

## 🧠 Machine Learning Model

The model used for cancer prediction is based on a popular dataset of breast cancer features, including various medical attributes such as cell size, shape, and texture. The following algorithms have been implemented and tested:

- **Logistic Regression**
- **Random Forest**
- **Support Vector Machine (SVM)**

Each model is trained to classify the tumors as **malignant** or **benign** based on the features provided.

## 🚀 How to Run the Web App

To run the **Cancer Prediction Web App** locally, follow these steps:

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/HafsaOuaj/Cancer_Prediction.git
cd Cancer_Prediction
```

### 2. Install Dependencies

Use `Poetry` to install the necessary dependencies:

```bash
poetry install
```

Alternatively, if you're not using Poetry, you can install the dependencies manually by creating a `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Set Up the Environment

Create a `.env` file in the root directory for any environment variables (if needed). Ensure that all configurations are set for the app to run correctly.

### 4. Run the Streamlit App

Launch the application using Streamlit:

```bash
streamlit run app.py
```

Once the app is running, you can access it in your web browser (usually at `http://localhost:8501`).

## 🔍 How it Works

The web app is designed to allow users to enter key features related to breast cancer (like radius, texture, perimeter, etc.) and predict whether the tumor is benign or malignant. The underlying machine learning models predict the outcome based on the data entered and provide the user with an instant result.

### Data Preprocessing

The dataset used for training the models is preprocessed to handle missing values, normalize features, and split the data into training and testing sets. The most relevant features are selected for training to ensure that the model performs optimally.

### Model Training

The models are trained on the processed dataset using a variety of machine learning algorithms. After training, the model is evaluated on a test set to measure its accuracy and performance. The best-performing model is deployed in the web app.

### Real-time Prediction

Once deployed, the app accepts user inputs in real-time. The model processes the data, applies the trained algorithms, and outputs a prediction. This allows users to quickly assess the risk of cancer based on their data.

## 📸 Application Screenshots

Here are some screenshots showcasing the **Cancer Prediction Web App**:

![Screenshot 1](https://github.com/HafsaOuaj/Cancer_Prediction/assets/99544208/3a77b45b-cf28-4003-90d4-4b081bd29e2e)

---

## 🧑‍💻 Tech Stack

- **Streamlit**: For creating the interactive web interface.
- **Scikit-learn**: Used for implementing machine learning algorithms like Logistic Regression, Random Forest, and SVM.
- **Pandas**: Data manipulation and analysis.
- **Matplotlib**: Data visualization and plotting.
- **NumPy**: For numerical computations.

---

## 📊 Evaluation

- **Accuracy**: Each model is evaluated on its accuracy score using cross-validation techniques.
- **Precision, Recall, F1-Score**: Metrics used to evaluate the model's performance in terms of its ability to correctly predict malignant and benign tumors.

---

## 🤝 Contributing

We welcome contributions! Feel free to open issues, submit feature requests, or send pull requests for improvements or bug fixes.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or inquiries, feel free to reach out to me at [hafsa.ouajdi.fr@gmail.com](mailto:hafsa.ouajdi.fr@gmail.com).

---

## 💡 Future Improvements

- Integrate more features for more accurate predictions.
- Deploy on cloud platforms such as **Heroku**, **AWS**, or **Google Cloud**.
- Add additional model evaluation techniques (e.g., ROC-AUC, confusion matrix).
- Explore deploying deep learning models for further improvement in predictions.

