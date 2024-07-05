import markovify
from googleapiclient.discovery import build

# Укажите свой API-ключ здесь
API_KEY = 'AIzaSyChuy233zvq620EdG5soBpeCbW-uHSYUb4'

# ID канала YouTube
CHANNEL_ID = 'UCpSUW9jMVFclGbLpCepnAMA'  # Пример ID канала

def get_video_titles(api_key, channel_id):
    # Создание объекта YouTube API
    youtube = build('youtube', 'v3', developerKey=api_key)

    try:
        # Получение ID плейлиста загруженных видео
        response = youtube.channels().list(
            part='contentDetails',
            id=channel_id
        ).execute()

        if 'items' not in response or len(response['items']) == 0:
            print("Ошибка: канал не найден или отсутствуют данные")
            return []

        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

        # Получение списка видео из плейлиста
        video_titles = []
        next_page_token = None

        while True:
            response = youtube.playlistItems().list(
                part='snippet',
                playlistId=uploads_playlist_id,
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            if 'items' not in response:
                print("Ошибка: нет видео в плейлисте или ошибка API")
                break

            for item in response['items']:
                video_titles.append(item['snippet']['title'])

            next_page_token = response.get('nextPageToken')
            if not next_page_token:
                break

        return video_titles

    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return []

def save_titles_to_file(titles, file_path):
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            for title in titles:
                file.write(title + '\n')
        print(f"Названия видео успешно записаны в файл {file_path}")
    except Exception as e:
        print(f"Не удалось записать в файл: {e}")

def load_titles(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Не удалось загрузить файл: {e}")
        return ""

def generate_title(model, tries=100):
    for _ in range(tries):
        title = model.make_sentence(tries=100)
        if title:
            return title
    return None

def main():
    titles = get_video_titles(API_KEY, CHANNEL_ID)
    if titles:
        save_titles_to_file(titles, 'titles.txt')
        titles_text = load_titles('titles.txt')
        
        if titles_text:
            try:
                text_model = markovify.NewlineText(titles_text)
                new_title = generate_title(text_model)
                if new_title:
                    print(f"Сгенерированное название: {new_title}")
                else:
                    print("Не удалось сгенерировать название")
            except Exception as e:
                print(f"Ошибка при создании модели цепи Маркова: {e}")
        else:
            print("Файл titles.txt пуст")
    else:
        print("Нет доступных названий видео")

if __name__ == "__main__":
    main()
print(main())
