import requests
import webbrowser
import sqlite3

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label

API_KEY = "AIzaSyAP_uI4YS8v_HGW0tA9ALzjEa9j49V2YEE"

# DATABASE
conn = sqlite3.connect("videos.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS saved (title TEXT, link TEXT)")
conn.commit()


class MyTube(App):

    def build(self):
        root = BoxLayout(orientation="vertical")

        self.search = TextInput(hint_text="Qidir...", size_hint_y=None, height=80)
        btn = Button(text="Qidirish", size_hint_y=None, height=60)
        btn.bind(on_press=self.search_video)

        self.layout = BoxLayout(orientation="vertical", size_hint_y=None)
        self.layout.bind(minimum_height=self.layout.setter("height"))

        scroll = ScrollView()
        scroll.add_widget(self.layout)

        root.add_widget(self.search)
        root.add_widget(btn)
        root.add_widget(scroll)

        return root

    def search_video(self, instance):
        self.layout.clear_widgets()

        url = "https://www.googleapis.com/youtube/v3/search"
        params = {
            "part": "snippet",
            "q": self.search.text,
            "maxResults": 10,
            "type": "video",
            "key": API_KEY
        }

        data = requests.get(url, params=params).json()

        for item in data.get("items", []):
            title = item["snippet"]["title"]
            vid = item["id"]["videoId"]
            thumb = item["snippet"]["thumbnails"]["high"]["url"]

            link = f"https://www.youtube.com/watch?v={vid}"

            box = BoxLayout(orientation="vertical", size_hint_y=None, height=320)

            img = AsyncImage(source=thumb, size_hint_y=None, height=200)
            lbl = Label(text=title, size_hint_y=None, height=50)

            open_btn = Button(text="▶ Play", size_hint_y=None, height=50)
            save_btn = Button(text="💾 Save", size_hint_y=None, height=50)

            open_btn.bind(on_press=lambda x, v=vid: self.play_video(v))
            save_btn.bind(on_press=lambda x, t=title, l=link: self.save(t, l))

            box.add_widget(img)
            box.add_widget(lbl)
            box.add_widget(open_btn)
            box.add_widget(save_btn)

            self.layout.add_widget(box)

    def play_video(self, video_id):
        webbrowser.open(f"https://www.youtube.com/watch?v={video_id}")

    def save(self, title, link):
        cursor.execute("INSERT INTO saved VALUES (?,?)", (title, link))
        conn.commit()
        print("Saved:", title)


if __name__ == "__main__":
    MyTube().run()

