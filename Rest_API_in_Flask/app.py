from flask import Flask, jsonify, render_template_string
import requests

app = Flask(__name__)

# Route to call external REST API and show data
@app.route('/')
def fetch_users():
    api_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)

    if response.status_code == 200:
        users = response.json()
        # Display users in simple HTML
        html = """
        <h2>User List from External API</h2>
        <ul>
            {% for user in users %}
                <li><strong>{{ user.name }}</strong> ({{ user.email }})</li>
            {% endfor %}
        </ul>
        """
        return render_template_string(html, users=users)
    else:
        return f"Failed to fetch users: {response.status_code}", 500

if __name__ == '__main__':
    app.run(debug=True)
