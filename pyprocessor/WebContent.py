# 2023/9/3


class WebContent:
    """
    WebContent is a type used to store content obtained from a webpage URL.
    """
    def __init__(self):
        self.title = ''
        self.author = ''
        self.publish_time = ''
        self.text = ''
        self.link = ''
        self.img_url = []
    
    def __str__(self):

        return f"WebContent(title={self.title}, author={self.author}, publish_time={self.publish_time}, link={self.link}, image_url={self.img_url[:2]}.......)"
