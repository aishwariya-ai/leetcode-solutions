-- ========================================================
-- 183. Customers Who Never Order
-- Difficulty : Easy
-- Language   : MySQL
-- Solution   : #1
-- Runtime    : 931 ms (Beats 7%)
-- Memory     : 0B (Beats 100%)
-- Link       : https://leetcode.com/problems/customers-who-never-order/
-- ========================================================

select name as Customers from Customers c left join Orders o on c.id=o.customerId where o.customerId is NULL
