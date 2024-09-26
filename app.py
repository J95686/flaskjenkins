from flask import Flask, render_template_string, request, redirect, url_for

app = Flask(__name__)

items = []

# HTML templates as strings
index_template = '''
<!doctype html>
<html lang="en">
    <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>Flask First Step</title>
        <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet" />
    </head>
    <body class="p-6">
        <div class="container mx-auto">
            <h1 class="text-2xl font-bold mb-4">Items</h1>
            <form method="POST" action="/add" class="mb-4">
                <input type="text" name="item" placeholder="Add new item" class="border p-2 mr-2" />
                <button type="submit" class="bg-blue-500 text-white p-2">Add</button>
            </form>
            <ul>
                {% for item in items %}
                <li class="mb-2">
                    {{ item }}
                    <a href="/edit/{{ loop.index0 }}" class="text-blue-500">Edit</a>
                    <a href="/delete/{{ loop.index0 }}" class="text-red-500">Delete</a>
                </li>
                {% endfor %}
            </ul>
        </div>
    </body>
</html>
'''

edit_template = '''
{% extends "base.html" %}
{% block content %}
<h1 class="text-2xl font-bold mb-4">Edit Item</h1>
<form method="POST" action="/edit/{{ item_id }}">
    <input type="text" name="item" value="{{ item }}" class="border p-2 mr-2" />
    <button type="submit" class="bg-blue-500 text-white p-2">Update</button>
</form>
{% endblock %}
'''

@app.route('/')
def index():
    return render_template_string(index_template, items=items)

@app.route('/add', methods=['POST'])
def add():
    item = request.form.get('item')
    if item:
        items.append(item)
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
def edit(item_id):
    if request.method == 'POST':
        item = request.form.get('item')
        items[item_id] = item
        return redirect(url_for('index'))
    return render_template_string(edit_template, item=items[item_id], item_id=item_id)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    items.pop(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
