from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados temporários
members = []
schedules = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_member', methods=['GET', 'POST'])
def add_member():
    if request.method == 'POST':
        name = request.form['name']
        role = request.form['role']
        instrument = request.form.get('instrument', '')
        members.append({'name': name, 'role': role, 'instrument': instrument})
        return redirect(url_for('add_member'))
    return render_template('add_member.html', members=members)

@app.route('/generate_schedule')
def generate_schedule():
    return render_template('schedule.html', schedule={})

@app.route('/search_music', methods=['GET'])
def search_music():
    query = request.args.get('query', '')
    if query:
        return redirect(f'https://www.cifraclub.com.br/?q={query}')
    return render_template('search_music.html')

if __name__ == '__main__':
    app.run(debug=True)
