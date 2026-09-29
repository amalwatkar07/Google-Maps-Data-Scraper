# Google Maps Data Scraper

A Django-based web application for scraping and collecting business information from Google Maps.

The project provides a web interface that can be used to search Google Maps and collect business-related information into a local database for further analysis and use.

Note: This project is intended for educational and research purposes. Make sure your use of Google Maps and any collected data complies with Google's Terms of Service, applicable laws, and privacy requirements.

✨ Features

🔎 Search Google Maps for businesses and places

📍 Collect business/location information

🗃️ Store scraped data in a local SQLite database

🌐 Django-based web interface

🖥️ Run locally on Windows

🐍 Python-based project

📊 Easily extendable for additional scraping and data-processing features

## 🛠️ Tech Stack

Python

Django

SQLite

HTML/CSS

JavaScript

Google Maps web interface

📁 Project Structure
Google-Maps-Data-Scraper/
│
├── Scrape/
│   ├── migrations/
│   ├── templates/
│   ├── ...
│
├── ScrapeApp/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── ...
│
├── db.sqlite3
├── database.txt
├── manage.py
├── requirements.txt
├── runWebServer.bat
├── SCREENS.docx
└── README.md

🚀 Getting Started
1. Clone the repository
git clone https://github.com/amalwatkar07/Google-Maps-Data-Scraper.git


Navigate to the project directory:

cd Google-Maps-Data-Scraper

2. Create a virtual environment

It is recommended to use a Python virtual environment.

Windows
python -m venv venv
venv\Scripts\activate

macOS / Linux
python3 -m venv venv
source venv/bin/activate

3. Install dependencies

Install the required Python packages:

pip install -r requirements.txt

▶️ Running the Application

Run the Django development server:

python manage.py runserver


You should see output similar to:

Starting development server at http://127.0.0.1:8000/


Open the following address in your browser:

http://127.0.0.1:8000/

Windows Quick Start

The repository also includes:

runWebServer.bat


You can run this batch file on Windows to start the web server, provided that the required Python environment and dependencies are installed.

🗄️ Database

The project uses SQLite as its database.

The repository contains:

db.sqlite3


Django database migrations can be applied with:

python manage.py migrate


If you make changes to Django models, create new migrations with:

python manage.py makemigrations


Then apply them:

python manage.py migrate

⚙️ Configuration

Before running the application, make sure that:

Python is installed.

The required dependencies from requirements.txt are installed.

The Django project is configured correctly.

Your internet connection is active when accessing Google Maps data.

Any scraping activity complies with applicable terms, laws, and privacy requirements.

📊 Data

Depending on the implementation and configuration of the scraper, collected information can be stored in the application's database and used by the Django application.

Typical Google Maps business information may include fields such as:

Business name

Address

Phone number

Website

Business category

Rating

Review information

Location information

The exact fields available depend on the scraper implementation.

🖼️ Screenshots

Project screenshots/documentation are included in:

SCREENS.docx


You can add screenshots to this README later by placing image files in a screenshots/ directory and referencing them like this:

![Application Screenshot](screenshots/home.png)

🐛 Troubleshooting
ModuleNotFoundError

Make sure the virtual environment is activated and install the dependencies again:

pip install -r requirements.txt

Django server does not start

Try:

python manage.py check


Then:

python manage.py migrate
python manage.py runserver

Port 8000 is already in use

Run Django on another port:

python manage.py runserver 8080


Then open:

http://127.0.0.1:8080/

Database problems

If you are working with a fresh installation, run:

python manage.py migrate

🔒 Responsible Use

This project interacts with publicly accessible information from Google Maps. Users are responsible for ensuring that their use of the scraper complies with:

Google's applicable terms and policies

Local and national laws

Data-protection and privacy requirements

Website access and scraping restrictions

Do not use collected information for spam, harassment, unauthorized profiling, or other unlawful activities.

🤝 Contributing

Contributions are welcome.

Fork the repository.

Create a new branch:

git checkout -b feature/my-feature


Make your changes.

Commit your changes:

git add .
git commit -m "Add my feature"


Push the branch:

git push origin feature/my-feature


Open a Pull Request.

📌 Future Improvements

Possible improvements include:

Add CSV/Excel export

Add JSON export

Improve search and filtering

Add pagination for scraped results

Add configurable scraping parameters

Improve error handling

Add authentication and user management

Add automated tests

Add Docker support

Improve the UI/UX

Add detailed scraping statistics

📄 License

No license is currently specified in the repository.

If you intend to make this project open source, consider adding an appropriate license file such as LICENSE.

👨‍💻 Author

Amal Watkar

GitHub:
https://github.com/amalwatkar07

⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub and contributing improvements.

Repository:
https://github.com/amalwatkar07/Google-Maps-Data-Scraper
