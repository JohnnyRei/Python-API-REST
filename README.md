# Python API REST

## Description

This project is a Flask application that connects to a Microsoft SQL Server database using pyodbc and retrieves data from a table. The retrieved data is then returned as a JSON response.

## Prerequisites

To run this project, you need to have the following prerequisites installed:

- Python 3
- Flask
- pyodbc
- ODBC Driver 17 for SQL Server

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-username/your-project.git
   ```

2. Change to the project directory:

   ```
   cd your-project
   ```

3. Install the required dependencies:

   ```
   pip install flask pyodbc
   ```

4. Configure the database connection:
   - Open the `app.py` file in a text editor.
   - Modify the following variables with your database connection details:
     - `server`: The server name or IP address where your SQL Server is hosted.
     - `database`: The name of the database you want to connect to.
     - `username`: The username to authenticate with the database.
     - `password`: The password for the provided username.
   - Save the changes.

## Usage

1. Run the Flask application:

   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5000`.
3. The application will retrieve data from the specified table in the database and return it as a JSON response.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
