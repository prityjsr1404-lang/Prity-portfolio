from flask import Flask, render_template

app = Flask(__name__)

# Aapka Resume Data
RESUME_DATA = {
    "name": "Prity Kumari",
    "role": "Python & Web Developer",
    "email": "prity14102004@gmail.com",
    "phone": "9508994032",
    "linkedin": "https://www.linkedin.com/in/prity-kumari-986356296",
    "github": "https://github.com/prityjsr1404-lang",
    "summary": "BCA graduate with 9.55/10 CGPA and professional experience in software and web development. Strong foundation in Python, Java, C/C++, SQL, OOP, DSA, and Database Management. Hands-on experience in Python Flask, .NET, C#, JavaScript, and SQL Server. Strong analytical, problem-solving, and communication skills.",
    
    "experience": [
        {
            "role": "Python Developer",
            "company": "Paul Tech Software Services Pvt. Ltd.",
            "duration": "May 2025 - Present",
            "points": [
                "Develop and maintain web-based applications using Python, HTML, CSS, JavaScript, and databases.",
                "Build responsive and user-friendly interfaces with emphasis on cross-browser compatibility.",
                "Integrate application components with databases and support efficient data storage/retrieval.",
                "Troubleshoot, debug, test, and enhance application functionality."
            ]
        },
        {
            "role": "Web Developer Intern",
            "company": "Generix Info Tech Pvt. Ltd.",
            "duration": "Mar 2025 - May 2025",
            "points": [
                "Developed responsive web pages using HTML, CSS, JavaScript, and Bootstrap.",
                "Applied UI/UX and responsive design principles to create accessible interfaces.",
                "Gained practical exposure to front-end development and back-end technologies.",
                "Participated in testing, debugging, and improving website functionality."
            ]
        }
    ],
    
       "projects": [
        {
            "title": "NICT Website (Full-Stack)",
            "tech": "Python (Flask), SQLite, SQLAlchemy, Flask-Login, HTML, CSS, JS",
            "desc": "Designed and developed a complete professional website for a computer training institute. Implemented dynamic course pages, faculty profiles, and a secure database-driven Admin Dashboard for staff to view and manage student admission enquiries.",
            "github": "https://github.com/prityjsr1404-lang/nict-website" # Apna sahi link yahan daalein
        },
        {
            "title": "Online Vehicle Service Management System",
            "tech": "Python, Flask, HTML, CSS, JavaScript, SQL Server",
            "desc": "Developed a web-based vehicle service management application to digitize service activities. Implemented SQL Server database connectivity for organized storage and retrieval of vehicle and service information.",
            "github": "#"
        },
        {
            "title": "Class Management System",
            "tech": "C#, .NET, SQL Server, Visual Studio 2022",
            "desc": "Developed a centralized platform for faculty, courses, attendance, grades, and fee management. Applied Object-Oriented Programming concepts using C# and .NET.",
            "github": "#"
        }
    ],
    
    "skills": {
        "Programming": ["Python", "Java", "C", "C++", "C#"],
        "Web Technologies": ["HTML", "CSS", "JavaScript", "Bootstrap", "Flask", "ASP.NET", ".NET"],
        "Database & Tools": ["SQL", "SQL Server", "Git", "Visual Studio", "VS Code"],
        "Core Concepts": ["OOP", "Data Structures & Algorithms", "DBMS"]
    },
    
    "education": [
        {
            "degree": "Bachelor of Computer Applications (BCA)",
            "institute": "Jamshedpur Women's University",
            "year": "2022 - 2025",
            "score": "CGPA: 9.55/10"
        },
        {
            "degree": "Intermediate",
            "institute": "Jamshedpur Women's College",
            "year": "2020 - 2022",
            "score": "Percentage: 70%"
        }
    ],
    
    "certifications": [
        "Web Designing & Web Development",
        "Data Visualisation: Empowering Business with Effective Insights (TATA)",
        "GenAI Powered Data Analytics Job Simulation (TATA)"
    ]
}

@app.route('/')
def home():
    return render_template('index.html', data=RESUME_DATA)

if __name__ == '__main__':
    app.run(debug=True)