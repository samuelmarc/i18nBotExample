import i18n

i18n.set('filename_format', '{locale}.{format}')
i18n.set('enable_memoization', True)
i18n.load_path.append('langs')


def _(key, lang, **kwargs):
    return i18n.t(key, locale=lang, **kwargs)
