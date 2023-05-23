import os

if os.name=="nt":
    base_url="http://127.0.0.1:8000/"
elif os.name=="posix":
    base_url="http://127.0.0.1:8000/"#可調整成自己提供的網站網域例www.example.com