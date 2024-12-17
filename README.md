# โปรแกรมเว็บครอว์เลอร์ (Web Crawler Application) 🌐
โปรแกรมนี้เป็นเครื่องมือสำหรับดึงลิงก์ทั้งหมดจากเว็บไซต์ที่ระบุ พัฒนาด้วย Python และ PyQt6 ผู้ใช้สามารถป้อน URL และดูผลลัพธ์ลิงก์ที่ดึงออกมาได้อย่างง่ายดาย

## คุณสมบัติหลัก 🛠️
ป้อน URL: ป้อนลิงก์เว็บไซต์ที่ต้องการ
ดึงลิงก์ทั้งหมด: โปรแกรมจะดึงข้อมูลลิงก์ที่พบในเว็บเพจที่ระบุ
แสดงผลลัพธ์: แสดงลิงก์ทั้งหมดในหน้าต่างผลลัพธ์
## เทคโนโลยีที่ใช้ 💻
- Python 3.x
- PyQt6: ใช้ในการสร้างอินเทอร์เฟซ (GUI)
- Requests: ใช้สำหรับดึงข้อมูลจากเว็บไซต์
- BeautifulSoup4: ใช้สำหรับการประมวลผล HTML
## วิธีติดตั้งและใช้งาน ⚙️
### 1. ติดตั้ง Python
ดาวน์โหลดและติดตั้ง Python เวอร์ชัน 3.6 ขึ้นไปจาก python.org
ระหว่างการติดตั้ง เลือก "Add Python to PATH"

### 2. ติดตั้งไลบรารีที่จำเป็น
ใช้คำสั่งนี้ใน Terminal หรือ Command Prompt เพื่อดาวน์โหลดไลบรารีที่ต้องการ:


pip install PyQt6 requests beautifulsoup4
### 3. รันโปรแกรม
บันทึกโค้ดในไฟล์ชื่อ web_crawler.py และรันโปรแกรมด้วยคำสั่ง:

python web_crawler.py

## การใช้งานโปรแกรม 🚀
 1. ป้อน URL ของเว็บไซต์ที่ต้องการดึงลิงก์ (เช่น https://example.com)
 2. คลิกปุ่ม "crawl"
 3. โปรแกรมจะแสดงลิงก์ทั้งหมดที่พบในช่องผลลัพธ์
 
## ข้อแนะนำ 🔍
ตรวจสอบให้แน่ใจว่า URL ที่ป้อนไม่มีปัญหาและสามารถเข้าถึงได้
ใช้โปรแกรมนี้เพื่อการศึกษาและไม่รบกวนเว็บไซต์อื่น



# Web Crawler Application 🌐
This application is a simple web crawler that extracts all hyperlinks from a given URL. Built using Python and PyQt6, it allows users to input a website URL and view the extracted links in an intuitive interface.

## Features 🛠️
Input URL: Enter a valid website URL
Extract Links: Fetch and display all hyperlinks found on the specified webpage
Display Results: View the extracted links in a clean text area
## Technologies Used 💻
- Python 3.x
- PyQt6: For GUI development
- Requests: For HTTP requests
- BeautifulSoup4: For HTML parsing
## Installation and Usage ⚙️
### 1. Install Python
Download and install Python version 3.6 or higher from python.org.
Make sure to add Python to PATH during installation.

### 2. Install Required Libraries
Run the following command in Terminal or Command Prompt to install dependencies:

pip install PyQt6 requests beautifulsoup4

### 3. Run the Application
Save the code as web_crawler.py and run it using:

python web_crawler.py

## How to Use 🚀
- Enter a website URL (e.g., https://example.com)
- Click the "crawl" button
- View all extracted links in the result area


## Notes 🔍
Ensure the URL is valid and accessible.
Use this application responsibly and avoid overloading websites.

##
Developer 👨‍💻
Kanyarat Thammachot
© 2024