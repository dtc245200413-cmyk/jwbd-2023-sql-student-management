import os
import shutil
import subprocess
import tempfile

svg_content = """<svg width="1280" height="820" viewBox="0 0 1280 820" xmlns="http://www.w3.org/2000/svg" style="background:#ffffff; border-radius: 12px;">
  <defs>
    <filter id="shadow" x="-8%" y="-8%" width="120%" height="120%">
      <feDropShadow dx="2" dy="4" stdDeviation="4" flood-color="#0f172a" flood-opacity="0.08" />
    </filter>
  </defs>

  <style>
    .tbl-title { font-size: 14px; font-weight: 800; fill: #ffffff; }
    .col-pk { font-size: 12px; font-weight: 800; fill: #b91c1c; }
    .col-fk { font-size: 12px; font-weight: 700; fill: #2563eb; }
    .col-norm { font-size: 12px; fill: #1e293b; }
    .col-type { font-size: 11px; fill: #64748b; text-anchor: end; font-family: monospace; }
  </style>

  <!-- Title Banner -->
  <rect x="30" y="20" width="1220" height="48" rx="8" fill="#f0fdf4" stroke="#86efac" stroke-width="1.5" />
  <text x="640" y="50" font-size="16" font-weight="800" fill="#166534" text-anchor="middle">
    SƠ ĐỒ CƠ SỞ DỮ LIỆU QUẢN LÝ SINH VIÊN (DATABASE: QuanLySinhVien)
  </text>

  <!-- TABLE 1: Class -->
  <g transform="translate(60, 110)" filter="url(#shadow)">
    <rect width="280" height="185" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 272,0 Q 280,0 280,8 L 280,36 L 0,36 Z" fill="#1e40af" />
    <text x="18" y="24" class="tbl-title">🏫 Class (Lớp học)</text>
    
    <text x="18" y="62" class="col-pk">🔑 ClassID (PK, AI)</text>
    <text x="262" y="62" class="col-type">INT NOT NULL</text>
    <line x1="12" y1="74" x2="268" y2="74" stroke="#f1f5f9" />

    <text x="18" y="98" class="col-norm">ClassName</text>
    <text x="262" y="98" class="col-type">VARCHAR(60) NOT NULL</text>
    <line x1="12" y1="110" x2="268" y2="110" stroke="#f1f5f9" />

    <text x="18" y="134" class="col-norm">StartDate</text>
    <text x="262" y="134" class="col-type">DATETIME NOT NULL</text>
    <line x1="12" y1="146" x2="268" y2="146" stroke="#f1f5f9" />

    <text x="18" y="170" class="col-norm">Status</text>
    <text x="262" y="170" class="col-type">BIT</text>
  </g>

  <!-- TABLE 2: Student -->
  <g transform="translate(480, 110)" filter="url(#shadow)">
    <rect width="320" height="235" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 312,0 Q 320,0 320,8 L 320,36 L 0,36 Z" fill="#4338ca" />
    <text x="18" y="24" class="tbl-title">👨‍🎓 Student (Sinh viên)</text>
    
    <text x="18" y="62" class="col-pk">🔑 StudentId (PK, AI)</text>
    <text x="302" y="62" class="col-type">INT NOT NULL</text>
    <line x1="12" y1="74" x2="308" y2="74" stroke="#f1f5f9" />

    <text x="18" y="96" class="col-norm">StudentName</text>
    <text x="302" y="96" class="col-type">VARCHAR(30) NOT NULL</text>
    <line x1="12" y1="106" x2="308" y2="106" stroke="#f1f5f9" />

    <text x="18" y="128" class="col-norm">Address</text>
    <text x="302" y="128" class="col-type">VARCHAR(50)</text>
    <line x1="12" y1="138" x2="308" y2="138" stroke="#f1f5f9" />

    <text x="18" y="160" class="col-norm">Phone</text>
    <text x="302" y="160" class="col-type">VARCHAR(20)</text>
    <line x1="12" y1="170" x2="308" y2="170" stroke="#f1f5f9" />

    <text x="18" y="192" class="col-norm">Status</text>
    <text x="302" y="192" class="col-type">BIT</text>
    <line x1="12" y1="202" x2="308" y2="202" stroke="#f1f5f9" />

    <text x="18" y="222" class="col-fk">🔗 ClassId (FK)</text>
    <text x="302" y="222" class="col-type">INT NOT NULL</text>
  </g>

  <!-- TABLE 3: Subject -->
  <g transform="translate(930, 390)" filter="url(#shadow)">
    <rect width="290" height="185" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 282,0 Q 290,0 290,8 L 290,36 L 0,36 Z" fill="#0f766e" />
    <text x="18" y="24" class="tbl-title">📚 Subject (Môn học)</text>
    
    <text x="18" y="62" class="col-pk">🔑 SubId (PK, AI)</text>
    <text x="272" y="62" class="col-type">INT NOT NULL</text>
    <line x1="12" y1="74" x2="278" y2="74" stroke="#f1f5f9" />

    <text x="18" y="98" class="col-norm">SubName</text>
    <text x="272" y="98" class="col-type">VARCHAR(30) NOT NULL</text>
    <line x1="12" y1="110" x2="278" y2="110" stroke="#f1f5f9" />

    <text x="18" y="134" class="col-norm">Credit</text>
    <text x="272" y="134" class="col-type">TINYINT (>=1) DEFAULT 1</text>
    <line x1="12" y1="146" x2="278" y2="146" stroke="#f1f5f9" />

    <text x="18" y="170" class="col-norm">Status</text>
    <text x="272" y="170" class="col-type">BIT DEFAULT 1</text>
  </g>

  <!-- TABLE 4: Mark (Junction Table between Student & Subject) -->
  <g transform="translate(480, 420)" filter="url(#shadow)">
    <rect width="320" height="215" rx="8" fill="#ffffff" stroke="#cbd5e1" />
    <path d="M 0,8 Q 0,0 8,0 L 312,0 Q 320,0 320,8 L 320,36 L 0,36 Z" fill="#c2410c" />
    <text x="18" y="24" class="tbl-title">📝 Mark (Điểm thi - Quan hệ N - N)</text>
    
    <text x="18" y="62" class="col-pk">🔑 MarkId (PK, AI)</text>
    <text x="302" y="62" class="col-type">INT NOT NULL</text>
    <line x1="12" y1="74" x2="308" y2="74" stroke="#f1f5f9" />

    <text x="18" y="94" class="col-fk">🔗 SubId (FK, UQ)</text>
    <text x="302" y="94" class="col-type">INT NOT NULL</text>
    <line x1="12" y1="104" x2="308" y2="104" stroke="#f1f5f9" />

    <text x="18" y="124" class="col-fk">🔗 StudentId (FK, UQ)</text>
    <text x="302" y="124" class="col-type">INT NOT NULL</text>
    <line x1="12" y1="134" x2="308" y2="134" stroke="#f1f5f9" />

    <text x="18" y="154" class="col-norm">Mark</text>
    <text x="302" y="154" class="col-type">FLOAT (0-100) DEFAULT 0</text>
    <line x1="12" y1="164" x2="308" y2="164" stroke="#f1f5f9" />

    <text x="18" y="184" class="col-norm">ExamTimes</text>
    <text x="302" y="184" class="col-type">TINYINT DEFAULT 1</text>
    <line x1="12" y1="194" x2="308" y2="194" stroke="#f1f5f9" />

    <text x="18" y="206" font-size="11" font-weight="700" fill="#dc2626">⚡ UNIQUE (SubId, StudentId)</text>
  </g>

  <!-- RELATIONSHIP CONNECTORS -->
  <!-- Class.ClassID -> Student.ClassId (1 : N) -->
  <path d="M 340,172 L 410,172 L 410,332 L 480,332" fill="none" stroke="#1e40af" stroke-width="2.5" />
  <circle cx="340" cy="172" r="4" fill="#1e40af" />
  <polygon points="475,327 485,332 475,337" fill="#1e40af" />

  <!-- Student.StudentId -> Mark.StudentId (1 : N) -->
  <path d="M 640,345 L 640,420" fill="none" stroke="#4338ca" stroke-width="2.5" />
  <circle cx="640" cy="345" r="4" fill="#4338ca" />
  <polygon points="635,415 640,425 645,415" fill="#4338ca" />

  <!-- Subject.SubId -> Mark.SubId (1 : N) -->
  <path d="M 930,480 L 865,480 L 865,514 L 800,514" fill="none" stroke="#0f766e" stroke-width="2.5" />
  <circle cx="930" cy="480" r="4" fill="#0f766e" />
  <polygon points="805,509 795,514 805,519" fill="#0f766e" />

  <!-- SUMMARY INFO CARD -->
  <g transform="translate(60, 655)">
    <rect width="1160" height="140" rx="10" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5" />
    <text x="25" y="28" font-size="13.5" font-weight="800" fill="#0f172a">ĐẶC ĐIỂM CÁC RÀNG BUỘC TOÀN VẸN (CONSTRAINTS) ĐÃ CẤU HÌNH:</text>
    <text x="35" y="54" font-size="12" fill="#334155">• AUTO_INCREMENT &amp; PRIMARY KEY: Tự động tăng khóa chính trên tất cả các bảng (ClassID, StudentId, SubId, MarkId).</text>
    <text x="35" y="78" font-size="12" fill="#334155">• CHECK CONSTRAINT: Ràng buộc số tín chỉ Credit >= 1 trên bảng Subject; Điểm thi Mark trong khoảng 0 đến 100.</text>
    <text x="35" y="102" font-size="12" fill="#334155">• UNIQUE CONSTRAINT: UNIQUE (SubId, StudentId) đảm bảo mỗi sinh viên trong 1 lần thi chỉ có 1 bản ghi điểm cho 1 môn học.</text>
    <text x="35" y="124" font-size="12" font-weight="700" fill="#16a34a">✓ Mô hình CSDL chuẩn hóa, phân rã chính xác quan hệ Nhiều - Nhiều (N - N) giữa Sinh viên và Môn học qua bảng Mark.</text>
  </g>
</svg>
"""

