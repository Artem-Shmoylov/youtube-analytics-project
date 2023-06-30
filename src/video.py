import os

from googleapiclient.discovery import build


class Video:
    api_key: str = os.getenv('YT_API_KEY')

    def __init__(self, video_id):
        self.__video_id = video_id
        try:
            self.video_response = self.youtube().videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                               id=video_id).execute()

            self.__video_title = self.video_response['items'][0]['snippet']['title']
            self.__video_url = f'https://www.youtube.com/watch?v={video_id}'
            self.__video_view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.__video_like_count = self.video_response['items'][0]['statistics']['likeCount']
        except IndexError:
            self.__video_like_count = None
            self.__video_view_count = None
            self.__video_title = None
            self.__video_url = None

    def __str__(self):
        return f"{self.__video_title}"

    @property
    def like_count(self):
        return self.__video_like_count

    @property
    def title(self):
        return self.__video_title

    @property
    def video_url(self):
        return self.__video_url

    @property
    def view_count(self):
        return self.__video_view_count

    @classmethod
    def youtube(cls):
        youtube = build('youtube', 'v3', developerKey=Video.api_key)
        return youtube


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):
        super().__init__(video_id)
        self.__playlist_id = playlist_id
