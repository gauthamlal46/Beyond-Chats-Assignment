1. Clone the repository to your local machine:

git clone <repository-url>

2. Navigate to the project directory:

cd <project-directory>
Create a new folder "templates" and move "index.html" to templates

3. Install the required dependencies. It's recommended to create a virtual environment first:

python3 -m venv venv
source venv/bin/activate  # For Unix/Linux
# OR
venv\Scripts\activate  # For Windows
pip install -r requirements.txt

4. Run the Flask application:

python app.py

5. Open a web browser and go to http://localhost:5000/ to view the citations