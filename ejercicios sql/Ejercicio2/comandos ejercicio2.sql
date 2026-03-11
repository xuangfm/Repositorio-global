--¿Qué empleado tiene más clientes asignados?
SELECT 
e.FirstName || ' ' || e.LastName AS Nombre_Empleado, 
COUNT(c.CustomerId) AS total_clientes
FROM Employee e
JOIN Customer c ON e.EmployeeId = c.SupportRepId
GROUP BY e.EmployeeId
ORDER BY total_clientes DESC;

-- ¿En qué mes se factura más? ¿Y menos?
SELECT 
strftime('%m', InvoiceDate) , 
SUM(Total)
FROM Invoice
GROUP BY strftime('%m', InvoiceDate)
ORDER BY sum(total) DESC;

-- ¿Cuántos clientes han comprado solo una vez?
SELECT CustomerId , count(InvoiceId) as total_compras
FROM Invoice
GROUP by CustomerId
HAVING count(total) =1;

--# Pregunta 4: ¿Cuál es el género más vendido por número de tracks comprados?

SELECT *, 
SUM(Quantity) AS NumeroCanciones 
FROM InvoiceLine 
JOIN TRACK ON InvoiceLine.TrackId = Track.TrackId 
JOIN Genre on Track.GenreId = Genre.GenreId 
GROUP BY Genre.GenreId 
ORDER BY NumeroCanciones DESC Limit 5;

SELECT *,
SUM(Quantity) AS NumeroCanciones 
FROM InvoiceLine il
JOIN TRACK t ON il.TrackId = t.TrackId 
JOIN Genre g on t.GenreId = g.GenreId 
GROUP BY g.GenreId 
ORDER BY NumeroCanciones DESC Limit 5;




































































