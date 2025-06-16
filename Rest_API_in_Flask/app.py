from flask import Flask, render_template_string
import requests

app = Flask(__name__)

@app.route('/', methods=['GET'])
def fetch_users():
    api_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(api_url)

    if response.status_code == 200:
        users = response.json()
        # Strip email to show only the part before '@'
        for user in users:
            user["email_prefix"] = user["email"].split("@")[0]

        html = """
        <h2>User List (Name + Partial Email)</h2>
        <ul>
            {% for user in users %}
                <li><strong>{{ user.name }}</strong> ({{ user.email_prefix }}@...)</li>
            {% endfor %}
        </ul>
        """
        return render_template_string(html, users=users)
    else:
        return f"Failed to fetch users: {response.status_code}", 500

if __name__ == '__main__':
    app.run(debug=True)
