from django.core.exceptions import ValidationError


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')



def validate_file_size(value):
    filesize= value.size
    
    if filesize > 10485760:
        raise ValidationError("The maximum file size that can be uploaded is 10MB")
    else:
        return value