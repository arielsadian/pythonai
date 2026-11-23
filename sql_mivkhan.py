#--part a:
#1. option 1
#2. option 1
#3. option 2
#4. option 2
#5. option 1
#6 option 2
#7 option 4
#8 option 1
#9 option 4
#10. option 1
import sqlite3
DB_PATH = "televisions.db
def show_all_movies():
  with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies")
    rows = cursor.fetchall()
    print("--- All Movies ---")
    for row in rows:
      print(row)


def search_movies_by_name():
  term = input("Enter movie name or part of it: ").strip()
  with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM movies WHERE movie_name LIKE ?", (f"%{term}%",)
    )
    rows = cursor.fetchall()
    print(f"--- Search results for '{term}' ---")
    for row in rows:
      print(row)


def add_movie():
  print("--- Add New Movie ---")
  movie_name = input("Movie name: ").strip()
  genre = input("Genre: ").strip()
  country = input("Country: ").strip()
  language = input("Language: ").strip()
  year = int(input("Year: ").strip())
  revenue = float(input("Revenue: ").strip())

  with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO movies (movie_name, genre, country, language, year, revenue)
            VALUES (?, ?, ?, ?, ?, ?)
            """,
        (movie_name, genre, country, language, year, revenue),
    )
    conn.commit()
    print("Movie inserted successfully.")


if __name__ == "__main__":
  show_all_movies()
  search_movies_by_name()
  add_movie()
