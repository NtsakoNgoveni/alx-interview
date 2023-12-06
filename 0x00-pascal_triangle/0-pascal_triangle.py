def pascal_triangle(n):
    # Check if n is less than or equal to 0
    if n <= 0:
        return []

    # Initialize the triangle with the first row
    triangle = [[1]]

    # Generate the subsequent rows using zip
    for _ in range(1, n):
        # Use zip to combine the current row and its shifted version
        row = [1] + [a + b for a, b in zip(triangle[-1], triangle[-1][1:])] + [1]
        triangle.append(row)

    return triangle
