SELECT p.idnumber
FROM patients p
JOIN reservations r ON p.id = r.patient_id
JOIN services s ON r.service_id = s.id
WHERE s.specialty_id = 123456
    AND r.res_date >= UNIX_TIMESTAMP(DATE_SUB(CURDATE(), INTERVAL 6 MONTH));
