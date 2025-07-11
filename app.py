from flask import Flask, request, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import os

app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def screenshot():
    try:
        url = request.args.get('url')
        width = int(request.args.get('width', 1280))
        height = int(request.args.get('height', 2400))

        if not url:
            return "URL parameter is required", 400

        chrome_options = Options()
        chrome_options.add_argument("--headless=new")  # chrome headless mode terbaru
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument(f"--window-size={width},{height}")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--single-process")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--disable-software-rasterizer")

        driver = webdriver.Chrome(service=Service("/usr/bin/chromedriver"), options=chrome_options)
        driver.get(url)
        time.sleep(3)

        path = 'screenshot.png'
        driver.save_screenshot(path)
        driver.quit()

        return send_file(path, mimetype='image/png')
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
