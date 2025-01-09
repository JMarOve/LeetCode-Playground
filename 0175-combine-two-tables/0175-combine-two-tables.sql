# Write your MySQL query statement below
Select Person.firstname,
Person.lastName,
Address.city,
Address.state
from Person Left join Address On Person.personId = Address.personId