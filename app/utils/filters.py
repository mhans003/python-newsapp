# Format date for post (convert datetime object to string in correct format).
def format_date(date):
  return date.strftime('%m/%d/%y')

# Test format_date by outputting current date.
from datetime import datetime
print(format_date(datetime.now()))

# Format URL output.
def format_url(url):
  return url.replace('http://', '').replace('https://', '').replace('www.', '').split('/')[0].split('?')[0]

# Test format_url.
print(format_url('http://google.com/test/'))
print(format_url('https://www.google.com?q=test'))

# Format plurals (that end in s)
def format_plural(amount, word):
  if amount != 1:
    return word + 's'

  return word

print(format_plural(2, 'cat'))
print(format_plural(1, 'dog'))