from PIL import Image

path = "C:\\Users\\User\\e_desktop\\memes\\progr\\unsafe.png"
chars = " .:-=+*#%@"
width = 70


print(f"image path: {path}, width: {width}, \nchars: {chars}\n\n")
_ = Image.open(path)
_ = _.resize((width, int((_.size[1] / _.size[0]) * width))).convert("L")
n = [chars[int(pix / (256 / len(chars)))] for pix in list(_.getdata())]
chars = "".join(n)
print("\n".join([chars[index: index + width] for index in range(0, len(chars), width)]))
