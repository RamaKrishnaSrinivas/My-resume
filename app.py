from flask import Flask, render_template_string, request
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

combined_html = """
<!DOCTYPE html>
<html>
<head>
    <title>Even or Odd Checker and Register</title>
</head>
<body style="text-align: center; padding-top: 100px;">
    <h2>Check Even or Odd and Sum of Different Numbers</h2>
    <form method="post" action="/">
        <input type="number" name="number" placeholder="Enter a number" required>
        <br><br>
        <input type="number" name="a" placeholder="Enter number a" required>
        <br><br>
        <input type="number" name="b" placeholder="Enter number b" required>
        <br><br>
        <button type="submit" name="form_type" value="even_odd">Check</button>
    </form>

    {% if result is defined %}
        <h3>Result: {{ result }}</h3>
    {% endif %}

    {% if total is defined %}
        <h3>Sum: {{ total }}</h3>
    {% endif %}

    <hr>

    <h2>Register</h2>
    <form action="/" method="post">
        <input type="text" name="name" placeholder="Enter your name" required>
        <br><br>
        <input type="email" name="email" placeholder="Enter your email" required>
        <br><br>
        <input type="password" name="password" placeholder="Enter your password" required>
        <br><br>
        <button type="submit" name="form_type" value="register">Register</button>
    </form>

    {% if success_message is defined %}
        <h3 style="color: green;">{{ success_message }}</h3>
    {% endif %}

    {% if error_message is defined %}
        <h3 style="color: red;">{{ error_message }}</h3>
    {% endif %}

    <hr>

    <h2>Login</h2>
    <form action="/" method="post">
        <input type="email" name="email" placeholder="Enter your email" required>
        <br><br>
        <input type="password" name="password" placeholder="Enter your password" required>
        <br><br>
        <button type="submit" name="form_type" value="Login">Login</button>
    </form>
</body>
</html>
"""
dashboard_html="""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Rama Krishna Srinivas | Portfolio</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="bg-white text-gray-800 font-sans leading-relaxed p-6">
    <div class="max-w-4xl mx-auto space-y-10">
      <!-- Header -->
      <header class="text-center">
        <h1 class="text-4xl font-bold">ORUGANTI RAMA KRISHNA SRINIVAS</h1>
        <h2 class="text-xl text-gray-600 mt-2">Contact Information</h2>
        <p class="mt-1">
          📧 orugantirks@gmail.com | 📞 7997141652 | 🔗 LinkedIn: b84528306
        </p>
      </header>

      <!-- Summary -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Summary
        </h3>
        <p>
          Motivated and passionate Computer Science Engineering graduate from
          Siddharth Institute of Engineering and Technology, with a strong
          foundation in programming, web development, and database management.
          Actively engaged in personal projects and internships to enhance
          technical expertise. Seeking opportunities to contribute to innovative
          software development teams and continuously grow in the tech field.
        </p>
      </section>

      <!-- Education -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Education
        </h3>
        <div class="overflow-x-auto">
          <table class="min-w-full text-left border border-gray-300">
            <thead class="bg-gray-100 text-gray-700">
              <tr>
                <th class="px-4 py-2 border border-gray-300">Examination</th>
                <th class="px-4 py-2 border border-gray-300">Institution</th>
                <th class="px-4 py-2 border border-gray-300">Year</th>
                <th class="px-4 py-2 border border-gray-300">Score</th>
              </tr>
            </thead>
            <tbody>
              <tr class="hover:bg-gray-50">
                <td class="px-4 py-2 border border-gray-300">SSC</td>
                <td class="px-4 py-2 border border-gray-300">
                  Himaja English Medium School, Puttur, Andhra Pradesh
                </td>
                <td class="px-4 py-2 border border-gray-300">2020</td>
                <td class="px-4 py-2 border border-gray-300">99.8%</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-4 py-2 border border-gray-300">Intermediate</td>
                <td class="px-4 py-2 border border-gray-300">
                  Himaja Junior College, Puttur, Andhra Pradesh
                </td>
                <td class="px-4 py-2 border border-gray-300">2022</td>
                <td class="px-4 py-2 border border-gray-300">68.8%</td>
              </tr>
              <tr class="hover:bg-gray-50">
                <td class="px-4 py-2 border border-gray-300">B.Tech</td>
                <td class="px-4 py-2 border border-gray-300">
                  Siddharth Institute of Engineering and Technology, Puttur,
                  Andhra Pradesh
                </td>
                <td class="px-4 py-2 border border-gray-300">2026</td>
                <td class="px-4 py-2 border border-gray-300">7.0 CGPA</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- Skills -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Skills
        </h3>
        <div class="grid grid-cols-2 gap-4">
          <div>
            <h4 class="font-semibold">Programming Languages:</h4>
            <ul class="list-disc list-inside">
              <li>Python (Medium)</li>
              <li>Java (Basics)</li>
            </ul>
          </div>
             <div>
            <h4 class="font-semibold">Database:</h4>
            <ul class="list-disc list-inside">
              <li>SQL</li>
            </ul>
          </div>
          <div>
            <h4 class="font-semibold">Web Technologies:</h4>
            <ul class="list-disc list-inside">
              <li>HTML, CSS, JavaScript</li>
              <li>React JS (Basics)</li>
              <li>Tailwind CSS</li>
              <li>FLASK</li>
            </ul>
          </div>
        </div>
      </section>

      
      <!-- Projects -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Projects
        </h3>
        <ul class="list-disc list-inside">
        <li>
            <strong>Calculator:</strong> Created a basic calculator using HTML,
            CSS, and JavaScript.
          </li>
          <li>
            <strong>Registration Form:</strong> Built with HTML, THAILWIND CSS, and PYTHON(FLASK) for
            secure login and data handling.
          </li>
          <li>
            <strong>College Ranking System:</strong> Still on progress using HTML,THAILWIND CSS,
            JavaScript, and React JS (Basics), PYTHON(FLASK) for evaluating college domains like
            faculty, teaching, hostels, food, etc.
          </li>
        </ul>
      </section>

      <!-- Certifications -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Certifications
        </h3>
        <ul class="list-disc list-inside">
          <li>Joy of Computing Using Python – NPTEL</li>
          <li>Web Development Internship – Assistive Technologies, Tirupati</li>
          <li>Introduction to Aspects of Game Design – edX</li>
          <li>Aptitude, Java (Basics), MySQL – Q-Spiders</li>
        </ul>
      </section>

      <!-- Hobbies -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Hobbies
        </h3>
        <ul class="list-disc list-inside">
          <li>Learning something new</li>
          <li>Cooking</li>
          <li>Reading books (Education & Manga)</li>
          <li>Watching movies</li>
        </ul>
      </section>

      <!-- Personal Info -->
      <section>
        <h3 class="text-2xl font-semibold border-b-2 border-gray-300 pb-1 mb-3">
          Personal Information
        </h3>
        <ul class="list-disc list-inside">
          <li>Full Name: Oruganti Rama Krishna Srinivas</li>
          <li>Father's Name: Oruganti Sudhakar</li>
          <li>Phone: 7997141652</li>
          <li>LinkedIn: b84528306</li>
          <li>Email: orugantirks@gmail.com</li>
        </ul>
      </section>
      <!-- Footer -->
      <footer class="text-center mt-10 text-sm text-gray-500">
        &copy; 2025 Oruganti Rama Krishna Srinivas. All rights reserved.
      </footer>
    </div>
  </body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def combined_route():
    if request.method == 'POST':
        # Check which form was submitted
        form_type = request.form.get('form_type')

        if form_type == 'even_odd':
            # Process the "Even or Odd Checker" form
            a = int(request.form['a'])
            b = int(request.form['b'])
            number = int(request.form['number'])
            total = a + b
            result = f"{number} is Even" if number % 2 == 0 else f"{number} is Odd"
            return render_template_string(combined_html, total=total, result=result)

        elif form_type == 'register':
            # Process the "Registration" form
            name = request.form['name']
            email = request.form['email']
            password = request.form['password']

            # Hash the password
            hashed_password = generate_password_hash(password)

            # Save to database
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                )
            ''')
            # Check if email already exists
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            if c.fetchone():
                conn.close()
                error_message = "Email already registered!"
                return render_template_string(combined_html, error_message=error_message)

            # Insert new user
            c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, hashed_password))
            conn.commit()
            conn.close()

            success_message = f"User {name} registered successfully with email {email}."
            return render_template_string(combined_html, success_message=success_message)

        elif form_type == 'Login':
            # Process the "Login" form
            email = request.form['email']
            password = request.form['password']

            # Check credentials
            conn = sqlite3.connect('users.db')
            c = conn.cursor()
            c.execute('SELECT * FROM users WHERE email = ?', (email,))
            user = c.fetchone()
            conn.close()

            if user and check_password_hash(user[3], password):  # user[3] is the hashed password
                success_message = f"Welcome back, {user[1]}!"  # user[1] is the name
                return render_template_string(dashboard_html, success_message=success_message)
            else:
                error_message = "Invalid email or password!"
                return render_template_string(combined_html, error_message=error_message)

    # Render the combined form for GET requests
    return render_template_string(combined_html)
if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
