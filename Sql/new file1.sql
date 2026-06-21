create  database company_funnel;
use  company_funnel;
create table companies(
company_id  int primary key ,
name varchar(20),
created_at date
);
create table jobs(
job_id int primary key,
company_id int ,
job_title varchar(50),
posted_date date,
foreign key (company_id) references companies(company_id)
);
create table applications(
application_id int primary key,
job_id int,
student_id int ,
applied_date date,
foreign key (job_id) references jobs(job_id)
);
create table shortlists(
application_id int,
shortlisted_id int primary key,
shortlisted_date date,
foreign key (application_id) references applications(application_id)
);
create table interviews(
interview_id int primary key,
application_id int,
interview_date date,
foreign key (application_id) references applications(application_id)
);
create table hired(
hire_id int primary key,
application_id int ,
hire_date date,
foreign key (application_id) references applications(application_id)
);
INSERT INTO companies VALUES
(1,'Infosys','2026-01-01'),
(2,'TCS','2026-01-02'),
(3,'Wipro','2026-01-03'),
(4,'HCL','2026-01-04'),
(5,'Tech Mahindra','2026-01-05'),
(6,'Accenture','2026-01-06'),
(7,'Capgemini','2026-01-07'),
(8,'Cognizant','2026-01-08'),
(9,'IBM','2026-01-09'),
(10,'Deloitte','2026-01-10'),
(11,'Oracle','2026-01-11'),
(12,'Microsoft','2026-01-12'),
(13,'Google','2026-01-13'),
(14,'Amazon','2026-01-14'),
(15,'Adobe','2026-01-15'),
(16,'Paytm','2026-01-16'),
(17,'Flipkart','2026-01-17'),
(18,'Zomato','2026-01-18'),
(19,'Swiggy','2026-01-19'),
(20,'PhonePe','2026-01-20'),
(21,'Razorpay','2026-01-21'),
(22,'Freshworks','2026-01-22'),
(23,'Zoho','2026-01-23'),
(24,'Myntra','2026-01-24'),
(25,'Meesho','2026-01-25'),
(26,'Naukri','2026-01-26'),
(27,'UpGrad','2026-01-27'),
(28,'Byjus','2026-01-28'),
(29,'Unacademy','2026-01-29'),
(30,'Ola','2026-01-30'),
(31,'Uber','2026-01-31'),
(32,'SAP','2026-02-01'),
(33,'Salesforce','2026-02-02'),
(34,'Intel','2026-02-03'),
(35,'Cisco','2026-02-04'),
(36,'Nvidia','2026-02-05'),
(37,'AMD','2026-02-06'),
(38,'Qualcomm','2026-02-07'),
(39,'JP Morgan','2026-02-08'),
(40,'Goldman Sachs','2026-02-09'),
(41,'KPMG','2026-02-10'),
(42,'EY','2026-02-11'),
(43,'PwC','2026-02-12'),
(44,'L&T','2026-02-13'),
(45,'Reliance','2026-02-14'),
(46,'Tata Steel','2026-02-15'),
(47,'Mahindra','2026-02-16'),
(48,'Bajaj','2026-02-17'),
(49,'Hero','2026-02-18'),
(50,'Havells','2026-02-19');
INSERT INTO jobs
SELECT
company_id*2-1,
company_id,
'Data Analyst',
DATE_ADD(created_at, INTERVAL 5 DAY)
FROM companies;

INSERT INTO jobs
SELECT
company_id*2,
company_id,
'Business Analyst',
DATE_ADD(created_at, INTERVAL 10 DAY)
FROM companies;
## jobs 
INSERT INTO jobs
SELECT
company_id*2-1,
company_id,
'Data Analyst',
DATE_ADD(created_at, INTERVAL 5 DAY)
FROM companies;

INSERT INTO jobs
SELECT
company_id*2,
company_id,
'Business Analyst',
DATE_ADD(created_at, INTERVAL 10 DAY)
FROM companies;
# applications
INSERT INTO applications
SELECT
    n,
    ((n - 1) % 100) + 1,
    1000 + n,
    DATE_ADD('2026-03-01', INTERVAL (n % 30) DAY)
FROM (
    WITH RECURSIVE nums AS (
        SELECT 1 AS n
        UNION ALL
        SELECT n + 1
        FROM nums
        WHERE n < 500
    )
    SELECT n
    FROM nums
) AS t;
#shortlisted
INSERT INTO shortlists
SELECT
application_id,
application_id,
DATE_ADD(applied_date,INTERVAL 3 DAY)
FROM applications
WHERE application_id <= 150;
#interviews
INSERT INTO interviews
SELECT
shortlisted_id,
application_id,
DATE_ADD(shortlisted_date,INTERVAL 5 DAY)
FROM shortlists
WHERE shortlisted_id <= 80;
#hired
INSERT INTO hired
SELECT
interview_id,
application_id,
DATE_ADD(interview_date,INTERVAL 7 DAY)
FROM interviews
WHERE interview_id <= 30;
select * from hired;
