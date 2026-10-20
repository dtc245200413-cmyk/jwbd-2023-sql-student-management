-- ==============================================================================
-- BÀI TẬP: XÂY DỰNG CƠ SỞ DỮ LIỆU QUẢN LÝ SINH VIÊN (QuanLySinhVien)
-- Sinh viên thực hiện: DTC245200413
-- Repository: https://github.com/dtc245200413-cmyk/jwbd-2023-sql-student-management
-- Tham khảo: https://github.com/codegym-vn/jwbd-2023-sql-student-management (branch dev)
-- ==============================================================================

-- Bước 1: Tạo cơ sở dữ liệu có tên là QuanLySinhVien
CREATE DATABASE IF NOT EXISTS QuanLySinhVien CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Bước 2: Chọn Database QuanLySinhVien để thao tác với cơ sở dữ liệu này
USE QuanLySinhVien;

-- Bước 3: Tạo bảng Class với các trường ClassId, ClassName, StartDate, Status
CREATE TABLE Class (
    ClassID   INT         NOT NULL AUTO_INCREMENT PRIMARY KEY,
    ClassName VARCHAR(60) NOT NULL,
    StartDate DATETIME    NOT NULL,
    Status    BIT
);

-- Bước 4: Tạo bảng Student với các thuộc tính StudentId, StudentName, Address, Phone, Status, ClassId
CREATE TABLE Student (
    StudentId   INT         NOT NULL AUTO_INCREMENT PRIMARY KEY,
    StudentName VARCHAR(30) NOT NULL,
    Address     VARCHAR(50),
    Phone       VARCHAR(20),
    Status      BIT,
    ClassId     INT         NOT NULL,
    FOREIGN KEY (ClassId) REFERENCES Class (ClassID)
);

-- Bước 5: Tạo bảng Subject với các thuộc tính SubId, SubName, Credit, Status
CREATE TABLE Subject (
    SubId   INT         NOT NULL AUTO_INCREMENT PRIMARY KEY,
    SubName VARCHAR(30) NOT NULL,
    Credit  TINYINT     NOT NULL DEFAULT 1 CHECK ( Credit >= 1 ),
    Status  BIT                  DEFAULT 1
);

-- Bước 6: Tạo bảng Mark với các thuộc tính MarkId, SubId, StudentId, Mark, ExamTimes
CREATE TABLE Mark (
    MarkId    INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    SubId     INT NOT NULL,
    StudentId INT NOT NULL,
    Mark      FLOAT   DEFAULT 0 CHECK ( Mark BETWEEN 0 AND 100),
    ExamTimes TINYINT DEFAULT 1,
    UNIQUE (SubId, StudentId),
    FOREIGN KEY (SubId) REFERENCES Subject (SubId),
    FOREIGN KEY (StudentId) REFERENCES Student (StudentId)
);

-- ==============================================================================
-- DỮ LIỆU MẪU KIỂM CHỨNG TOÀN VẸN DỮ LIỆU (SEED DATA TEST)
-- ==============================================================================

-- 1. Thêm dữ liệu mẫu vào bảng Class
INSERT INTO Class (ClassName, StartDate, Status) VALUES
('A1', '2026-12-20', 1),
('A2', '2026-12-22', 1),
('B3', current_date(), 0);

-- 2. Thêm dữ liệu mẫu vào bảng Student
INSERT INTO Student (StudentName, Address, Phone, Status, ClassId) VALUES
('Hung', 'Ha Noi', '0912111111', 1, 1),
('Hoa', 'Hai phong', NULL, 1, 1),
('Manh', 'HCM', '0123123123', 0, 2);

-- 3. Thêm dữ liệu mẫu vào bảng Subject
INSERT INTO Subject (SubName, Credit, Status) VALUES
('CF', 5, 1),
('C', 6, 1),
('HDJ', 5, 1),
('RDBMS', 10, 1);

-- 4. Thêm dữ liệu mẫu vào bảng Mark
INSERT INTO Mark (SubId, StudentId, Mark, ExamTimes) VALUES
(1, 1, 8, 1),
(1, 2, 10, 2),
(2, 1, 12, 1);
