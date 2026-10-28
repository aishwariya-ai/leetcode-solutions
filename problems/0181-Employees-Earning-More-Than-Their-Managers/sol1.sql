-- ========================================================
-- 181. Employees Earning More Than Their Managers
-- Difficulty : Easy
-- Language   : MySQL
-- Solution   : #1
-- Runtime    : 433 ms (Beats 38%)
-- Memory     : 0B (Beats 100%)
-- Link       : https://leetcode.com/problems/employees-earning-more-than-their-managers/
-- ========================================================

# Write your MySQL query statement below
select e.name as Employee  from Employee e join Employee m on e.managerId=m.id where e.salary>m.salary 