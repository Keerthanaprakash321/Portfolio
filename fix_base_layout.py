
import os

with open(r'c:\Users\keert\Portfolio\templates\base_layout.html', 'w', encoding='utf-8') as f:
    f.write("""{% load static tailwind_tags %}
<!DOCTYPE html>
<html lang="en" class="scroll-smooth scroll-pt-20">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Portfolio | {% block title %}Home{% endblock %}</title>
    {% tailwind_css %}
    <style>
        :root {
            {% if request.session.theme == 'light' %}
            /* "Light" Mode: White Background, Dark Green Text (#003300) */
            --bg-primary: #FFFFFF;
            --bg-secondary: #F0FFF4;
            --text-primary: #003300;
            --text-secondary: #00AA00;
            --text-accent: #00AA00;
            --border-color: #00AA00;
            {% else %}
            /* Dark Mode: Black Background, VERY Dark Green Text (#003300) */
            --bg-primary: #000000;
            --bg-secondary: #003300;
            --text-primary: #00AA00;
            --text-secondary: #003300;
            --text-accent: #00AA00;
            --border-color: #003300;
            {% endif %}
        }
        
        /* Submit Button Styled as Toggle Switch */
        .theme-toggle-btn {
            position: relative;
            display: inline-block;
            width: 50px;
            height: 24px;
            background-color: #ccc;
            border-radius: 34px;
            border: none;
            cursor: pointer;
            transition: background-color 0.4s;
            vertical-align: middle;
            outline: none;
        }

        .theme-toggle-circle {
            position: absolute;
            height: 18px;
            width: 18px;
            left: 3px;
            bottom: 3px;
            background-color: white;
            border-radius: 50%;
            transition: transform 0.4s;
        }

        /* Light Mode State (Green, Right) */
        .theme-toggle-btn.light-mode {
            background-color: #68D391;
        }

        .theme-toggle-btn.light-mode .theme-toggle-circle {
            transform: translateX(26px);
        }
    </style>
</head>

<body class="bg-[var(--bg-primary)] text-[var(--text-primary)] font-sans leading-normal tracking-normal flex flex-col min-h-screen transition-colors duration-300">

    <!-- Navigation -->
    <nav class="bg-[var(--bg-primary)] shadow fixed w-full z-10 top-0 border-b border-[var(--border-color)] transition-colors duration-300">
        <div class="container mx-auto px-6 py-3 flex justify-between items-center">
            <a class="text-xl font-bold text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors" href="/">Keerthana Prakash</a>
            <div class="flex items-center space-x-4">
                <a href="#home" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">Home</a>
                <a href="#about" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">About</a>
                <a href="#projects" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">Projects</a>
                <a href="{% url 'contact' %}" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">Contact</a>
                
                <!-- Theme Toggle Form -->
                <form action="{% url 'toggle_theme' %}" method="post" class="inline-flex items-center ml-4">
                    {% csrf_token %}
                    <button type="submit" class="theme-toggle-btn {% if request.session.theme == 'light' %}light-mode{% endif %}" aria-label="Toggle Theme">
                        <span class="theme-toggle-circle"></span>
                    </button>
                    <span class="text-xs text-[var(--text-primary)] ml-2 cursor-default select-none">
                        {% if request.session.theme == 'light' %}Light{% else %}Dark{% endif %}
                    </span>
                </form>

                {% if user.is_authenticated and user.is_staff %}
                <a href="{% url 'dashboard' %}" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors ml-4">Dashboard</a>
                {% else %}
                <a href="#" class="text-[var(--text-primary)] opacity-60 cursor-not-allowed ml-4" title="Admin only" aria-disabled="true">Dashboard</a>
                {% endif %}
                <form action="{% url 'logout' %}" method="post" class="inline ml-2">
                    {% csrf_token %}
                    <button type="submit" class="text-red-500 hover:text-red-700 transition-colors">Logout</button>
                </form>
                {% else %}
                <a href="{% url 'login' %}" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors ml-4">Login</a>
                {% endif %}
            </div>
        </div>
    </nav>

    <!-- Main Content -->
    <main class="{% block main_class %}container mx-auto px-6 py-8 flex-grow mt-16{% endblock %}">
        {% if messages %}
        <div class="mb-6">
            {% for message in messages %}
            <div class="p-4 mb-4 text-sm text-white rounded-lg {% if message.tags == 'success' %}bg-green-500{% elif message.tags == 'error' %}bg-red-500{% else %}bg-blue-500{% endif %}"
                role="alert">
                <span class="font-medium">{{ message }}</span>
            </div>
            {% endfor %}
        </div>
        {% endif %}

        {% block content %}
        {% endblock %}
    </main>

    <!-- Footer -->
    <footer class="bg-[var(--bg-primary)] border-t border-[var(--border-color)] mt-auto transition-colors duration-300">
        <div class="container mx-auto px-6 py-4">
            <div class="flex justify-between items-center">
                <p class="text-[var(--text-primary)] text-sm">© {% now "Y" %} MyPortfolio. All rights reserved.</p>
                <div class="flex space-x-4">
                    <a href="https://github.com/Keerthanaprakash321" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors"
                        target="_blank">GitHub</a>
                    <a href="https://www.linkedin.com/in/KeerthanaPrakashKP" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors"
                        target="_blank">LinkedIn</a>
                    <a href="mailto:keerthana76666@gmail.com" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">Email</a>
                </div>
            </div>
        </div>
    </footer>

    <script src="{% static 'js/main.js' %}"></script>
</body>

</html>""")
print("Successfully overwrote base_layout.html")
