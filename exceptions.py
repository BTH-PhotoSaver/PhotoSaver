#!/usr/bin/python3

from constants import SUPPORTED_FILE_TYPES


class UnsupportedFileTypeError(Exception):
    def __init__(self, message=f"File type unsupported. Supported formats are: {', '.join(SUPPORTED_FILE_TYPES)}"):

        super().__init__(message)


class ImageTitleMissingError(Exception):
    def __init__(self, message="Please specify a title."):
        super().__init__(message)


class FileUnspecifiedError(Exception):
    def __init__(self, message="Please choose a file."):
        super().__init__(message)
