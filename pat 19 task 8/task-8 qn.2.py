class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list
        self._pi = 3.141

    def calculate_area(self, radius):
        return self._pi * radius ** 2

    def calculate_circumference(self, radius):
        return 2 * self._pi * radius

    def calculate_all(self):
        results = []
        for radius in self.radius_list:
            area = self.calculate_area(radius)
            circumference = self.calculate_circumference(radius)
            results.append((radius, area, circumference))
        return results

circle_instance = Circle([19, 51, 29, 67, 10, 99, 87, 35])

circle_data = circle_instance.calculate_all()
for radius, area, circumference in circle_data:
    print(f"Radius: {radius}, Area: {area:.2f}, Circumference: {circumference:.2f}")