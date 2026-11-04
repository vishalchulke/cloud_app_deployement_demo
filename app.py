
from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Welcome to Cloud - Azure Flask</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: Arial, sans-serif;
            background: #f0f4f8;
            color: #333;
        }

        header {
            background: linear-gradient(120deg, #0078d4, #004578);
            color: white;
            padding: 25px;
            text-align: center;
        }

        nav {
            background: #00345c;
            padding: 15px;
            text-align: center;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 15px;
            font-weight: bold;
        }

        nav a:hover {
            color: #80d4ff;
        }

        .hero {
            padding: 65px 20px;
            text-align: center;
            background: white;
        }

        .hero h1 {
            font-size: 42px;
            color: #0078d4;
            margin-bottom: 15px;
        }

        .hero p {
            font-size: 18px;
            margin-bottom: 25px;
        }

        .button {
            display: inline-block;
            background: #0078d4;
            color: white;
            padding: 12px 25px;
            border-radius: 6px;
            text-decoration: none;
        }

        .container {
            max-width: 1100px;
            margin: auto;
            padding: 40px 20px;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
        }

        .card {
            background: white;
            padding: 25px;
            border-radius: 10px;
            text-align: center;
            box-shadow: 0 3px 12px #00000012;
        }

        .card h2 {
            color: #0078d4;
            margin-bottom: 15px;
        }

        .card p {
            line-height: 1.6;
        }

        .status {
            color: green;
            font-weight: bold;
        }

        .contact {
            background: white;
            padding: 30px;
            border-radius: 10px;
            text-align: center;
            margin-top: 30px;
        }

        input, textarea {
            width: 100%;
            max-width: 500px;
            padding: 12px;
            margin: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }

        button {
            background: #0078d4;
            color: white;
            border: none;
            padding: 12px 30px;
            border-radius: 5px;
            cursor: pointer;
        }

        footer {
            background: #00345c;
            color: white;
            text-align: center;
            padding: 20px;
            margin-top: 40px;
        }
    </style>
</head>

<body>

<header>
    <h1>Microsoft Azure Cloud Platform</h1>
    <p>Python Flask Web Application</p>
</header>

<nav>
    <a href="/">Home</a>
    <a href="/about">About</a>
    <a href="/services">Services</a>
    <a href="/contact">Contact</a>
</nav>

<section class="hero">
    <h1>Welcome to Cloud!</h1>
    <p>Successfully Deployed on Microsoft Azure</p>
    <p>Experience the power of Python, Flask and Cloud Computing.</p>
    <a href="/services" class="button">Explore Services</a>
</section>

<div class="container">

    <h2 style="text-align:center; margin-bottom:25px;">
        Cloud Dashboard
    </h2>

    <div class="cards">

        <div class="card">
            <h2>☁️ Cloud Platform</h2>
            <p>Application hosted on Microsoft Azure App Service.</p>
        </div>

        <div class="card">
            <h2>🐍 Python Flask</h2>
            <p>Backend application developed using Python Flask.</p>
        </div>

        <div class="card">
            <h2>🚀 Deployment</h2>
            <p>Application deployed using Azure App Service.</p>
        </div>

        <div class="card">
            <h2>✅ Status</h2>
            <p class="status">Application Running Successfully</p>
        </div>

    </div>

    <div class="contact">
        <h2>Contact Us</h2>
        <p>Send us a message</p>

        <form action="/contact" method="POST">
            <input type="text" name="name"
                   placeholder="Enter your name" required>

            <br>

            <input type="email" name="email"
                   placeholder="Enter your email" required>

            <br>

            <textarea name="message"
                      placeholder="Enter your message"
                      required></textarea>

            <br>

            <button type="submit">Submit</button>
        </form>

        <p>{{ message }}</p>
    </div>

</div>

<footer>
    <p>© 2026 Azure Flask Cloud Application</p>
    <p>Powered by Python and Microsoft Azure</p>
</footer>

</body>
</html>
"""


@app.route('/')
def home():
    return render_template_string(HTML, message="")


@app.route('/about')
def about():
    return """
    <h1>About Our Cloud Application</h1>
    <p>This application is developed using Python Flask.</p>
    <p>It is hosted on Microsoft Azure App Service.</p>
    <a href="/">Back to Home</a>
    """


@app.route('/services')
def services():
    return """
    <h1>Cloud Services</h1>
    <ul>
        <li>Azure App Service</li>
        <li>Python Flask Development</li>
        <li>Cloud Hosting</li>
        <li>Application Deployment</li>
        <li>Cloud Scalability</li>
    </ul>
    <a href="/">Back to Home</a>
    """


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name', '')
        email = request.form.get('email', '')
        message = request.form.get('message', '')

        print("Contact Form Submission:")
        print("Name:", name)
        print("Email:", email)
        print("Message:", message)

        return render_template_string(
            HTML,
            message="Thank you, " + name + "! Message received."
        )

    return render_template_string(HTML, message="")


@app.route('/health')
def health():
    return {
        "status": "healthy",
        "application": "Azure Flask Cloud App",
        "platform": "Microsoft Azure"
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
