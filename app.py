from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

items = []

@app.route('/')
def index():
    return render_template('index.html', items=items)

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
    return render_template('edit.html', item=items[item_id], item_id=item_id)

@app.route('/delete/<int:item_id>')
def delete(item_id):
    items.pop(item_id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
