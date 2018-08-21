from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Test'}
    items = [
        {
            'type': 'Adapter',
            'size': 'pci-3',
            'description': '4 port 16GB FC'
        },
        {
            'type': 'Cable',
            'size': '10M',
            'description': '10M OM3 fibre cable'
        }
    ]
    return render_template('index.html', title='Inventory', user=user, items=items)
