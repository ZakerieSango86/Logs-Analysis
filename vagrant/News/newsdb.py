#!/usr/bin/env python2.7

import psycopg2


def get_top_articles():
    """Return top articles from news db.

    Performs a SQL query that retrieves the top 3 articles according to number
    of views recorded in a separate log table.
    """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """Select articles.title, count(log.path) as views
                From articles left join log
                    On articles.slug = right(log.path, -9)
                Group by articles.title
                Order by views desc
                Limit 3"""
    c.execute(query)
    result = c.fetchall()
    columnNames = [desc[0] for desc in c.description]
    db.close()
    return result, columnNames

def get_top_authors():
    """Return top authors from news db.

    Performs a SQL query that retrieves the top 3 authors according to number
    of views recorded in a separate log table.
    """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """Select authors.name, sum(subquery2.times_viewed) as views
                From authors
                Join
                    (Select articles.author, articles.title, subquery1.times_viewed
                        From (
                            Select articles.title, count(log.path) as times_viewed
                            From articles
                                left join log
                                On articles.slug = right(log.path, -9)
                            Group by articles.title
                            Order by times_viewed desc) subquery1
                        join articles on articles.title = subquery1.title) subquery2
                On authors.id = subquery2.author
                Group by authors.id
                Order by views desc
                """
    c.execute(query)
    result = c.fetchall()
    columnNames = [desc[0] for desc in c.description]
    db.close()
    return result, columnNames

def get_error_percentage():
    """Return top authors from news db.

    Performs a SQL query that retrieves the top 3 authors according to number
    of views recorded in a separate log table.
    """
    db = psycopg2.connect("dbname=news")
    c = db.cursor()
    query = """
            SELECT
            trim(to_char(sq2.date_row, 'Month')) || ' ' || to_char(sq2.date_row,'dd, yyyy'),
            round(sum(sq2.error_instance::DECIMAL * 100.0 / sq2.total_views),2)::text || '%' AS error
            FROM
                (SELECT date(log.time) AS date_row, count(log.status) AS total_views, sq1.error_instance
                FROM
                    (SELECT date(log.time) AS date_row, count(log.status) AS error_instance
                    FROM log
                    WHERE status='404 NOT FOUND'
                    GROUP BY date(log.time)
                    ORDER BY error_instance desc) sq1
                JOIN log on date(log.time) = sq1.date_row
                GROUP BY date(log.time), sq1.error_instance
                ORDER BY total_views desc) sq2
            GROUP BY date_row
            ORDER BY error desc
            LIMIT 1
        """
    c.execute(query)
    result = c.fetchall()
    columnNames = [desc[0] for desc in c.description]
    db.close()
    return result, columnNames

def get_results_array(query):
    results = query[0]
    columnName = query[1][1]
    new_array = []
    o = 0
    for i in results:
        new_array.append(results[o][0])
        new_array.append(results[o][1])
        new_array.append(columnName)
        o += 1
    return new_array

def post_articles():
    articles_array = get_results_array(get_top_articles())
    return articles_array

def post_authors():
    authors_array = get_results_array(get_top_authors())
    return authors_array

def post_errors():
    errors_array = get_results_array(get_error_percentage())
    return errors_array
