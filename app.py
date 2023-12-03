from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Assume data.json contains your menu data
with open('data.json', 'r') as file:
    data = json.load(file)
    menu = data['menu']

@app.route('/')
def index():
    return render_template('index.html', menu=menu)

@app.route('/get_answer', methods=['POST'])
def get_answer():
    question_id = int(request.form['question_id'])
    
    # Find the selected option based on the question_id
    selected_option = None
    for main_option in menu:
        for sub_option in main_option.get('options', []):
            if sub_option['id'] == question_id:
                selected_option = sub_option
                break
            elif 'suboptions' in sub_option:
                for sub_sub_option in sub_option['suboptions']:
                    if sub_sub_option['id'] == question_id:
                        selected_option = sub_sub_option
                        break
                if selected_option:
                    break
        if selected_option:
            break
    
    # Check if the selected option is found
    if selected_option:
        answer = selected_option.get('answer', 'No answer found')
    else:
        answer = 'No answer found'

    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
