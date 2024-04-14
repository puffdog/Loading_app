from flask import Flask, request, render_template, Response

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/select_equipment', methods=['POST'])
def select_equipment():
    equipment_type = request.form['equipmentType']
    if equipment_type == 'container':
        return render_template('container_dimensions.html')
    elif equipment_type == 'truck':
        return render_template('truck_dimensions.html')
    else:
        return "Error: Equipment type not recognized.", 400

@app.route('/container_dimensions', methods=['POST'])
def container_dimensions():
    if request.method == 'POST':
        # Process form data for container dimensions
        return render_template('cargo_type.html')

@app.route('/truck_dimensions', methods=['POST'])
def truck_dimensions():
    if request.method == 'POST':
        # Process form data for truck dimensions
        return render_template('cargo_type.html')

@app.route('/cargo_type', methods=['POST'])
def cargo_type():
    if request.method == 'POST':
        # Process form data for cargo type
        return render_template('enter_cargo_data.html')

@app.route('/enter_cargo_data', methods=['POST'])
def enter_cargo_data():
    if request.method == 'POST':
        # Process form data for cargo data entry
        cargo_name = request.form.get('cargo_name')
        cargo_length = float(request.form.get('cargo_length'))
        cargo_width = float(request.form.get('cargo_width'))
        cargo_height = float(request.form.get('cargo_height'))
        cargo_weight = float(request.form.get('cargo_weight'))
        cargo_quantity = int(request.form.get('cargo_quantity'))
        
        # Calculate total volume and weight
        total_volume = cargo_length * cargo_width * cargo_height * cargo_quantity
        total_weight = cargo_weight * cargo_quantity

        return render_template('results.html', cargo_name=cargo_name, total_volume=total_volume, total_weight=total_weight)

@app.route('/export_results', methods=['POST'])
def export_results():
    # Example results data
    results = [
        {'name': 'Item 1', 'quantity': 5},
        {'name': 'Item 2', 'quantity': 10},
        {'name': 'Item 3', 'quantity': 8}
    ]

    # Generate CSV data
    csv_data = "Name,Quantity\n"
    for result in results:
        csv_data += f"{result['name']},{result['quantity']}\n"

    # Create response with CSV data
    response = Response(csv_data, mimetype='text/csv')
    response.headers['Content-Disposition'] = 'attachment; filename=results.csv'

    return response

if __name__ == '__main__':
    app.run(debug=True)
