class Font:
    def __init__(self, style):
        self.style = style

class FontsFactory:
    fonts = {}

    @classmethod
    def get_font(cls, style):
        if style not in cls.fonts:
            cls.fonts[style] = Font(style)
        return cls.fonts[style]

if __name__ == '__main__':
    FontsFactory()
    font1 = FontsFactory.get_font('Arial')
    font2 = FontsFactory.get_font('Arial')
    font3 = FontsFactory.get_font('Roboto')
    print(font1 is font2)
    print(font1 is font3)