import easyocr
from PIL import Image
class EasyOCR:
    def __init__(self):
        self.reader = easyocr.Reader(
            ['ch_sim','en'],
            gpu = False,
            # detect_network= 'craft',
            # download_enabled= False,
            # model_storage_directory= '/mnt/d/projectB/py/add/model/'
        )
        print('OCR loaded')
        pass

    def ocr(self, img_dir) -> str:
        try:
            # Check if the image is a gif            
            import requests
            from io import BytesIO

            response = requests.get(img_dir)
            img = Image.open(BytesIO(response.content))
            print(img.format)
            if img.format == 'GIF':
                print('GIF')
                return ''
            ocrinfo = self.reader.readtext(img_dir)
        except Exception as e:
            print('OCR ERROR',e)
            return ''

        result = ''
        for item in ocrinfo:
            result += item[1]
        # print('result = ', result)
        return result

if __name__ == '__main__':
    ocr = EasyOCR()
    print(ocr.ocr('https://mmbiz.qpic.cn/mmbiz_gif/qfMmVoEgEk2kx3AqqLcUG91NLNbR7Kzm79fQeZ1AUsFWPgttib9bpoSRu2dEXRTp7I25iaas2C3aoBmialVQ7kbRQ/640'))
    print(ocr.ocr('https://mmbiz.qpic.cn/mmbiz_jpg/xdXyG3icTG4aRNu79jMK6LqJxBeNnPd6D9XEjTDRYz6ibDAwvdKFUpiaTubxFngJljicfAgZFL8nL4OeYniaWGaDvKw/640?wx_fmt=jpeg'))
