class Circle:
    def __init__(self, radius_list):
        self.radius_list = radius_list

    def calculate_area(self, radius):
        return 3.141 * radius ** 2

    def calculate_circumference(self, radius):
        return 2 * 3.141 * radius

    def calculate_all(self):
        results = []
        for radius in self.radius_list:
            area = self.calculate_area(radius)
            circumference = self.calculate_circumference(radius)
            results.append((radius, area, circumference))
        return results

# Example usage:
circle_instance = Circle([10, 501, 22, 37, 100, 999, 87, 351])

circle_data = circle_instance.calculate_all()
for radius, area, circumference in circle_data:
    print(f"Radius: {radius}, Area: {area:.2f}, Circumference: {circumference:.2f}")