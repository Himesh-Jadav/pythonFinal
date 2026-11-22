from timeconvert.converter import TimeConverter

try:
    converter = TimeConverter()
    time = input("Enter time (12-hour e.g. 02:30 PM or 24-hour e.g. 14:30): ")
    if "AM" in time.upper() or "PM" in time.upper():
        print("24-hour format:", converter.to_24(time.upper()))
    else:
        print("12-hour format:", converter.to_12(time))
except ValueError:
    print("Invalid time format.")
