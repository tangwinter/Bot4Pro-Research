from PIL import Image

# Remove white background from cyberport logo
img = Image.open(r'h:\My Drive\1. Admin\3. Logo   Name Card  Website\Bot4pro research\cyberport.jpeg')
img = img.convert('RGBA')
data = img.getdata()

new_data = []
for item in data:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save(r'h:\My Drive\1. Admin\3. Logo   Name Card  Website\Bot4pro research\cyberport_transparent.png', 'PNG')
print('Done - cyberport_transparent.png saved')
