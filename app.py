from flask import Flask, request, send_file
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

app = Flask(__name__)

@app.route('/screenshot', methods=['GET'])
def screenshot():
    url = request.args.get('url')
    width = int(request.args.get('width', 1280))
    height = int(request.args.get('height', 2400))

    if not url:
        return "URL parameter is required", 400

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(f"--window-size={width},{height}")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(url)
    time.sleep(3)

    path = 'screenshot.png'
    driver.save_screenshot(path)
    driver.quit()

    return send_file(path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
