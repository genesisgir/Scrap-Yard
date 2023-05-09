/*
Here is the steps:

1. Drop table if exists
2. Create table
3. Insert data into table (2 rows)
4. Select table
5. Update table
6. Delete a row in the table
7. Truncate table completely (clears table but keeps it)

*/


-- DROPS TABLE
DROP TABLE if exists [TestTable]

-- CREATE TABLE
CREATE TABLE [TestTable]
(
Id int identity(1,1)
,EmployeeName nvarchar(50)
,EmployeeStatus nvarchar(50)
)

-- INSERT DATA INTO TABLE
INSERT INTO [TestTable]
(
EmployeeName
,EmployeeStatus
)
VALUES
(
'Genesis'
,'Active'
)

INSERT INTO [TestTable]
(
EmployeeName
,EmployeeStatus
)
VALUES
(
'whiffle'
,'Active'


-- SLEECT TABLE
SELECT * -- star means everything in table
FROM [TestTable]


-- UPDATE TABLE
UPDATE [TestTable]
SET EmployeeStatus = 'Inactive'
WHERE EmployeeName = 'whiffle'


-- DELETES ROW
DELETE FROM [TestTable]
WHERE EmployeeName = 'Genesis'


-- TRUNCATE TABLE
TRUNCATE TABLE [TestTable]