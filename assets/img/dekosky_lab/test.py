

from PIL import Image
import os

dir = 'polaroids'

for filename in os.listdir(dir):
  print(filename)
  name = 'polaroids/' + filename
  image = Image.open(name)

  # next 3 lines strip exif
  data = list(image.getdata())
  imageNew = Image.new(image.mode, image.size)
  imageNew.putdata(data)
  imageNew = imageNew.rotate(270, expand=True)
    
  imageNew.save(name)

  imageNew.close()
