"""CS 1001 - Lab Programming 5: Processing Lists of Compound Data

Friday, November 13, 2026 | One-day programming lab

Read the provided Point and Book classes. Complete only the six TODO
functions below; do not change their signatures. Add your own tests
in test_1.py, and show your passing test suite for instructor signoff.

Keep input lists and the objects they contain unchanged.
"""

from math import sqrt


class Point:
    """A point in a two-dimensional coordinate system."""

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def distance_to(self, other: "Point") -> float:
        """Return the Euclidean distance to another Point (provided)."""
        return sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Book:
    """A book with a list of authors and a title."""

    def __init__(self, authors: list[str], title: str):
        self.authors = authors
        self.title = title


def count_positive(values: list[int]) -> int:
    """Return the number of values strictly greater than zero.

    Example: count_positive([-3, 5, 0, -1, 8, 2]) -> 3
    """
    # TODO (Task 1): Count positive integers using an accumulator.
    number=0
    for value in values:
        if value>0:
            number+=1
    return number


def sum_x_coordinates(points: list[Point]) -> float:
    """Return the sum of all Point.x values, or 0.0 for an empty list.

    Example: Point x-values [1.0, 3.0, -2.0] -> 2.0
    """
    # TODO (Task 2): Accumulate the x-coordinate of each existing point.
    sum=0.0
    for p in points:
        sum+=p.x
    return sum


def average_y_coordinate(points: list[Point]) -> float | None:
    """Return the mean Point.y value, or None for an empty list.

    Example: Point y-values [2.0, 6.0, 10.0] -> 6.0
    """
    # TODO (Task 3): Handle the empty case and calculate the average y.
    if len(points)==0:
        return None
    value=0
    for p in points:
        value+=p.y
    value=value/len(points)
    return value


def book_with_most_authors(books: list[Book]) -> Book | None:
    """Return the existing Book with the most authors, or None if empty.

    If multiple books tie for most authors, return the first such book.
    Do not construct another Book.
    """
    # TODO (Task 4): Remember the best Book object found so far.
    comparison=0
    object=None
    for book in books:
        if len(book.authors)>comparison:
            comparison=len(book.authors)
            object=book
    return object


def furthest_from_origin(points: list[Point]) -> int | None:
    """Return the index of the Point farthest from (0, 0), or None.

    Resolve ties in favor of the first such point. Reuse the provided
    Point.distance_to method instead of duplicating its formula.
    """
    # TODO (Task 5): Track the best index using Point.distance_to.
    raise NotImplementedError


def closest_book_title(books: list[Book], target_length: int) -> str | None:
    """Return the title whose length is closest to target_length.

    Return None for an empty list. If multiple titles are equally close,
    return the title from the first such book. Do not change the books.
    """
    # TODO (Task 6): Track the smallest absolute length difference.
    raise NotImplementedError
