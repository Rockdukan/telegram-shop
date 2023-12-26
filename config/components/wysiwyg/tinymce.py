"""Tinymce settings"""
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'convert_urls': True,
    'custom_undo_redo_levels': 20,
    'height': '400px',
    'width': 'auto',
    'language': 'ru',
    'menubar': 'file edit view insert format tools table help',
    'relative_urls': False,
    "remove_script_host": False,
    'statusbar': True,
    'theme': 'silver',
    'plugins':
        'advlist anchor autolink autoresize autosave'
        'bbcode charmap code codesample colorpicker contextmenu'
        'directionality emoticons fullpage fullscreen help hr'
        'image imagetools importcss insertdatetime legacyoutput link lists'
        'media nonbreaking noneditable pagebreak paste preview print'
        'quickbars save searchreplace spellchecker'
        'tabfocus table template textcolor textpattern toc'
        'visualblocks visualchars wordcount',
    'toolbar1':
        'undo redo|bold italic underline strikethrough|'
        'forecolor backcolor removeformat|selectall copy cut paste remove'
        'alignleft aligncenter alignright alignjustify|'
        'bullist numlist checklist|outdent indent| help',
    'toolbar2':
        'fontselect fontsizeselect formatselect|numlist bullist|'
        'casechange permanentpen formatpainter removeformat|'
        'pagebreak|charmap emoticons',
    'toolbar3':
        'fullscreen  preview save print|visualaid insertfile image media'
        'pageembed template link anchor codesample|a11ycheck ltr rtl|'
        'styleselect subscript superscript showcomments addcomment code',
}

TINYMCE_COMPRESSOR = False

TINYMCE_EXTRA_MEDIA = {
    'css': {
        'all': [],
    },
    'js': [],
}

TINYMCE_FILEBROWSER = ''  # filebrowser

TINYMCE_SPELLCHECKER = False

X_FRAME_OPTIONS = 'SAMEORIGIN'
