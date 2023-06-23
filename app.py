from flask import Flask, render_template
# from app.data_loader import load_data
# from app.data_processing import process_data

app = Flask(__name__, template_folder='C:/Users/arnab/Downloads/Documents/template')


@app.route('/')
def home():
    return render_template("home.html")

@app.route('/index')
def index():
    return render_template('index.html')
# @app.route('/question', methods=['POST'])
# def question():
#     question_number= request.form['question-info']
#     subtitle = "Example Subtitle"  
    
#     return render_template('index.html', question_number=question_number, subtitle=subtitle)


@app.route('/index2')
def index2():
    return render_template('index2.html')

# @app.route('/')
# def index(): 
#     data = load_data()  # Call a function from your dataset app
#     processed_data = process_data(data)  # Call another function from your dataset app
#     # Perform further operations or return the processed data
#     return processed_data



if __name__ == "__main__":
    app.run(debug=True)
