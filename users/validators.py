from rest_framework.exceptions import ValidationError


class VideoValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val is not None:
            if 'youtube.com' not in tmp_val and 'youtu.be' not in tmp_val:
                raise ValidationError('No YouTube Video')