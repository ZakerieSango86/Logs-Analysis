import webbrowser
import os
from newsdb import post_articles, post_authors, post_errors

# Styles and scripting for the page
main_page_head = '''
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }

        .reporting-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
    </style>
'''

# The main page layout and title bar
main_page_content = '''
<!DOCTYPE html>
<html lang="en">
  <body>
    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Udacity News Reporting Dashboard</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
        {article_report}
        {author_report}
        {error_report}
    </div>
  </body>
</html>
'''


article_report_content = '''
<div class="reporting-tile">
    <h2>{report_title}</h2>
    <ul>
        <li>{item_1}</li>
        <li>{item_2}</li>
        <li>{item_3}</li>
    </ul>
</div>
'''

author_report_content = '''
<div class="reporting-tile">
    <h2>{report_title}</h2>
    <ul>
        <li>{item_1}</li>
        <li>{item_2}</li>
        <li>{item_3}</li>
    </ul>
</div>
'''

error_report_content = '''
<div class="reporting-tile">
    <h2>{report_title}</h2>
    <ul>
        <li>{item_1}</li>
    </ul>
</div>
'''


# Python code to format web content
top_articles = post_articles()
top_authors = post_authors()
top_errors = post_errors()

def create_article_report(query_list):
    """Return a list of top articles, formatted into string variables"""
    content = ''
    content += article_report_content.format(
        report_title = "The top 3 articles of all time:",
        item_1 = query_list[0] + " - " + str(query_list[1]) + " " + query_list[2],
        item_2 = query_list[3] + " - " + str(query_list[4]) + " " + query_list[5],
        item_3 = query_list[6] + " - " + str(query_list[7]) + " " + query_list[8]
        )
    return content

def create_author_report(query_list):
    """Return a list of top authors, formatted into string variables"""
    content = ''
    content += author_report_content.format(
        report_title = "The top 3 authors of all time:",
        item_1 = query_list[0] + " - " + str(query_list[1]) + " " + query_list[2],
        item_2 = query_list[3] + " - " + str(query_list[4]) + " " + query_list[5],
        item_3 = query_list[6] + " - " + str(query_list[7]) + " " + query_list[8]
        )
    return content

def create_error_report(query_list):
    """Return a single entry list, formatted into a string variable"""
    content = ''
    content += error_report_content.format(
        report_title = "The day we had the most failed attempts to access our site:",
        item_1 = query_list[0] + " - " + query_list[1] + " " + query_list[2]
        )
    return content


def open_report_page(articles, authors, errors):
    """Create a html report using data from the News DB.

    Keyword arguments:
    articles -- list of articles
    authors -- list of authors
    errors -- list of errors
    """

    # Create or overwrite the output file
    output_file = open('news.html', 'w')

    # Replace the placeholder for the report tiles with the actual dynamically generated content
    rendered_content = main_page_content.format(article_report=create_article_report(articles),
                                            author_report=create_author_report(authors),
                                            error_report=create_error_report(errors))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()


open_report_page(top_articles, top_authors, top_errors)
