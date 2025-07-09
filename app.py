from flask import Flask, render_template_string

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Poomalai B - Embedded Developer Portfolio</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body { padding: 30px; font-family: Arial, sans-serif; background-color: #f5f5f5; }
        .section { margin-bottom: 40px; }
        h1, h2 { color: #4b0082; }
        .card { margin-top: 10px; }
    </style>
</head>
<body>
    <div class="container">
        <h1 class="text-center">Poomalai B</h1>
        <p class="text-center">Embedded Developer | IoT | UI/UX | Arduino & Raspberry Pi</p>

        <div class="section">
            <h2>About Me</h2>
            <p>I have hands-on experience with electronics and small computers like Arduino and Raspberry Pi. 
               I can work with sensors, modules, and simple circuits. I also design basic PCBs using KiCad. 
               I enjoy building and testing projects and exploring how hardware works.</p>
        </div>

        <div class="section">
            <h2>Skills</h2>
            <ul>
                <li>Embedded C, Python, IoT</li>
                <li>PCB Design (KiCad, EasyEDA)</li>
                <li>Arduino, Raspberry Pi</li>
                <li>UI/UX Design (Figma, Canva)</li>
                <li>Tools: Proteus, MATLAB, ThingSpeak</li>
            </ul>
        </div>

        <div class="section">
            <h2>Education</h2>
            <ul>
                <li><strong>KSR Institute For Engineering And Technology</strong> (2022–2026) - CGPA: 7.5</li>
                <li><strong>HSC:</strong> Bharathi Matric Hr. Sec School (75%)</li>
                <li><strong>SSLC:</strong> Bharathi Matric Hr. Sec School (90%)</li>
            </ul>
        </div>

        <div class="section">
            <h2>Internships</h2>
            <ul>
                <li><strong>NoviTech R&D Pvt Ltd</strong> (May–Jun 2024) – IoT hardware, sensors, and communication</li>
                <li><strong>Rabbit QR</strong> (Jul 2024) – UI/UX design using Figma and Canva</li>
                <li><strong>Brainery Spot Technology</strong> (Jun 2025) – IoT projects with Arduino & Raspberry Pi</li>
            </ul>
        </div>

        <div class="section">
            <h2>Projects</h2>
            <div class="card p-3">
                <h5>Color Sorting Machine</h5>
                <p>Used Raspberry Pi Zero W with a camera to detect object colors and sort them with servo motors.</p>
            </div>
            <div class="card p-3">
                <h5>Gas Leakage Detection System</h5>
                <p>Built with Arduino Uno and gas sensor to alert gas leaks using buzzer and LEDs.</p>
            </div>
            <div class="card p-3">
                <h5>Mobile App UI/UX Design</h5>
                <p>Designed intuitive app layouts using Figma for a clean and responsive user experience.</p>
            </div>
        </div>

        <div class="section">
            <h2>Certifications</h2>
            <ul>
                <li>Introduction to IoT - NPTEL</li>
                <li>Arduino vs Raspberry Pi - Great Learning</li>
                <li>Wiring Harness Workshop - KSRIET</li>
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
    app.run(debug=True)
