import requests #this is a library that allows us to send HTTP requests using Python. It is a popular library for making API calls and handling web requests.
import os 
from PIL import Image  # pil(Pillow Library .this is a library for opening, manipulating, and saving many different image file formats. It is commonly used for image processing tasks in Python.
from IPython.display import IFrame, display #this is a function from the IPython.display module that allows you to display an HTML iframe in a Jupyter Notebook. It is often used to embed external web content, such as videos or interactive widgets, directly within the notebook.


url = 'https://www.ibm.com/'
url2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/IDSNlogo.png'#non-text data (image)


r = requests.get(url)
r2 = requests.get(url2)

print(r.status_code)  # 200 means success
print(r.text[:500])   # print first 500 chars of the HTML response
print(r.request.headers) # print the headers sent in the request.This returns a python dictionary containing the headers that were included in the HTTP request sent to the server. Headers are key-value pairs that provide additional information about the request, such as the user agent, content type, and other metadata.


#output for the second URL (image)
print(r2.status_code)  # 200 means success
print(r2.headers['Content-Type']) # print the content type of the response. This returns the value of the 'Content-Type' header from the HTTP response. The 'Content-Type' header indicates the media type of the resource being returned by the server, such as 'text/html' for HTML documents or 'image/png' for PNG images.


#save the image to a file and display it
path=os.path.join(os.getcwd(),'image.png')
with open(path,'wb') as f:
    f.write(r2.content) # write the content of the response to a file. This saves the image data retrieved from the URL to a file named 'image.png' in the current working directory. The 'wb' mode indicates that the file is opened for writing in binary mode, which is necessary for handling image data correctly.
image = Image.open(path) # open the image file using the PIL library. This loads the image from the specified path into memory, allowing you to manipulate or display it using the PIL library's functions.
display(image) # display the image in a Jupyter Notebook. This function is used to render    