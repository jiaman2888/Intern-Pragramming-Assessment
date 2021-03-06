
#Using MySql to answer this question.


# 1. Write a query that returns all posts posted in the past 24 hours

SELECT * FROM LoveCouch.Posts
WHERE time_posted >= NOW() - INTERVAL 1 DAY;

# 2. Write a query that returns all posts grouped by topic

SELECT * FROM LoveCouch.Posts
ROUP BY topic;

#3. Write a query that returns all anonymous posts posted in the last week, sorted by most recent to least recent.

SELECT * FROM LoveCouch.Posts
WHERE is_anonymous is true AND date_posted > current_date - 7
ORDER BY time_posted DESC;


# 4. Write a query to return all posts that have the word “Love” in the title.

SELECT * FROM LoveCouch.Posts
WHERE title LIKE “%Love%”;
