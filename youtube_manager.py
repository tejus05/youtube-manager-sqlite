import sqlite3

conn = sqlite3.connect('youtube_videos.db')

cursor = conn.cursor()

cursor.execute('''
  CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL,
               time TEXT NOT NULL
  )
''')


def list_all_videos():
  cursor.execute("SELECT * FROM videos")
  for row in cursor.fetchall():
    print(row)

def add_video():
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
  conn.commit()

def update_video():
  name = input("Enter video name: ")
  time = input("Enter video time: ")
  id = input("Enter video id to be updated: ")
  cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?",(name, time, id))
  conn.commit()

def delete_video():
  index = int(input("Enter the video to be deleted: "))
  cursor.execute("DELETE FROM videos WHERE id = ?",(index,))
  conn.commit()

def main():
  
  while True:
    print("Youtube Manager")
    print("1. List all youtube videos")
    print("2. Add a youtube video")
    print("3. Update a youtube video detail")
    print("4.Delete a youtube video")
    print("5. Exit")
    choice = input("Enter your choice: ")
    
    match choice:
      case '1':
        list_all_videos()
      case '2':
        add_video()
      case '3':
        update_video()
      case '4':
        delete_video()
      case '5':
        break
      case _:
        print("Invalid Choice")

  conn.close()

if __name__ == "__main__":
  main()