import requests
url = "https://httpbin.org/image/jpeg"
response = requests.get(url)
# print(response)
# print(type(response))
# print(response.status_code)
binary_img = response.content # бинарное значение
with open("test_img.jpg", "wb") as file:# w - write, b - binary
    file.write(binary_img)