import os
from django.core.files import File
from django.conf import settings
from artigos.models import Artigo

media_root = '/workspaces/DiogoAlves-a22407390/mediafiles'

for obj in Artigo.objects.all():
    if obj.fotografia and obj.fotografia.name:
        local_path = os.path.join(media_root, obj.fotografia.name)
        if os.path.exists(local_path):
            with open(local_path, 'rb') as f:
                obj.fotografia.save(
                    os.path.basename(local_path),
                    File(f),
                    save=True
                )
            print(f"Migrado: {obj}")
        else:
            print(f"Ficheiro não encontrado: {local_path}")