base_dir = r"C:\Users\Admin\.gemini\antigravity-ide\scratch\jwbd-2023-sql-student-management"
assets_dir = os.path.join(base_dir, "assets")

svg_path = os.path.join(assets_dir, "erd_quan_ly_sinh_vien.svg")
with open(svg_path, "w", encoding="utf-8") as f:
    f.write(svg_content)

html_content = f"""<!DOCTYPE html>
<html lang="vi">
<head>
  <meta charset="UTF-8">
  <title>Sơ đồ CSDL QuanLySinhVien</title>
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      background: #f1f5f9;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      display: flex;
      justify-content: center;
      align-items: center;
      min-height: 100vh;
      padding: 30px;
    }}
    .card {{
      background: #ffffff;
      border-radius: 20px;
      padding: 24px 28px 32px 28px;
      box-shadow: 0 20px 25px -5px rgba(0,0,0,0.08);
      border: 1px solid #cbd5e1;
    }}
  </style>
</head>
<body>
  <div class="card">
    {svg_content}
  </div>
</body>
</html>
"""

html_path = os.path.join(assets_dir, "index.html")
with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
temp_dir = tempfile.gettempdir()
temp_png = os.path.join(temp_dir, "erd_quan_ly_sinh_vien.png")
dest_png = os.path.join(assets_dir, "erd_quan_ly_sinh_vien.png")

cmd = [
    chrome_path,
    "--headless=new",
    "--no-sandbox",
    "--disable-gpu",
    "--window-size=1400,980",
    f"--screenshot={temp_png}",
    "file:///" + html_path.replace("\\", "/")
]

subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(temp_png):
    shutil.copy2(temp_png, dest_png)
    print("PNG rendered successfully to", dest_png)
else:
    print("Error rendering PNG")
