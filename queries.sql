-- Nut-free Icecream with Best Average Rating
SELECT 
	icecream.name, 
  ROUND(AVG(review.rating),2) AS average_rating,
  COUNT(*) AS review_count
FROM review
JOIN icecream ON icecream.id = review.icecream_id 
JOIN icecream_dietr ON icecream_dietr.icecream_id = icecream.id
JOIN dietr ON dietr.id = icecream_dietr.dietr_id
WHERE dietr.name = 'nut_free'
GROUP BY icecream.name
ORDER BY average_rating DESC
;

-- Dietary requirements with highest Average Rating
SELECT 
	dietr.name, 
  ROUND(AVG(review.rating),2) AS average_rating, 
  COUNT(*) AS review_count
FROM dietr
JOIN icecream_dietr ON dietr.id = icecream_dietr.dietr_id
JOIN icecream ON icecream_dietr.icecream_id = icecream.id 
JOIN review ON  icecream.id = review.icecream_id
GROUP BY dietr.name
ORDER BY average_rating DESC
;

-- Icecream with Best Average Rating
SELECT 
	icecream.name, 
  ROUND(AVG(review.rating),2) AS average_rating,
  COUNT(*) AS review_count
FROM review
JOIN icecream
ON icecream.id = review.icecream_id 
GROUP BY icecream.name
ORDER BY average_rating DESC
;

-- Average Review Each Month
SELECT 
	TO_CHAR(DATE_TRUNC('month', date), 'YYYY Month') AS formatted_month, 
  ROUND(AVG(rating),2), 
  COUNT(*) AS review_count
FROM review
GROUP BY DATE_TRUNC('month', date)
ORDER BY DATE_TRUNC('month', date)
;



