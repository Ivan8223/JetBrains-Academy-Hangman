def print_book_info(title, author=None, year=None):
    print(f'"{title}"',
          ' was written' if author is not None or year is not None else '',
          f' by {author}' if author is not None else '',
          f' in {year}' if year is not None else '',
          sep='')
