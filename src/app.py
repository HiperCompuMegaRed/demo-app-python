from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def container_info():
    container_name = os.environ.get('HOSTNAME', 'No container name')
    container_language = os.environ.get('PYTHON_VERSION', 'No version')
    container_demoenv = os.environ.get('DEMO_ENV', 'No variable defined')
    container_demosecret = os.environ.get('DEMO_SECRET', 'No variable defined')
    container_project = os.environ.get('PROJECT', 'No project defined')
    container_env = os.environ.get('ENV', 'No ENV defined')
    html = f"""
    <html>
    <head>
        <title>Container Info</title>
        <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Encode+Sans:wght@400;700&display=swap">
        <style>
            .container {{
                font-family: 'Encode Sans', sans-serif;
                width: 300px;
                padding: 20px;
                border: 1px solid #ccc;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                margin: 50px auto;
                background-color: #fff;
                text-align: center;
            }}

            .header {{
                font-family: 'Encode Sans', sans-serif;
                background-color: #7D00FF; /* Change the color as desired */
                color: #fff;
                padding: 10px;
                text-align: center;
                font-weight: bold;
                border-top-left-radius: 10px; /* Rounded top-left corner */
                border-top-right-radius: 10px; /* Rounded top-right corner */
                border-bottom-left-radius: 10px; /* Rounded top-left corner */
                border-bottom-right-radius: 10px;
            }}

            .logo {{
                height: 50px;
                widht: 40px;
                margin-top: 10px;
                margin-bottom: 20px;

            }}
        </style>
    </head>
    <body>
        <div class="container">
            <img class="logo" src="https://www.shamanops.com/assets/img2/logo_shamanops.svg" alt="Logo Image">
            <div class="header">Container Information</div>
            <p><strong>PROJECT</strong><br> {container_project}</p>
            <p><strong>ENV</strong><br> {container_env}</p>
            <p><strong>LANGUAGE VERSION</strong><br> {container_language}</p>
            <p><strong>CONTAINER NAME</strong><br> {container_name}</p>
            <p><strong>DEMO ENVIRONMENT</strong><br> {container_demoenv}</p>
            <p><strong>DEMO SECRET</strong><br> {container_demosecret}</p>
            <img class="logo" src="https://www.shamanops.com/assets/img2/python.png" alt="logo-python">
        </div>
    </body>
    </html>
    """
    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

