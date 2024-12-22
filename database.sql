CREATE DATABASE medkink;
USE medkink;

DROP TABLE IF EXISTS users;
CREATE DATABASE medkink;
USE medkink;
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(150) NOT NULL UNIQUE,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    date_joined TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM authentication_user;


-- Create Pharmacies table first
CREATE TABLE Pharmacies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    address TEXT,
    phone_number VARCHAR(20),
    email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Users table
CREATE TABLE Users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) NOT NULL,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    phone_number VARCHAR(20),
    address TEXT,
    role ENUM('admin', 'regular', 'guest') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Prescriptions table
CREATE TABLE Prescriptions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    file_path VARCHAR(255) NOT NULL,
    status ENUM('uploaded', 'verified', 'rejected') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create Drugs table
CREATE TABLE Drugs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    description TEXT,
    price DECIMAL(10, 2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Create Orders table
CREATE TABLE Orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    prescription_id INT,
    status ENUM('pending', 'confirmed', 'delivered', 'canceled') NOT NULL,
    total_price DECIMAL(10, 2),
    pickup_or_delivery ENUM('pickup', 'delivery') NOT NULL,
    delivery_address TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (prescription_id) REFERENCES Prescriptions(id)
);

-- Create OrderItems table
CREATE TABLE OrderItems (
    id INT AUTO_INCREMENT PRIMARY KEY,
    order_id INT,
    drug_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (order_id) REFERENCES Orders(id),
    FOREIGN KEY (drug_id) REFERENCES Drugs(id)
);

