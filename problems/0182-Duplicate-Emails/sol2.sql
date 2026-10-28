-- ========================================================
-- 182. Duplicate Emails
-- Difficulty : Easy
-- Language   : MySQL
-- Solution   : #2
-- Runtime    : 435 ms (Beats 32%)
-- Memory     : 0B (Beats 100%)
-- Link       : https://leetcode.com/problems/duplicate-emails/
-- ========================================================

# Write your MySQL query statement below
select email from Person group by email having count(*)>1