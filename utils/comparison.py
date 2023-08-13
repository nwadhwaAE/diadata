def calculate_divergence(actual_price, reference_price):
    return abs(reference_price - actual_price) / actual_price * 100

def highlight_divergence(divergence, threshold_percent):
    if divergence > threshold_percent:
        return f"Divergence: {divergence:.2f}%"
    else:
        return "No significant divergence"
