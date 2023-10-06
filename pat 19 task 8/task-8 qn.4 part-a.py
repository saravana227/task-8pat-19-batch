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

my_tv = TV("Panasonic", 32, 499.99)

print(my_tv.status())  # Output: "Panasonic at channel 1, volume 50"

my_tv.increase_volume()
print(my_tv.status())  # Output: "Panasonic at channel 1, volume 51"

my_tv.set_channel(8)
print(my_tv.status())  # Output: "Panasonic at channel 8, volume 51"

my_tv.decrease_volume()
print(my_tv.status())  # Output: "Panasonic at channel 8, volume 50"

my_tv.reset()
print(my_tv.status())  # Output: "Panasonic at channel 1, volume 50"