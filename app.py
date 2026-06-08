import os
import pickle
import numpy as np
from flask import Flask, request, render_template_string

app = Flask(__name__)

# Load your trained KNN model
MODEL_PATH = 'KNN_HP.pkl'
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

# Beautiful UI Template using Tailwind CSS
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>House Price Predictor</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-slate-50 min-h-screen flex items-center justify-center p-4 antialiased text-slate-800 font-sans">

    <div class="w-full max-w-xl bg-white rounded-2xl shadow-xl border border-slate-100 overflow-hidden">
        <div class="bg-linear-to-r from-blue-600 to-indigo-700 p-6 text-center text-white">
            <h1 class="text-2xl font-bold tracking-tight">House Price Predictor</h1>
            <p class="text-blue-100 text-sm mt-1">Enter property metrics below to estimate the current market valuation.</p>
        </div>

        <form action="/predict" method="POST" class="p-6 space-y-5">
            <div class="grid grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Bedrooms</label>
                    <input type="number" step="1" name="beds" value="{{ beds if beds is not none else '3' }}" required
                        class="w-full px-3 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Bathrooms</label>
                    <input type="number" step="0.5" name="baths" value="{{ baths if baths is not none else '2' }}" required
                        class="w-full px-3 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
            </div>

            <div class="grid grid-cols-2 gap-4">
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Size (Sq Ft)</label>
                    <input type="number" step="any" name="size" value="{{ size if size is not none else '1500' }}" required
                        class="w-full px-3 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
                <div>
                    <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Lot Size (Sq Ft)</label>
                    <input type="number" step="any" name="lot_size" value="{{ lot_size if lot_size is not none else '5000' }}" required
                        class="w-full px-3 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
                </div>
            </div>

            <div>
                <label class="block text-xs font-semibold text-slate-600 uppercase tracking-wider mb-2">Zip Code</label>
                <input type="number" step="1" name="zip_code" value="{{ zip_code if zip_code is not none else '90210' }}" required
                    class="w-full px-3 py-2 border border-slate-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition">
            </div>

            <button type="submit" 
                class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 rounded-xl shadow-md transition duration-200 transform active:scale-98 cursor-pointer text-center">
                Calculate Valuation
            </button>
        </form>

        {% if prediction_text %}
        <div class="bg-emerald-50 border-t border-emerald-100 p-6 text-center">
            <p class="text-emerald-800 font-semibold text-xl tracking-tight">
                {{ prediction_text }}
            </p>
        </div>
        {% endif %}

        {% if error_text %}
        <div class="bg-rose-50 border-t border-rose-100 p-6 text-center">
            <p class="text-rose-700 font-medium text-sm">
                {{ error_text }}
            </p>
        </div>
        {% endif %}
    </div>

</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE, beds=None, baths=None, size=None, lot_size=None, zip_code=None)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features submitted from form fields
        beds = float(request.form.get('beds'))
        baths = float(request.form.get('baths'))
        size = float(request.form.get('size'))
        lot_size = float(request.form.get('lot_size'))
        zip_code = float(request.form.get('zip_code'))

        # Prepare the input features vector for your model [beds, baths, size, lot_size, zip_code]
        features = np.array([[beds, baths, size, lot_size, zip_code]])

        # Execute machine learning model inference
        prediction = model.predict(features)[0]
        predicted_price = f"${prediction:,.2f}"

        return render_template_string(
            HTML_TEMPLATE, 
            prediction_text=f'Estimated Valuation: {predicted_price}',
            beds=beds, baths=baths, size=size, lot_size=lot_size, zip_code=int(zip_code)
        )
    except Exception as e:
        return render_template_string(HTML_TEMPLATE, error_text=f"Error processing parameters: {str(e)}", beds=None, baths=None, size=None, lot_size=None, zip_code=None)

if __name__ == "__main__":
    # Render binds dynamic environment ports at deployment runtime
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
