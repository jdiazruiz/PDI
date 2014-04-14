# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import PIL.Image
import dicom
import ImageFilter
from dicom.contrib.pydicom_PIL import show_PIL
dataset = dicom.read_file("C:\\vid.dcm")
frame=6
def getframe(frameSize,frame,dataset):
  data=dataset.PixelData[frame*frameSize:(frame+1)*frameSize]
  return data    

if ('WindowWidth' not in dataset) or ('WindowCenter' not in dataset):  # can only apply LUT if these values exist
        bits = dataset.BitsAllocated
        samples = dataset.SamplesPerPixel
        if bits == 8 and samples == 1:
            mode = "L"
        elif bits == 8 and samples == 3:
            mode = "RGB"
        elif bits == 16:
            mode = "I;16"  # not sure about this -- PIL source says is 'experimental' and no documentation. Also, should bytes swap depending on endian of file and system??
        else:
            raise TypeError("Don't know PIL mode for %d BitsAllocated and %d SamplesPerPixel" % (bits, samples))
        size = (dataset.Columns, dataset.Rows)
        ROWS=dataset.Rows
        COLUMNS=dataset.Columns
        SAMPLES_PER_PIXEL=dataset.SamplesPerPixel
        frameSize = ROWS*COLUMNS*SAMPLES_PER_PIXEL
        salida=getframe(frameSize,frame,dataset)
        im = PIL.Image.frombuffer(mode, size, salida, "raw", mode, 0, 1)  # Recommended to specify all details by http://www.pythonware.com/library/pil/handbook/image.htm

else:
        image = get_LUT_value(dataset.pixel_array, dataset.WindowWidth, dataset.WindowCenter)
        im = PIL.Image.fromarray(image).convert('L')  # Convert mode to L since LUT has only 256 values: http://www.pythonware.com/library/pil/handbook/image.htm
im1 = im.filter(ImageFilter.CONTOUR)
        
im.show()

        

# <codecell>


# <codecell>


