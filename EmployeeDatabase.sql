create database if not exists emp;
use emp; 

CREATE TABLE if not exists Employee (
    EmployeeID INT,
    FirstName VARCHAR(255),
    LastName VARCHAR(255),
    DOE DATE,
    Salary INT,
    Department VARCHAR(255),
    primary key(EmployeeID)
);  

insert into Employee values(1, 'Matthew', 'Truelove', '2018-01-01', 1000000, 'Java');
insert into Employee values(2, 'Orquidia', 'Moreno', '2019-01-01', 1000000, 'Java');
insert into Employee values(3, 'Christina', 'Torres', '2022-01-01', 1000000, 'Data');
insert into Employee values(4, 'Jamison', 'Ducey', '2022-01-01', 1000000, 'Data');

