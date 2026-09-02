from PIL import Image

img = Image.open(r'h:\My Drive\1. Admin\3. Logo   Name Card  Website\Bot4pro research\WhatsApp Image 2026-08-28 at 10.13.39 PM.jpeg')
img = img.convert('RGBA')
data = img.getdata()

new_data = []
for item in data:
    if item[0] > 240 and item[1] > 240 and item[2] > 240:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save(r'h:\My Drive\1. Admin\3. Logo   Name Card  Website\Bot4pro research\logo_transparent.png', 'PNG')
print('Done - logo_transparent.png saved')
