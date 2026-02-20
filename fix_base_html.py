
import os

with open(r'c:\Users\keert\Portfolio\templates\base.html', 'w', encoding='utf-8') as f:
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
            /* "Light" Mode: Dark Green Background, White Text */
            --bg-primary: #003300;
            --bg-secondary: #001a00;
            --text-primary: #FFFFFF;
            --text-secondary: #00AA00;
            --text-accent: #00AA00;
            --border-color: #00AA00;
            {% else %}
            /* Dark Mode: Black Background, Green Text */
            --bg-primary: #000000;
            --bg-secondary: #003300;
            --text-primary: #00AA00;
            --text-secondary: #003300;
            --text-accent: #003300;
            --border-color: #003300;
            {% endif %}
        }
        
        /* Toggle Switch Styles */
        .toggle-checkbox:checked {
            right: 0;
            border-color: #68D391;
        }
        .toggle-checkbox:checked + .toggle-label {
            background-color: #68D391;
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
                
                <!-- Theme Toggle -->
                <form action="{% url 'toggle_theme' %}" method="post" class="inline-flex items-center">
                    {% csrf_token %}
                    <button type="submit" class="relative inline-block w-10 mr-2 align-middle select-none transition duration-200 ease-in">
                        <input type="checkbox" name="toggle" id="toggle" class="toggle-checkbox absolute block w-6 h-6 rounded-full bg-white border-4 appearance-none cursor-pointer border-gray-300 transition-all duration-300 ease-in-out" {% if request.session.theme == 'light' %}checked{% endif %} style="pointer-events: none; {% if request.session.theme == 'light' %}right: 0; border-color: #68D391;{% else %}left: 0;{% endif %}"/>
                        <label for="toggle" class="toggle-label block overflow-hidden h-6 rounded-full bg-gray-300 cursor-pointer transition-colors duration-300 ease-in-out {% if request.session.theme == 'light' %}bg-green-400{% endif %}"></label>
                    </button>
                    <label for="toggle" class="text-xs text-[var(--text-primary)] cursor-pointer">
                        {% if request.session.theme == 'light' %}Light{% else %}Dark{% endif %}
                    </label>
                </form>

                {% if user.is_authenticated %}
                <a href="{% url 'dashboard' %}" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">Dashboard</a>
                <form action="{% url 'logout' %}" method="post" class="inline">
                    {% csrf_token %}
                    <button type="submit" class="text-red-500 hover:text-red-700 transition-colors">Logout</button>
                </form>
                {% else %}
                <a href="{% url 'login' %}" class="text-[var(--text-primary)] hover:text-[var(--text-accent)] transition-colors">Login</a>
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
print("Successfully overwrote base.html")
