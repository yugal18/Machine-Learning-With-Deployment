# My End-to-End Machine Learning Project with Deployment

This repository showcases a comprehensive machine learning pipeline, including data ingestion, transformation, model training, and deployment via a web application.

---

## 🚀 **Project Structure**

The project is organized into several directories and files to make the workflow more modular and maintainable. Below is the structure:

└── artifacts/                                  # Stores intermediate outputs like processed data and models
└── build/                                      # Build files for the project
└── catboost_info/                              # Logs and metadata for CatBoost models
└── dist/                                       # Distribution files
└── logs/                                       # Execution logs for debugging and monitoring
└── notebook/                                   # Jupyter notebooks for analysis and experiments
│   └── data/
│   └── EDA_Student_Performance.ipynb           # Exploratory Data Analysis notebook
│   └── Model_Training.ipynb                    # Notebook for training models
└── src/                                        # Source code for the ML pipeline
│   └── components/                             # Core components for the pipeline
│   └── pipeline/                               # Training and prediction pipelines
│   └── train_pipeline.py                       # Training pipeline
│   └── predict_pipeline.py                     # Prediction pipeline
│   └── exception.py                            # Custom exception handling
│   └── logger.py                               # Logging utility
│   └── utils.py                                # Helper functions
└── templates/                                  # HTML templates for the web app
│   └── home.html                               # Home page template
│   └── index.html                              # Main interface template
└── venv/                                       # Virtual environment for dependencies
└── .gitignore                                  # Files and folders to ignore in version control
└── README.md                                   # Project documentation
└── requirements.txt                            # Python dependencies
└── setup.py                                    # Setup script for project packaging
└── app.py                                      # Main Flask application





---

## 📝 **Features**

- **Data Exploration and Visualization:**
  - Analyze and visualize datasets in Jupyter notebooks.
  - Perform exploratory data analysis (EDA) on student performance datasets.

- **Pipeline for Model Training:**
  - Includes data ingestion, preprocessing, and training pipelines.
  - Supports CatBoost and other models.

- **Web-Based Deployment:**
  - Deploy ML models using Flask with interactive web pages.

- **Custom Logging and Exception Handling:**
  - Comprehensive logging for monitoring pipeline executions.
  - Structured exception handling for easier debugging.

---

## ⚙️ **Setup Instructions**

### **Prerequisites**
- Python 
- Virtual environment (venv) or conda

---

### **Steps to Set Up**

1. **Clone the Repository:**
    ```bash
    git clone https://github.com/yugal18/Machine-Learning-With-Deployment.git
    ```

2. **Navigate to the Project Directory:**
    ```bash
    cd End-to-End-ML-Project
    ```

3. **Create a Virtual Environment:**
    ```bash
    python -m venv venv
    ```

4. **Activate the Virtual Environment:**

    - **Windows:**
      ```bash
      venv\Scripts\activate
      ```

    - **macOS/Linux:**
      ```bash
      source venv/bin/activate
      ```

5. **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Run the Flask Application:**
    ```bash
    python app.py
    ```

7. Open the app in your browser at:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

   [http://127.0.0.1:5000/predictdata]


---

## 🌟 **Key Highlights**

- **End-to-End Implementation:** From raw data to model deployment.
- **User-Friendly Interface:** Interactive web interface for model predictions.
- **Extensive Logging:** Track and debug pipeline execution with detailed logs.

---

## 🛠️ **Technologies Used**

- **Languages:** Python
- **Frameworks:** Flask
- **Modeling:** CatBoost, scikit-learn
- **Visualization:** Jupyter Notebook
- **Environment:** venv

---

## 🤝 **Contribution**

Contributions are welcome! Please fork the repository and submit a pull request. For major changes, open an issue first to discuss.

---

## 📝 **License**

This project is licensed under the **MIT License**.

---




