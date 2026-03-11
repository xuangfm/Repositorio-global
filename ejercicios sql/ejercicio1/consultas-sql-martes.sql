SELECT * FROM Invoice;
SELECT CustomerId as Cliente_id, InvoiceDate as Fecha_factura, Total FROM Invoice;
SELECT CustomerId, InvoiceDate, Total 
FROM Invoice WHERE Total > 10;
SELECT CustomerId, InvoiceDate, Total FROM Invoice;
SELECT CustomerId, InvoiceDate, BillingCountry, Total 
FROM Invoice WHERE BillingCountry = 'USA';
SELECT * FROM Invoice ORDER BY Total DESC;
SELECT * FROM Invoice ORDER BY Total DESC LIMIT 5;
SELECT DISTINCT BillingCountry FROM Invoice ORDER BY BillingCountry ASC;
SELECT COUNT(*) FROM Invoice;
SELECT CustomerId, COUNT(*) AS TotalInvoices FROM Invoice GROUP BY CustomerId ORDER BY TotalInvoices DESC;
SELECT BillingCountry, round(AVG(Total),2) AS AverageTotal FROM Invoice GROUP BY BillingCountry ORDER BY AverageTotal DESC;

--Muestra las facturas con Total entre 5 y 15.,
SELECT *
FROM Invoice
WHERE total BETWEEN 5 AND 15;

--Muestra facturas de USA o Canada.,
SELECT BillingCountry , Total 
FROM Invoice
WHERE BillingCountry = "USA" OR BillingCountry = "Canada" ORDER by BillingCountry DESC;

--Calcula el gasto total (SUM(Total)) por país.,

SELECT BillingCountry , sum(total)
FROM Invoice GROUP by BillingCountry ORDER by BillingCountry asc;

--Muestra solo países con más de 10 facturas (HAVING).,

SELECT BillingCountry , total
FROM Invoice
GROUP by BillingCountry
HAVING count(*) >10;

--Muestra top 10 clientes por gasto total.,

SELECT CustomerId , sum(total)
FROM Invoice 
GROUP BY CustomerId ORDER by sum(Total) DESC
LIMIT 10;

--Muestra para cada país: total facturas y ticket medio.,

SELECT BillingCountry , Count(*) , round(avg(total),2)
from Invoice
group by BillingCountry

--Muestra facturas del año 2012 (strftime('%Y', InvoiceDate)).,

SELECT * 
FROM Invoice
WHERE strftime('%Y' , invoiceDate) = "2012";

-- Muestra el top 5 de facturas con mayor total y, en empate, ordena por fecha más reciente.,
SELECT *
FROM Invoice
ORDER by total desc , InvoiceDate desc
limit 5;