-- Create Notifications table
CREATE TABLE Notifications (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT NOT NULL,
    type VARCHAR(50) NOT NULL,
    status ENUM('sent', 'failed') NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create Inventory table
CREATE TABLE Inventory (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pharmacy_id INT,
    drug_id INT,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (pharmacy_id) REFERENCES Pharmacies(id),
    FOREIGN KEY (drug_id) REFERENCES Drugs(id)
);

-- Create EmergencyContacts table
CREATE TABLE EmergencyContacts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    contact_name VARCHAR(100) NOT NULL,
    contact_phone VARCHAR(20),
    contact_email VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Create Feedback table
CREATE TABLE Feedback (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    order_id INT,
    rating INT NOT NULL,
    comments TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (order_id) REFERENCES Orders(id)
);

-- Create Chat table
CREATE TABLE Chat (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    message TEXT NOT NULL,
    response TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);
INSERT INTO Users (username, password, email, first_name, last_name, phone_number, address, role) VALUES
('john_doe', 'hashed_password_1', 'john_doe@example.com', 'John', 'Doe', '555-1234', '123 Main St, Cityville', 'regular'),
('jane_doe', 'hashed_password_2', 'jane_doe@example.com', 'Jane', 'Doe', '555-5678', '456 Oak St, Cityville', 'admin'),
('alice_smith', 'hashed_password_3', 'alice_smith@example.com', 'Alice', 'Smith', '555-8765', '789 Pine St, Cityville', 'regular'),
('bob_jones', 'hashed_password_4', 'bob_jones@example.com', 'Bob', 'Jones', '555-3456', '321 Elm St, Townsville', 'guest'),
('charlie_brown', 'hashed_password_5', 'charlie_brown@example.com', 'Charlie', 'Brown', '555-2345', '654 Cedar St, Villagecity', 'regular'),
('david_clark', 'hashed_password_6', 'david_clark@example.com', 'David', 'Clark', '555-5432', '987 Birch St, Cityville', 'admin'),
('emma_williams', 'hashed_password_7', 'emma_williams@example.com', 'Emma', 'Williams', '555-6789', '135 Maple St, Cityville', 'regular'),
('george_martin', 'hashed_password_8', 'george_martin@example.com', 'George', 'Martin', '555-9876', '246 Walnut St, Townsville', 'regular'),
('henry_harris', 'hashed_password_9', 'henry_harris@example.com', 'Henry', 'Harris', '555-1122', '357 Fir St, Villagecity', 'regular'),
('isla_perez', 'hashed_password_10', 'isla_perez@example.com', 'Isla', 'Perez', '555-2233', '468 Oak St, Cityville', 'guest'),
('jack_lee', 'hashed_password_11', 'jack_lee@example.com', 'Jack', 'Lee', '555-3344', '579 Cedar St, Townsville', 'admin'),
('karen_kim', 'hashed_password_12', 'karen_kim@example.com', 'Karen', 'Kim', '555-4455', '680 Pine St, Villagecity', 'regular'),
('leo_white', 'hashed_password_13', 'leo_white@example.com', 'Leo', 'White', '555-5566', '791 Birch St, Cityville', 'regular'),
('mia_king', 'hashed_password_14', 'mia_king@example.com', 'Mia', 'King', '555-6677', '902 Maple St, Townsville', 'regular'),
('nora_moore', 'hashed_password_15', 'nora_moore@example.com', 'Nora', 'Moore', '555-7788', '103 Cedar St, Villagecity', 'admin'),
('oliver_scott', 'hashed_password_16', 'oliver_scott@example.com', 'Oliver', 'Scott', '555-8899', '214 Pine St, Cityville', 'regular'),
('peter_johnson', 'hashed_password_17', 'peter_johnson@example.com', 'Peter', 'Johnson', '555-9900', '325 Oak St, Townsville', 'regular'),
('quinn_davis', 'hashed_password_18', 'quinn_davis@example.com', 'Quinn', 'Davis', '555-1011', '436 Fir St, Villagecity', 'guest'),
('rachel_evans', 'hashed_password_19', 'rachel_evans@example.com', 'Rachel', 'Evans', '555-1123', '547 Maple St, Cityville', 'regular'),
('samuel_lee', 'hashed_password_20', 'samuel_lee@example.com', 'Samuel', 'Lee', '555-2234', '658 Cedar St, Townsville', 'regular'),
('tina_garcia', 'hashed_password_21', 'tina_garcia@example.com', 'Tina', 'Garcia', '555-3345', '769 Pine St, Villagecity', 'admin'),
('ursula_roberts', 'hashed_password_22', 'ursula_roberts@example.com', 'Ursula', 'Roberts', '555-4456', '870 Birch St, Cityville', 'regular'),
('victor_hall', 'hashed_password_23', 'victor_hall@example.com', 'Victor', 'Hall', '555-5567', '981 Oak St, Townsville', 'guest'),
('willow_thomas', 'hashed_password_24', 'willow_thomas@example.com', 'Willow', 'Thomas', '555-6678', '109 Cedar St, Villagecity', 'regular'),
('xander_morris', 'hashed_password_25', 'xander_morris@example.com', 'Xander', 'Morris', '555-7789', '210 Fir St, Cityville', 'admin'),
('yasmine_hernandez', 'hashed_password_26', 'yasmine_hernandez@example.com', 'Yasmine', 'Hernandez', '555-8890', '321 Maple St, Townsville', 'regular'),
('zachary_garcia', 'hashed_password_27', 'zachary_garcia@example.com', 'Zachary', 'Garcia', '555-9901', '432 Oak St, Villagecity', 'regular');

INSERT INTO Prescriptions (user_id, file_path, status) VALUES
(1, '/prescriptions/john_doe_prescription.pdf', 'verified'),
(2, '/prescriptions/jane_doe_prescription.pdf', 'uploaded'),
(3, '/prescriptions/alice_smith_prescription.pdf', 'rejected'),
(4, '/prescriptions/bob_jones_prescription.pdf', 'verified'),
(5, '/prescriptions/charlie_brown_prescription.pdf', 'uploaded'),
(6, '/prescriptions/david_clark_prescription.pdf', 'verified'),
(7, '/prescriptions/emma_williams_prescription.pdf', 'rejected'),
(8, '/prescriptions/george_martin_prescription.pdf', 'verified'),
(9, '/prescriptions/henry_harris_prescription.pdf', 'verified'),
(10, '/prescriptions/isla_perez_prescription.pdf', 'uploaded'),
(11, '/prescriptions/jack_lee_prescription.pdf', 'verified'),
(12, '/prescriptions/karen_kim_prescription.pdf', 'rejected'),
(13, '/prescriptions/leo_white_prescription.pdf', 'verified'),
(14, '/prescriptions/mia_king_prescription.pdf', 'uploaded'),
(15, '/prescriptions/nora_moore_prescription.pdf', 'rejected'),
(16, '/prescriptions/oliver_scott_prescription.pdf', 'verified'),
(17, '/prescriptions/peter_johnson_prescription.pdf', 'uploaded'),
(18, '/prescriptions/quinn_davis_prescription.pdf', 'verified'),
(19, '/prescriptions/rachel_evans_prescription.pdf', 'verified'),
(20, '/prescriptions/samuel_lee_prescription.pdf', 'uploaded'),
(21, '/prescriptions/tina_garcia_prescription.pdf', 'verified'),
(22, '/prescriptions/ursula_roberts_prescription.pdf', 'rejected'),
(23, '/prescriptions/victor_hall_prescription.pdf', 'verified'),
(24, '/prescriptions/willow_thomas_prescription.pdf', 'uploaded'),
(25, '/prescriptions/xander_morris_prescription.pdf', 'verified'),
(26, '/prescriptions/yasmine_hernandez_prescription.pdf', 'rejected'),
(27, '/prescriptions/zachary_garcia_prescription.pdf', 'verified');


INSERT INTO Drugs (name, category, description, price) VALUES
('Aspirin', 'Pain Reliever', 'Used for pain relief', 10.99),
('Paracetamol', 'Pain Reliever', 'Used to reduce fever and pain', 7.99),
('Ibuprofen', 'Pain Reliever', 'Used for pain, fever, and inflammation', 5.49),
('Amoxicillin', 'Antibiotic', 'Used for treating bacterial infections', 12.99),
('Metformin', 'Diabetic Medication', 'Used to control blood sugar levels', 15.99),
('Lipitor', 'Cholesterol Medication', 'Used to lower cholesterol levels', 22.99),
('Prednisone', 'Corticosteroid', 'Used to treat inflammation', 14.99),
('Ciprofloxacin', 'Antibiotic', 'Used to treat various infections', 11.49),
('Atenolol', 'Beta Blocker', 'Used to treat high blood pressure', 9),
('Simvastatin', 'Cholesterol Medication', 'Used to reduce cholesterol levels', 19.99),
('Lisinopril', 'ACE Inhibitor', 'Used to treat high blood pressure and heart failure', 13.49),
('Clindamycin', 'Antibiotic', 'Used for bacterial infections', 16.99),
('Prozac', 'Antidepressant', 'Used for depression and anxiety', 18.99),
('Zoloft', 'Antidepressant', 'Used for anxiety and depression', 20.49),
('Loratadine', 'Antihistamine', 'Used for allergies and hay fever', 5.79),
('Fluoxetine', 'Antidepressant', 'Used for depression and panic disorder', 21.99),
('Gabapentin', 'Anticonvulsant', 'Used to treat nerve pain and seizures', 14.99),
('Metoprolol', 'Beta Blocker', 'Used for high blood pressure and heart problems', 9.79),
('Oxycodone', 'Pain Reliever', 'Used for severe pain management', 25.99),
('Furosemide', 'Diuretic', 'Used to reduce swelling and fluid retention', 7.29),
('Hydrochlorothiazide', 'Diuretic', 'Used for high blood pressure and fluid retention', 6.99),
('Citalopram', 'Antidepressant', 'Used for depression and anxiety disorders', 17.99),
('Diazepam', 'Anxiolytic', 'Used for anxiety, muscle spasms, and seizures', 12.49),
('Tamsulosin', 'Alpha Blocker', 'Used to treat enlarged prostate', 9.99),
('Warfarin', 'Anticoagulant', 'Used to prevent blood clots', 14.99),
('Fluticasone', 'Steroid', 'Used for asthma and allergies', 11.59),
('Ranitidine', 'Antacid', 'Used to treat heartburn and acid reflux', 8.49),
('Prednisolone', 'Corticosteroid', 'Used for inflammatory conditions', 16.49),
('Enalapril', 'ACE Inhibitor', 'Used for high blood pressure and heart failure', 10.99);


SET SQL_SAFE_UPDATES = 0;




INSERT INTO Orders (user_id, prescription_id, status, total_price, pickup_or_delivery, delivery_address) VALUES
(7, 88, 'delivered', 95.00, 'delivery', '135 Maple St, Villagecity'),
(8, 89, 'pending', 110.00, 'pickup', ''),
(9, 90, 'delivered', 160.00, 'delivery', '246 Walnut St, Cityville'),
(10, 91, 'canceled', 50.00, 'pickup', ''),
(11, 92, 'pending', 170.00, 'delivery', '357 Fir St, Townsville'),
(12, 93, 'confirmed', 90.00, 'pickup', ''),
(13, 94, 'delivered', 135.00, 'delivery', '468 Oak St, Villagecity'),
(14, 95, 'canceled', 80.00, 'pickup', ''),
(15, 96, 'pending', 120.00, 'delivery', '579 Cedar St, Cityville'),
(16, 97, 'confirmed', 150.00, 'pickup', ''),
(17, 98, 'delivered', 190.00, 'delivery', '680 Pine St, Townsville'),
(18, 99, 'pending', 105.00, 'pickup', ''),
(19, 100, 'canceled', 60.00, 'pickup', ''),
(20, 101, 'confirmed', 210.00, 'delivery', '791 Birch St, Villagecity'),
(21, 102, 'delivered', 130.00, 'delivery', '902 Maple St, Cityville'),
(22, 103, 'pending', 115.00, 'pickup', ''),
(23, 104, 'confirmed', 185.00, 'delivery', '103 Cedar St, Townsville'),
(24, 105, 'delivered', 170.00, 'delivery', '214 Pine St, Villagecity'),
(25, 106, 'canceled', 90.00, 'pickup', ''),
(26, 107, 'pending', 140.00, 'delivery', '325 Oak St, Cityville'),
(27, 108, 'confirmed', 155.00, 'pickup', '');



INSERT INTO OrderItems (order_id, drug_id, quantity, price) VALUES
(146, 1, 2, 10.99),
(176, 2, 3, 7.99),
(177, 3, 4, 5.49),
(205, 4, 1, 12.99),
(206, 5, 2, 15.99),
(207, 6, 3, 22.99),
(232, 7, 2, 14.99),
(233, 8, 4, 11.49),
(234, 9, 5, 9.99),
(235, 10, 1, 19.99),
(236, 11, 3, 13.49),
(237, 12, 2, 16.99),
(238, 13, 4, 18.99),
(239, 14, 1, 20.49),
(240, 15, 2, 5.79),
(241, 16, 3, 21.99),
(242, 17, 5, 12.49),
(243, 18, 4, 9.79),
(244, 19, 3, 25.99),
(245, 20, 1, 14.99),
(246, 21, 3, 7.29),
(247, 22, 2, 6.99),
(248, 23, 4, 17.99),
(249, 24, 5, 21.49),
(256, 25, 1, 12.99),
(257, 26, 2, 19.99),
(258, 27, 3, 14.99);
(28, 28, 1, 10.49),
(29, 29, 3, 9.99),
(30, 30, 2, 7.99);

SELECT * FROM Pharmacies;

INSERT INTO Pharmacies (name, address, phone_number, email) VALUES
('Pharmacy 1', '123 Main St, Cityville', '555-1111', 'pharmacy1@example.com'),
('Pharmacy 2', '456 Oak St, Townsville', '555-2222', 'pharmacy2@example.com'),
('Pharmacy 3', '789 Pine St, Villagecity', '555-3333', 'pharmacy3@example.com'),
('Pharmacy 4', '101 Maple St, Cityville', '555-4444', 'pharmacy4@example.com'),
('Pharmacy 5', '202 Cedar St, Townsville', '555-5555', 'pharmacy5@example.com'),
('Pharmacy 6', '303 Birch St, Villagecity', '555-6666', 'pharmacy6@example.com'),
('Pharmacy 7', '404 Elm St, Cityville', '555-7777', 'pharmacy7@example.com'),
('Pharmacy 8', '505 Pine St, Townsville', '555-8888', 'pharmacy8@example.com'),
('Pharmacy 9', '606 Maple St, Villagecity', '555-9999', 'pharmacy9@example.com'),
('Pharmacy 10', '707 Cedar St, Cityville', '555-1010', 'pharmacy10@example.com'),
('Pharmacy 11', '808 Birch St, Townsville', '555-1112', 'pharmacy11@example.com'),
('Pharmacy 12', '909 Elm St, Villagecity', '555-1212', 'pharmacy12@example.com'),
('Pharmacy 13', '1001 Maple St, Cityville', '555-1313', 'pharmacy13@example.com'),
('Pharmacy 14', '1102 Cedar St, Townsville', '555-1414', 'pharmacy14@example.com'),
('Pharmacy 15', '1203 Birch St, Villagecity', '555-1515', 'pharmacy15@example.com'),
('Pharmacy 16', '1304 Elm St, Cityville', '555-1616', 'pharmacy16@example.com'),
('Pharmacy 17', '1405 Maple St, Townsville', '555-1717', 'pharmacy17@example.com'),
('Pharmacy 18', '1506 Cedar St, Villagecity', '555-1818', 'pharmacy18@example.com'),
('Pharmacy 19', '1607 Birch St, Cityville', '555-1919', 'pharmacy19@example.com'),
('Pharmacy 20', '1708 Elm St, Townsville', '555-2020', 'pharmacy20@example.com'),
('Pharmacy 21', '1809 Maple St, Villagecity', '555-2121', 'pharmacy21@example.com'),
('Pharmacy 22', '1901 Cedar St, Cityville', '555-2222', 'pharmacy22@example.com'),
('Pharmacy 23', '2002 Birch St, Townsville', '555-2323', 'pharmacy23@example.com'),
('Pharmacy 24', '2103 Elm St, Villagecity', '555-2424', 'pharmacy24@example.com'),
('Pharmacy 25', '2204 Maple St, Cityville', '555-2525', 'pharmacy25@example.com'),
('Pharmacy 26', '2305 Cedar St, Townsville', '555-2626', 'pharmacy26@example.com'),
('Pharmacy 27', '2406 Birch St, Villagecity', '555-2727', 'pharmacy27@example.com'),
('Pharmacy 28', '2507 Elm St, Cityville', '555-2828', 'pharmacy28@example.com'),
('Pharmacy 29', '2608 Maple St, Townsville', '555-2929', 'pharmacy29@example.com'),
('Pharmacy 30', '2709 Cedar St, Villagecity', '555-3030', 'pharmacy30@example.com');


INSERT INTO Inventory (pharmacy_id, drug_id, quantity) VALUES
(1, 1, 50),
(1, 2, 100),
(2, 3, 150),
(2, 4, 75),
(3, 5, 200),
(3, 6, 250),
(4, 7, 300),
(4, 8, 400),
(5, 9, 600),
(5, 10, 500),
(6, 11, 700),
(6, 12, 300),
(7, 13, 400),
(7, 14, 450),
(8, 15, 350),
(8, 16, 500),
(9, 17, 550),
(9, 18, 450),
(10, 19, 600),
(10, 20, 700),
(11, 21, 200),
(11, 22, 350),
(12, 23, 150),
(12, 24, 500),
(13, 25, 250),
(13, 26, 150),
(14, 27, 100),
(14, 28, 200),
(15, 29, 150),
(15, 30, 100);


SELECT * FROM Users;
INSERT INTO EmergencyContacts (user_id, contact_name, contact_phone, contact_email) VALUES
(1, 'Mary Doe', '555-1111', 'mary_doe@example.com'),
(2, 'John Smith', '555-2222', 'john_smith@example.com'),
(3, 'Emma Green', '555-3333', 'emma_green@example.com'),
(4, 'Robert Brown', '555-4444', 'robert_brown@example.com'),
(5, 'Linda White', '555-5555', 'linda_white@example.com'),
(6, 'William Black', '555-6666', 'william_black@example.com'),
(7, 'Sophia Blue', '555-7777', 'sophia_blue@example.com'),
(8, 'David Wilson', '555-8888', 'david_wilson@example.com'),
(9, 'Isla Parker', '555-9999', 'isla_parker@example.com'),
(10, 'Michael Harris', '555-1010', 'michael_harris@example.com'),
(11, 'Olivia Adams', '555-2020', 'olivia_adams@example.com'),
(12, 'Henry Scott', '555-3030', 'henry_scott@example.com'),
(13, 'Liam Moore', '555-4040', 'liam_moore@example.com'),
(14, 'Amelia Davis', '555-5050', 'amelia_davis@example.com'),
(15, 'Charlotte Lopez', '555-6060', 'charlotte_lopez@example.com'),
(16, 'James Perez', '555-7070', 'james_perez@example.com'),
(17, 'Benjamin Clark', '555-8080', 'benjamin_clark@example.com'),
(18, 'Jack Garcia', '555-9090', 'jack_garcia@example.com'),
(19, 'Lucas Martinez', '555-1112', 'lucas_martinez@example.com'),
(20, 'Mia Robinson', '555-1212', 'mia_robinson@example.com'),
(21, 'Daniel Evans', '555-1313', 'daniel_evans@example.com'),
(22, 'Ella Moore', '555-1414', 'ella_moore@example.com'),
(23, 'Chloe Thompson', '555-1515', 'chloe_thompson@example.com'),
(24, 'Ethan Harris', '555-1616', 'ethan_harris@example.com'),
(25, 'Ava Taylor', '555-1717', 'ava_taylor@example.com'),
(26, 'Mason Johnson', '555-1818', 'mason_johnson@example.com'),
(27, 'Logan Walker', '555-1919', 'logan_walker@example.com');



