# Python Project 4 🚀

## Project Setup Guide 🛠️

Follow the steps below to set up and run the project on your local machine.

### Step 1: Clone the Repository 📂
```bash
git clone https://github.com/Stclair-4/DAB111_project_Group_4.git
cd python_project
```

### Step 2: Create and Activate a Virtual Environment (Optional but Recommended) 🌐
#### For Bash:
```bash
python -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies 📦
```bash
pip install -r requirements.txt
```

### Step 4: Create a Credentials File 🔑
Create a `credentials.py` file in the root directory and add the following content:
```python
# Replace with your actual API key and base URL
API_KEY = "WRITE_YOUR_OWN_API_KEY"
BASE_URL = "WRITE_YOUR_OWN_BASE_URL"
```

For this project just add this to run.
```python
API_KEY = "71739f1828mshb0ea83b855341a1p1ad4d3jsnedc6ea1d0a16"
BASE_URL = "https://exercisedb.p.rapidapi.com"
```

### Step 5: Initialize the Database 🗃️
```bash
python init_db.py
```

### Step 6: Start the Application 🚀
```bash
flask run
```

---

## Acknowledgements 🙏
We would like to express our gratitude to all contributors and developers who helped build this project. Special thanks to the open-source community for providing valuable libraries and tools.

```
Chandresh A Sachala
Namrata C Chaudhari
Souravdeep Singh
Komalpreet Kaur
```

## References 📚
- [API Integration](https://medium.com/strategioexploring-flask-and-external-api-integration-flask-weather-app-6a5774935bb3)
- [Python Official Website](https://www.python.org/)
- [GitHub Guide](https://docs.github.com/en/get-started/quickstart)

## Dataset Link 🔗
Please download the dataset from the following link:
- [Dataset Download](https://www.kaggle.com/datasets/valakhorasani/gym-members-exercise-dataset/data) 

---

**Note:** Ensure you have Python and Git installed on your machine before starting the setup process.

