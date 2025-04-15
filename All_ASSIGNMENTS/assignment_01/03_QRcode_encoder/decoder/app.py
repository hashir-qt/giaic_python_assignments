import qrcode # type: ignore

data = 'SSSSUUUIIIII'

img = qrcode.make(data)

img.save('D:\Q3-Python\giaic_python_assignments_1-6\myqrcode.png')