-- Problem 2.1

SELECT name FROM records WHERE supervisor = "Oliver Warbucks";


-- Problem 2.2

SELECT * FROM records WHERE supervisor = name;


-- Problem 2.3

SELECT name FROM records WHERE salary > 50000 ORDER BY name;


-- Problem 3.1

SELECT a.day, a.time FROM meetings AS a, records AS b 
    WHERE a.division = b.division AND
          b.supervisor = "Oliver Warbucks";


-- Problem 3.2

SELECT a.name, b.name FROM records AS a, records AS b, meetings AS c, meetings AS d
    WHERE a.division = c.division AND
          b.division = d.division AND
          c.day = d.day AND
          c.time = d.time AND
          a.name > b.name;


-- Problem 3.3 (revised after referring to the solution)

-- "No.  If a department has multiple meetings, then all pairs of individuals within that department will be listed multiple times. To avoid this, we can use the DISTINCT keyword."


-- Problem 3.4

SELECT a.name FROM records AS a, records AS b 
    WHERE a.supervisor = b.name AND
          a.division <> b.division;


-- Problem 4.1

SELECT supervisor, SUM(salary) FROM records GROUP BY supervisor;


-- Problem 4.2

SELECT a.day FROM meetings AS a, records AS b 
    WHERE a.division = b.division 
    GROUP BY a.day HAVING count(*) < 5;


-- Problem 4.3 
-- (Original answer was completely wrong: misunderstood the question)

SELECT a.division FROM records AS a, records AS b 
    WHERE a.division = b.division AND 
          a.name > b.name
    GROUP BY a.division  
    HAVING MAX(a.salary + b.salary) < 100000;


-- Problem 5.1 
-- (Original answer was not perfect: missiong the head name for each column)

CREATE TABLE num_taught AS 
    SELECT professor AS professor, course AS course, count(*) AS times 
    FROM courses GROUP BY professor, course;


-- Problem 5.2

SELECT a.professor, b.professor, a.course FROM num_taught AS a, num_taught AS b
    WHERE a.course = b.course AND 
          a.times = b.times AND 
          a.professor > b.professor;


-- Problem 5.3 
-- (Original answer was wrong in the GROUP BY expression: missing the necessary condition of the same course)

SELECT a.professor, b.professor FROM courses AS a, courses AS b 
    WHERE a.course = b.course AND 
          a.semester = b.semester AND 
          a.professor > b.professor 
    GROUP BY a.professor, b.professor, a.course 
    HAVING count(*) > 1;