import re

def is_valid_file(filename: str, file_type: str) -> bool:
    def is_audio(filename: str) -> bool:
        # Check if the filename is valid for audio
        return bool(re.match(r'^[a-zA-Z]+\.(mp3|flac|alac|aac)$', filename))

    def is_image(filename: str) -> bool:
        # Check if the filename is valid for image
        return bool(re.match(r'^[a-zA-Z]+\.(jpg|jpeg|png|bmp|gif)$', filename))

    if file_type == 'audio':
        return is_audio(filename)
    elif file_type == 'image':
        return is_image(filename)
    else:
        # If the file type is neither audio nor image, return False
        return False

