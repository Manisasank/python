readings = [12.5, -3.2, 45.0, 0.0, -9.8, 30.1, 100.4]
# Keep only positive readings, rounded to 1 decimal
positive_readings = [round(r, 1) for r in readings if r > 0]
# Normalize readings into a 0-1 range in one comprehension
lo, hi = min(readings), max(readings)
normalized = [(r - lo) / (hi - lo) for r in readings]
print(positive_readings)
print(normalized)