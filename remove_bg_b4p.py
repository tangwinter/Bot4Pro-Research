from PIL import Image

img = Image.open(r'h:\My Drive\1. Admin\3. Logo   Name Card  Website\Bot4pro research\B4Pword.png')
img = img.convert('RGBA')
data = img.getdata()

new_data = []
for item in data:
    # Remove gray/light background
    if item[0] > 180 and item[1] > 180 and item[2] > 180:
        new_data.append((255, 255, 255, 0))
    else:
        new_data.append(item)

img.putdata(new_data)
img.save(r'h:\My Drive\1. Admin\3. Logo   Name Card  Website\Bot4pro research\B4Pword.png', 'PNG')
print('Done - B4Pword.png background removed')
