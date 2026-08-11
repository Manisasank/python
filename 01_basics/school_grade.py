def classify_score(score):
    if not isinstance(score, (int, float)):
        raise TypeError("score must be numeric")
    if score < 0 or score > 100:
        raise ValueError("score must be between 0 and 100")
    if score >= 90:
        return "Grade: A"
    elif score >= 75:
        return "Grade: B"
    elif score >= 50:
        return "Grade: C"
    else:
        return "Grade: F"
for s in [95, 72, 40]:
    print(classify_score(s))