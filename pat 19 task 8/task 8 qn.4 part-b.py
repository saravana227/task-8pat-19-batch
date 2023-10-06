class TV:
    def __init__(self, brand, inches, price):
        self.brand = brand
        self.channel = 1  # Default channel is 1
        self.price = price
        self.inches = inches
        self.on = False  # TV is initially turned off
        self.volume = 50  # Default volume is 50

    def increase_volume(self):
        if self.volume < 100:
            self.volume += 1

    def decrease_volume(self):
        if self.volume > 0:
            self.volume -= 1

    def set_channel(self, channel):
        if 1 <= channel <= 50:  # TV has 50 channels
            self.channel = channel

    def reset(self):
        self.channel = 1
        self.volume = 50

    def status(self):
        status_str = f"{self.brand} at channel {self.channel}, volume {self.volume}"
        return status_str
class SmartTV(TV):
    def __init__(self, brand, inches, price, screen_thickness, energy_usage, lifespan, refresh_rate):
        super().__init__(brand, inches, price)
        self.screen_thickness = screen_thickness
        self.energy_usage = energy_usage
        self.lifespan = lifespan
        self.refresh_rate = refresh_rate

        # Additional properties for SmartTV
        self.viewing_angle = "Wide-angle"  # Default viewing angle
        self.backlight = "LED"  # Default backlight type

    def display_details(self):
        details = f"Brand: {self.brand}\nInches: {self.inches} inches\nPrice: ${self.price}\nScreen Thickness: {self.screen_thickness} mm\nEnergy Usage: {self.energy_usage} W\nLifespan: {self.lifespan} years\nRefresh Rate: {self.refresh_rate} Hz\nViewing Angle: {self.viewing_angle}\nBacklight: {self.backlight}\nChannel: {self.channel}\nVolume: {self.volume}"
        return details

smart_tv = SmartTV("Samsung", 55, 799.99, 10, "100W", 5, 120)

print(smart_tv.status())  # Output: "Samsung at channel 1, volume 50"
print(smart_tv.display_details())