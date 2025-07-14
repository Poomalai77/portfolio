from flask import Flask, render_template_string

app = Flask(__name__)

# Portfolio data structure
portfolio_data = {
    "name": "Poomalai B",
    "title": "IoT & Embedded Systems Engineer",
    "contact": {
        "email": "poomalairaja33@gmail.com",
        "phone": "+91 9159842429",
        "linkedin": "linkedin.com/in/poomalai-b-00778a262"
    },
    "about": "Electronics enthusiast specializing in Raspberry Pi and Arduino projects with hands-on experience in PCB design and IoT systems.",
    
    "projects": [
        {
            "title": "Color Sorting Machine",
            "tech": ["Raspberry Pi Zero W", "OpenCV", "Servo Motors"],
            "description": "Developed a computer vision system that sorts objects by color with 95% accuracy."
        },
        {
            "title": "Gas Leakage Detection",
            "tech": ["Arduino Uno", "MQ-2 Sensor", "Buzzer Alert"],
            "description": "Safety system that detects hazardous gases and triggers visual/audio alarms."
        }
    ],
    
    "skills": {
        "Programming": ["Python", "Embedded C"],
        "Hardware": ["Raspberry Pi", "Arduino", "Sensor Integration"],
        "Design": ["KiCad PCB Design", "Figma UI/UX"]
    },
    
    "education": [
        {
            "degree": "Electronics And Communication Engineering",
            "institution": "KSR Institute For Engineering And Technology",
            "year": "2022-2026",
            "score": "7.5 CGPA"
        }
    ],
    
    "certifications": [
        "NPTEL: Introduction to IoT",
        "Great Learning: Arduino vs Raspberry Pi"
    ]
}

# HTML template as a string
html_template = '''
<!DOCTYPE html>
<html>
<head>
    <title>{{ data.name }} - Portfolio</title>
    <style>
        body { font-family: 'Segoe UI', sans-serif; max-width: 800px; margin: auto; padding: 20px; background-color: #f4f6f8; color: #2c3e50; }
        header { text-align: center; margin-bottom: 30px; }
        h1 { color: #2c3e50; }
        h2 { color: #3498db; border-bottom: 2px solid #3498db; padding-bottom: 5px; }
        .project { background: #ffffff; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .skills-list { display: flex; flex-wrap: wrap; gap: 15px; }
        .skill-category { flex: 1; min-width: 200px; background: #ffffff; padding: 10px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        ul { padding-left: 20px; }
        section { margin-bottom: 30px; }
        footer { text-align: center; font-size: 14px; color: #888; margin-top: 30px; }
    </style>
</head>
<body>
    <header>
        <h1>{{ data.name }}</h1>
        <h3>{{ data.title }}</h3>
        <p>{{ data.contact.email }} | {{ data.contact.phone }} | {{ data.contact.linkedin }}</p>
    </header>

    <section>
        <h2>About Me</h2>
        <p>{{ data.about }}</p>
    </section>

    <section>
        <h2>Projects</h2>
        {% for project in data.projects %}
        <div class="project">
            <h3>{{ project.title }}</h3>
            <p><strong>Technologies:</strong> {{ ", ".join(project.tech) }}</p>
            <p>{{ project.description }}</p>
        </div>
        {% endfor %}
    </section>

    <section>
        <h2>Skills</h2>
        <div class="skills-list">
            {% for category, skills in data.skills.items() %}
            <div class="skill-category">
                <h3>{{ category }}</h3>
                <ul>
                    {% for skill in skills %}
                    <li>{{ skill }}</li>
                    {% endfor %}
                </ul>
            </div>
            {% endfor %}
        </div>
    </section>

    <section>
        <h2>Education</h2>
        {% for edu in data.education %}
        <p>
            <strong>{{ edu.degree }}</strong><br>
            {{ edu.institution }} ({{ edu.year }})<br>
            <em>{{ edu.score }}</em>
        </p>
        {% endfor %}
    </section>

    <section>
        <h2>Certifications</h2>
        <ul>
            {% for cert in data.certifications %}
            <li>{{ cert }}</li>
            {% endfor %}
        </ul>
    </section>

    <footer>
        &copy; {{ data.name }} | Portfolio built with Flask
    </footer>
</body>
</html>
'''

@app.route('/')
def portfolio():
    return render_template_string(html_template, data=portfolio_data)

if __name__ == '__main__':
    app.run(debug=True)
