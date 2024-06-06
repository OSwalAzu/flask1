from flask import Flask, render_template_string, url_for

app = Flask(__name__)

home_html = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tarjeta de Presentación</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        .card {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            text-align: center;
            padding: 20px;
        }
        .card img {
            border-radius: 50%;
            width: 150px;
            height: 150px;
        }
        .card h1 {
            font-size: 24px;
            margin: 10px 0;
        }
        .card p {
            font-size: 18px;
            color: #555;
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="card">
        <img src="{{ url_for('static', filename='doval.jpg') }}" alt="Foto de Oswaldo">
        <h1>Oswaldo Azuara Morales</h1>
        <p>Cuatrimestre: 9   Grupo: A</p>
        <p>Matrícula: 20211318</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(home_html)

if __name__ == '__main__':
    app.run(debug=True)
