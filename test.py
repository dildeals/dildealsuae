from pdf2image import convert_from_path

images = convert_from_path('Flyers/input.pdf', size=1500)

for i in range(len(images)):
    images[i].save(str(i+1) +'.webp', 'WEBP')

thumbs = convert_from_path('Flyers/input.pdf', size=750)

for i in range(len(thumbs)):
    thumbs[i].save(str(i+1) +'.thumb.webp', 'WEBP')
