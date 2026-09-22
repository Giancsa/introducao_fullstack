SELECT 
	c_title,
	substr(c_text, 1, 50) || '...' as c_resume
FROM content 
	WHERE c_status = 'on'
	ORDER BY c_created_at DESC;