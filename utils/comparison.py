# Function to calculate divergence percentage between two prices
def calculate_divergence(actual_price, reference_price):
    return abs(reference_price - actual_price) / actual_price * 100

# Function to highlight divergence based on a threshold percentage
def highlight_divergence(divergence, threshold_percent):
    if divergence > threshold_percent:
        return f"Divergence: {divergence:.2f}%"
    else:
        return "No significant divergence"