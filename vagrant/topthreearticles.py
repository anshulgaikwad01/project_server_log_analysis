#! /usr/bin/env python3
import psycopg2
from formatter import repeat_separator


def fetch_top_three_articles():
    conn = psycopg2.connect(database="news",
                            user="vagrant",
                            password="vagrant")
    c = conn.cursor()
    c.execute('''SELECT COUNT(LOG.PATH) AS hits,
               ARTICLES.SLUG,
               ARTICLES.TITLE,
               AUTHORS.NAME
               FROM LOG, ARTICLES, AUTHORS
               WHERE LOG.PATH != '/' AND
               LOG.STATUS = '200 OK' AND
               ARTICLES.SLUG = SUBSTR(LOG.PATH, LENGTH('/article/') +1)
               AND ARTICLES.AUTHOR = AUTHORS.ID
               GROUP BY
               ARTICLES.SLUG,
               AUTHORS.NAME,
               ARTICLES.TITLE
               ORDER BY hits DESC LIMIT 3;
               ''')
    results = c.fetchall()
    conn.close()
    return results


def layout_top_three_articles():
    print("Top articles:")
    repeat_separator()
    for items in fetch_top_three_articles():
        print(" The total number of views for the article '" + str(items[1]) +
              "' by the author '" + str(items[3]) +
              "' on the page '" + str(items[2]) +
              "' are " + str(items[0]) + ".\n")
    repeat_separator()


if __name__ == '__main__':
    layout_top_three_articles()
