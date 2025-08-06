from cloudinary.uploader import upload
from cloudinary.exceptions import Error as CloudinaryError
from fastapi import UploadFile, HTTPException

class FileService:
    def __init__(self, folder: str = "rental_marketplace"):
        self.folder = folder

    async def upload_image(self, file: UploadFile, folder: str) -> object:
        try:
            file_content = await file.read()
            return upload(file_content, folder=self.folder + folder)
        except CloudinaryError as e:
            raise HTTPException(status_code=500, detail=f"Cloudinary upload failed: {str(e)}")
