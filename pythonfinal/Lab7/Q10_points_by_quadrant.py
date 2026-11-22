points = [(2, 3), (-2, 4), (-3, -1), (4, -5), (0, 2)]
quadrants = {
    'Q1': [p for p in points if p[0] > 0 and p[1] > 0],
    'Q2': [p for p in points if p[0] < 0 and p[1] > 0],
    'Q3': [p for p in points if p[0] < 0 and p[1] < 0],
    'Q4': [p for p in points if p[0] > 0 and p[1] < 0],
    'Axis': [p for p in points if p[0] == 0 or p[1] == 0]
}
print(quadrants)
