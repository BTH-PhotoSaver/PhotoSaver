#!/usr/bin/python3

from constants import UPLOAD_TITLE, UPLOAD_TPL, UPLOAD_FINISHED_TITLE, UPLOAD_FINISHED_TPL
from bottle import template, request
from exceptions import ImageTitleMissingError, UnsupportedFileTypeError, FileUnspecifiedError


class UploadPage:
    def render_get(self):
        return template(UPLOAD_TPL, name=UPLOAD_TITLE)

    def render_post(self, image_store):
        title = request.forms.get('title')
        description = request.forms.get('description')
        file = request.files.get('uploaded_file')

        errors = []
        try:
            image_store.save(file, title, description)

        except ImageTitleMissingError as exc:
            errors.append(str(exc))
        except FileUnspecifiedError as exc:
            errors.append(str(exc))
        except UnsupportedFileTypeError as exc:
            errors.append(str(exc))

        if errors:
            return template(UPLOAD_TPL, name=UPLOAD_TITLE, error_messages=errors)

        return template(UPLOAD_FINISHED_TPL, name=UPLOAD_FINISHED_TITLE)
