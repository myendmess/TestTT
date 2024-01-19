SELECT p.idnumber, COUNT(r.patient_id) as num_reservations
FROM patients p
JOIN reservations r ON p.id = r.patient_id
WHERE YEAR(FROM_UNIXTIME(r.res_date)) = YEAR(CURDATE()) - 1
GROUP BY p.id
HAVING num_reservations > 5;
