from flask import Flask, render_template_string
import os

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Poomalai B - Embedded Developer</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', sans-serif;
            background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
            color: #fff;
        }
        header {
            background: rgba(0,0,0,0.6);
            padding: 60px 20px;
            text-align: center;
            color: #fff;
        }
        header h1 {
            font-size: 3rem;
            color: #ff2a6d;
        }
        header p {
            font-size: 1.2rem;
        }
        .btn-custom {
            background-color: #ff2a6d;
            color: #fff;
            border: none;
            padding: 10px 25px;
            margin: 10px;
            transition: all 0.3s ease;
        }
        .btn-custom:hover {
            background-color: #ff0050;
            transform: scale(1.05);
        }
        section {
            padding: 60px 20px;
        }
        .section-title {
            font-size: 2rem;
            border-left: 5px solid #00ffe0;
            padding-left: 10px;
            margin-bottom: 30px;
            color: #00ffe0;
        }
        .card {
            background-color: #1e1e2f;
            border: none;
            box-shadow: 0 0 10px rgba(0, 255, 200, 0.1);
            color: #fff;
            margin-bottom: 20px;
        }
        footer {
            text-align: center;
            padding: 30px;
            color: #aaa;
        }
        .profile-pic {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
            border: 4px solid #ff2a6d;
        }
    </style>
</head>
<body>

    <header>
        <img src="https://res.cloudinary.com/dtjjgiitl/image/upload/q_auto:good,f_auto,fl_progressive/v1752165287/q5c84ofs2q72r4ujfimk.jpg">
        <h1>Hi, I'm Poomalai</h1>
        <p>Embedded Developer | IoT Enthusiast | UI/UX Designer</p>
        <a href="#contact" class="btn btn-custom">Hire Me</a>
        <a href="#projects" class="btn btn-custom">View Projects</a>
    </header>

    <section id="about">
        <div class="container">
            <h2 class="section-title">About Me</h2>
            <p>I’m passionate about electronics, embedded systems, and intuitive design. I create real-world IoT projects using Arduino and Raspberry Pi, and I also enjoy crafting clean UI/UX interfaces using Figma and Canva.</p>
        </div>
    </section>

    <section id="skills">
        <div class="container">
            <h2 class="section-title">Skills</h2>
            <ul>
                <li>Embedded C, Python, IoT Protocols</li>
                <li>PCB Design (KiCad, EasyEDA)</li>
                <li>Arduino, Raspberry Pi, Sensors</li>
                <li>UI/UX Design (Figma, Canva)</li>
                <li>Simulation Tools (Proteus, MATLAB, ThingSpeak)</li>
            </ul>
        </div>
    </section>

    <section id="projects">
        <div class="container">
            <h2 class="section-title">Projects</h2>
            <div class="row">
                <div class="col-md-4">
                    <div class="card p-3">
                        <h5>Color Sorting Machine</h5>
                        <p>Uses Raspberry Pi Zero W and camera to detect object colors and sort them using servo motors.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3">
                        <h5>Gas Leakage Detection</h5>
                        <p>Arduino-based gas sensor system with alert via buzzer and LED when leaks are detected.</p>
                    </div>
                </div>
                <div class="col-md-4">
                    <div class="card p-3">
                        <h5>Mobile App UI</h5>
                        <p>Clean mobile UI designed in Figma focusing on modern layout and responsive experience.</p>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="contact">
        <div class="container">
            <h2 class="section-title">Contact</h2>
            <p><strong>Email:</strong> poomalairaja33@gmail.com</p>
            <p><strong>Phone:</strong> +91 9159842429</p>
            <p><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/poomalai-b-00778a262" target="_blank" style="color:#00ffe0;">poomalai-b</a></p>
        </div>
    </section>

    <footer>
        © 2025 Poomalai B — Portfolio
    </footer>

</body>
</html>
'''

@app.route('/')
def portfolio():
    return render_template_string(html)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
