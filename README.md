# JPEG_PNG Demo preview

* Upload and convert JPEG image to PNG image and download.
* Image linked with session.cookie.
* checking files with filetype.

![1](https://github.com/gconelhero/convert_image/assets/26088216/eabcd802-7f98-4b32-8392-3b07afb16878)

![2](https://github.com/gconelhero/convert_image/assets/26088216/08719b9a-5657-43ea-84a0-69cac62c0523)

![3](https://github.com/gconelhero/convert_image/assets/26088216/a283f9c6-43f6-459c-a782-8d446976e389)

Install and config JPEG_PNG demo:<br>
```python3 -m pip venv jpeg_png```<br>
```cd jpeg_png```<br>
```source bin/activate```<br>
```git clone https://github.com/gconelhero/jpeg_png```<br>
```cd jpeg_png```<br>
```python -m pip install -r requirements.txt```<br>
```python manage.py makemigrations insert_image```<br>
```python manage.py migrate```<br>
```python manage.py runserver```<br>
Browser address:
```localhost:8000/upload```<br>