import geometry

try:
    
    r = 5
    print(f"Area of circle with radius {r}: {geometry.area_circle(r):.2f}")

    l, w = 10, 4
    print(f"Area of rectangle {l}x{w}: {geometry.area_rectangle(l, w):.2f}")

except ValueError as e:
    print("Error:", e)
