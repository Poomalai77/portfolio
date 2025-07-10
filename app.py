from flask import Flask, render_template_string
import os

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Poomalai B - Embedded Developer Portfolio</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background-color: #121212;
            color: #e0e0e0;
            font-family: 'Segoe UI', sans-serif;
            padding: 30px;
        }
        h1, h2 {
            color: #00ffc8;
            border-bottom: 2px solid #00ffc8;
            display: inline-block;
            margin-bottom: 20px;
        }
        .section {
            margin-bottom: 60px;
        }
        .card {
            background-color: #1e1e1e;
            border: 1px solid #333;
            box-shadow: 0 0 15px rgba(0,255,200,0.2);
            color: #ccc;
        }
        a {
            color: #00ffc8;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .project-img {
            width: 100%;
            border-radius: 10px;
        }
        .container {
            max-width: 900px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center">Poomalai B</h1>
        <p class="text-center">Embedded Developer | IoT Engineer | UI/UX Designer</p>

        <div class="section">
            <h2>About Me</h2>
            <p>I specialize in embedded systems and love building real-world projects using Arduino, Raspberry Pi, and various sensors. I also enjoy designing clean, functional UI/UX using tools like Figma.</p>
        </div>

        <div class="section">
            <h2>Skills</h2>
            <ul>
                <li>Embedded C, Python, IoT Protocols</li>
                <li>PCB Design - KiCad, EasyEDA</li>
                <li>Arduino, Raspberry Pi, Sensors</li>
                <li>UI/UX Design - Figma, Canva</li>
                <li>Simulation - Proteus, MATLAB, ThingSpeak</li>
            </ul>
        </div>

        <div class="section">
            <h2>Education</h2>
            <ul>
                <li><strong>KSR Institute of Engineering & Technology</strong> – B.E. (2022–2026)</li>
                <li><strong>HSC:</strong> Bharathi Matric Hr. Sec School (75%)</li>
                <li><strong>SSLC:</strong> Bharathi Matric Hr. Sec School (90%)</li>
            </ul>
        </div>

        <div class="section">
            <h2>Internships</h2>
            <ul>
                <li><strong>NoviTech R&D Pvt Ltd</strong> – IoT Hardware & Sensor Communication</li>
                <li><strong>Rabbit QR</strong> – UI/UX Design using Figma</li>
                <li><strong>Brainery Spot</strong> – Arduino & Raspberry Pi Projects</li>
            </ul>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <div class="row g-4">
                <div class="col-md-6">
                    <div class="card p-3">
                        <img src="https://via.placeholder.com/400x200?text=Color+Sorting+Machine" class="project-img" alt="Color Sorting Machine">
                        <h5 class="mt-3">Color Sorting Machine</h5>
                        <p>Using Raspberry Pi & camera to detect and sort objects based on color.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card p-3">
                        <img src="https://via.placeholder.com/400x200?text=Gas+Leakage+Detection" class="project-img" alt="Gas Leakage Detection">
                        <h5 class="mt-3">Gas Leakage Detection</h5>
                        <p>Arduino + Gas Sensor with buzzer and LED alert system for safety.</p>
                    </div>
                </div>
                <div class="col-md-6">
                    <div class="card p-3">
                        <img src="https://via.placeholder.com/400x200?text=Mobile+App+UI" class="project-img" alt="Mobile App UI">
                        <h5 class="mt-3">Mobile App UI/UX Design</h5>
                        <p>Clean, responsive UI designed with Figma for a modern app concept.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="section">
            <h2>Certifications</h2>
            <ul>
                <li>Introduction to IoT – NPTEL</li>
                <li>Arduino vs Raspberry Pi – Great Learning</li>
                <li>Wiring Harness Workshop – KSRIET</li>
            </ul>
        </div>

        <div class="section">
            <h2>Other Activities</h2>
            <p>NCC B & C Certificate Holder</p>
        </div>

        <div class="section">
            <h2>Contact</h2>
            <ul>
                <li><strong>Email:</strong> poomalairaja33@gmail.com</li>
                <li><strong>Phone:</strong> +91 9159842429</li>
                <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/poomalai-b-00778a262" target="_blank">poomalai-b</a></li>
            </ul>
        </div>
    </div>
</body>
</html>
'''

@app.route('/')
def portfolio():
    return render_template_string(html)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
