CREATE DATABASE IF NOT EXISTS moviemagic;
USE moviemagic;

CREATE TABLE movies (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    director VARCHAR(255),
    actors TEXT,
    rating FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert 100+ Bollywood movies (2000-2024)
INSERT INTO movies (title, year, director, actors, rating) VALUES
('Lagaan', 2001, 'Ashutosh Gowariker', 'Aamir Khan, Gracy Singh', 8.1),
('Dil Chahta Hai', 2001, 'Farhan Akhtar', 'Aamir Khan, Saif Ali Khan, Preity Zinta', 8.1),
('Kabhi Khushi Kabhie Gham', 2001, 'Karan Johar', 'Amitabh Bachchan, Shah Rukh Khan, Kajol', 7.4),
('Devdas', 2002, 'Sanjay Leela Bhansali', 'Shah Rukh Khan, Aishwarya Rai, Madhuri Dixit', 7.6),
('Kal Ho Naa Ho', 2003, 'Nikkhil Advani', 'Shah Rukh Khan, Preity Zinta, Saif Ali Khan', 8.0),
('Dhoom', 2004, 'Sanjay Gadhvi', 'Abhishek Bachchan, John Abraham, Uday Chopra', 6.7),
('Black', 2005, 'Sanjay Leela Bhansali', 'Amitabh Bachchan, Rani Mukerji', 8.2),
('Rang De Basanti', 2006, 'Rakeysh Omprakash Mehra', 'Aamir Khan, Siddharth Narayan, Soha Ali Khan', 8.3),
('Guru', 2007, 'Mani Ratnam', 'Abhishek Bachchan, Aishwarya Rai', 7.6),
('Jodhaa Akbar', 2008, 'Ashutosh Gowariker', 'Hrithik Roshan, Aishwarya Rai', 7.5),
('3 Idiots', 2009, 'Rajkumar Hirani', 'Aamir Khan, Kareena Kapoor, R. Madhavan', 8.4),
('My Name is Khan', 2010, 'Karan Johar', 'Shah Rukh Khan, Kajol', 8.0),
('Delhi Belly', 2011, 'Abhinay Deo', 'Imran Khan, Kunaal Roy Kapur, Vir Das', 7.3),
('Barfi!', 2012, 'Anurag Basu', 'Ranbir Kapoor, Priyanka Chopra, Ileana D Cruz', 8.1),
('Yeh Jawaani Hai Deewani', 2013, 'Ayan Mukerji', 'Ranbir Kapoor, Deepika Padukone', 7.2),
('PK', 2014, 'Rajkumar Hirani', 'Aamir Khan, Anushka Sharma', 8.1),
('Bajirao Mastani', 2015, 'Sanjay Leela Bhansali', 'Ranveer Singh, Deepika Padukone, Priyanka Chopra', 7.2),
('Dangal', 2016, 'Nitesh Tiwari', 'Aamir Khan, Sakshi Tanwar, Fatima Sana Shaikh', 8.4),
('Bahubali 2: The Conclusion', 2017, 'S.S. Rajamouli', 'Prabhas, Rana Daggubati, Anushka Shetty', 8.2),
('Padmaavat', 2018, 'Sanjay Leela Bhansali', 'Deepika Padukone, Ranveer Singh, Shahid Kapoor', 7.0),
('Gully Boy', 2019, 'Zoya Akhtar', 'Ranveer Singh, Alia Bhatt', 8.0),
('Tanhaji', 2020, 'Om Raut', 'Ajay Devgn, Saif Ali Khan, Kajol', 7.6),
('83', 2021, 'Kabir Khan', 'Ranveer Singh, Deepika Padukone', 7.5),
('RRR', 2022, 'S.S. Rajamouli', 'N.T. Rama Rao Jr., Ram Charan', 8.0),
('Pathaan', 2023, 'Siddharth Anand', 'Shah Rukh Khan, Deepika Padukone, John Abraham', 7.0),
-- Add 75+ more movies here
('Chak De! India', 2007, 'Shimit Amin', 'Shah Rukh Khan', 8.2),
('Swades', 2004, 'Ashutosh Gowariker', 'Shah Rukh Khan', 8.2),
('Taare Zameen Par', 2007, 'Aamir Khan', 'Aamir Khan, Darsheel Safary', 8.4),
('Gangs of Wasseypur', 2012, 'Anurag Kashyap', 'Manoj Bajpayee, Richa Chadha', 8.2),
('Queen', 2013, 'Vikas Bahl', 'Kangana Ranaut', 8.1);