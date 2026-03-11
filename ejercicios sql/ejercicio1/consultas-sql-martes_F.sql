
-- 1. Muestra todas las columnas de Invoice
SELECT * FROM Invoice;

-- 2. Muestra solo CustomerId, InvoiceDate y Total
SELECT CustomerId AS Cliente, InvoiceDate AS Fecha, total FROM Invoice;

-- 3. Muestra facturas con Total > 10. Añadió ordenar de mayor a menor mostrando las 10 primeras
SELECT Total FROM Invoice WHERE total>10 ORDER BY Total desc LIMIT 10;

-- 4. Muestra facturas del país USA
SELECT Total FROM Invoice WHERE BillingCountry = "USA";

-- 5. Ordena las facturas por Total de mayor a menor
SELECT total FROM Invoice ORDER BY Total DESC;

-- 6. Muestra solo las 5 facturas con mayor Total
SELECT total FROM Invoice ORDER BY Total DESC LIMIT 5;

-- 7. Lista los países de facturación sin duplicados. Añadió ordenar alfabeticamente
SELECT distinct BillingCountry from Invoice ORDER by BillingCountry ASC;

-- 8. Cuenta cuántas facturas hay en total.
SELECT COUNT(total) AS "Total de facturas" FROM Invoice;

-- 9. Cuenta cuántas facturas tiene cada CustomerId.,
SELECT COUNT(CustomerId) AS "Numero de facturas por CustomerId" from Invoice GROUP BY CustomerId;

-- 10. Calcula el ticket medio (AVG(Total)) por BillingCountry y ordénalo de mayor a menor.
SELECT BillingCountry, ROUND(AVG(Total),2) AS  "Ticket medio" FROM Invoice group by BillingCountry order by "Ticket medio" desc;
---------------------------------------------------------------------------------------------
-- 11. Muestra las facturas con Total entre 5 y 15.,
SELECT Total FROM Invoice WHERE total BETWEEN 5 AND 15;

-- 12. Muestra facturas de USA o Canada.,
SELECT BillingCountry, Total 
FROM Invoice 
WHERE BillingCountry= "USA" OR BillingCountry="Canada";

-- 13. Calcula el gasto total (SUM(Total)) por país.,
SELECT BillingCountry, SUM(Total) FROM Invoice GROUP BY BillingCountry;

-- 14. Muestra solo países con más de 10 facturas (HAVING).,
SELECT BillingCountry FROM Invoice GROUP BY BillingCountry HAVING COUNT(total) >10;

-- 15. Muestra top 10 clientes por gasto total.,
SELECT c.CustomerId, c.FirstName, c.LastName, SUM(i.total)   
FROM Customer c INNER JOIN Invoice i
ON c.CustomerId =  i.CustomerId
GROUP BY c.CustomerId
ORDER BY i.total DESC
LIMIT 10;

-- 16. Muestra para cada país: total facturas y ticket medio.,
SELECT BillingCountry, SUM(total), ROUND(AVG(total),2) AS "Ticket medio" FROM Invoice GROUP BY BillingCountry;

-- 17. Muestra facturas del año 2012 (strftime('%Y', InvoiceDate)).,
SELECT InvoiceDate, total
FROM Invoice
WHERE strftime('%Y', InvoiceDate) = '2012';

----Otra forma
SELECT InvoiceDate, total
FROM Invoice 
WHERE InvoiceDate >= "2012-01-01" AND InvoiceDate < "2013-01-01";

-- 18. Muestra el top 5 de facturas con mayor total y, en empate, ordena por fecha más reciente.
SELECT InvoiceDate, total FROM Invoice ORDER BY total DESC, InvoiceDate DESC LIMIT 5;