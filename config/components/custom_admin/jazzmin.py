JAZZMIN_SETTINGS = {
    # Заголовок окна (По умолчанию будет current_admin_site.site_title,
    # если он отсутствует или None)
    'site_title': 'Административная панель сайта',

    # Заголовок на экране бренда и входа в систему (максимум 19 символов)
    # (по умолчанию current_admin_site.site_header, если он отсутствует или None)
    'site_header': 'Админпанель',

    # Логотип (левый верхний угол), должен присутствовать в статических файлах
    'site_logo': 'project/img/admin/logo.png',

    # Классы CSS, которые применяются к логотипу выше
    'site_logo_classes': 'img-circle',

    # Relative path to a favicon for your site, will default to site_logo if absent (ideally 32x32 px)
    'site_icon': None,

    # Текст приветствия на экране входа в систему
    'welcome_sign': 'Добро пожаловать!',

    # Copyright on the footer
    'copyright': None,

    # The model admin to search from the search bar, search bar omitted if excluded
    'search_model': 'auth.User',

    # Имя поля в модели пользователя, содержащей изображение аватара
    'user_avatar': 'avatar',

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    'topmenu_links': [

        # Url that gets reversed (Permissions can be added)
        {'name': 'Home',  'url': 'admin:index', 'permissions': ['auth.view_user']},

        # model admin to link to (Permissions checked against model)
        {'model': 'auth.User'},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {'app': 'books'},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ('app' url type is not allowed)
    'usermenu_links': [
        {'name': 'Support', 'url': 'https://github.com/farridav/django-jazzmin/issues', 'new_window': True},
        {'model': 'auth.user'}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    'show_sidebar': True,

    # Whether to aut expand the menu
    'navigation_expanded': True,

    # Hide these apps when generating side menu e.g (auth)
    'hide_apps': [],

    # Hide these models when generating side menu (e.g auth.user)
    'hide_models': [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    'order_with_respect_to': ['auth', 'books', 'books.author', 'books.book'],

    # Custom links to append to app groups, keyed on app name
    'custom_links': {
        'books': [{
            'name': 'Make Messages', 
            'url': 'make_messages', 
            'icon': 'fas fa-comments',
            'permissions': ['books.view_book']
        }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free&v=5.0.0,5.0.1,5.0.10,5.0.11,5.0.12,5.0.13,5.0.2,5.0.3,5.0.4,5.0.5,5.0.6,5.0.7,5.0.8,5.0.9,5.1.0,5.1.1,5.2.0,5.3.0,5.3.1,5.4.0,5.4.1,5.4.2,5.13.0,5.12.0,5.11.2,5.11.1,5.10.0,5.9.0,5.8.2,5.8.1,5.7.2,5.7.1,5.7.0,5.6.3,5.5.0,5.4.2
    # for the full list of 5.13.0 free icon classes
    'icons': {
        'auth': 'fas fa-users-cog',
        'auth.user': 'fas fa-user',
        'auth.Group': 'fas fa-users',
    },
    # Icons that are used when one is not manually specified
    'default_icon_parents': 'fas fa-chevron-circle-right',
    'default_icon_children': 'fas fa-circle',

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    'related_modal_active': False,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    'custom_css': None,
    'custom_js': None,
    # Whether to show the UI customizer on the sidebar
    'show_ui_builder': False,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    'changeform_format': 'horizontal_tabs',
    # override change forms on a per modeladmin basis
    'changeform_format_overrides': {'auth.user': 'collapsible', 'auth.group': 'vertical_tabs'},
    # Add a language dropdown into the admin
    'language_chooser': True,
}

JAZZMIN_UI_TWEAKS = {
    'theme': 'spacelab',
    # 'dark_mode_theme': 'darkly',
}
