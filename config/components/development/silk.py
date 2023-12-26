"""Silk settings"""
from config.settings import MIDDLEWARE


# Middleware settings
MIDDLEWARE += ('silk.middleware.SilkyMiddleware', )
