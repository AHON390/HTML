from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def bmi_calculator():
    bmi = None
    category = ""
    
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            height = float(request.form.get('height')) / 100  # Convert cm to meters
            
            # BMI Formula: weight / height squared
            bmi = round(weight / (height ** 2), 2)
            
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
        except (TypeError, ValueError):
            category = "Please enter valid numbers!"

    return render_template('index.html', bmi=bmi, category=category)

if __name__ == '__main__':
    app.run(debug=True)
