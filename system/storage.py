#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-02 11:39:05
# @Author  : Claus Chen (245618722@qq.com)
# @Link    : https://github.com/clauschen121


from django.core.files.storage import FileSystemStorage


class ImageStorage(FileSystemStorage):
    from django.conf import settings

    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(ImageStorage, self).__init__(location, base_url)

    def _save(self, name, content):
        import os
        import time
        import random
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0, 100)
        name = os.path.join(d, fn + ext)
        return super(ImageStorage, self)._save(name, content)
