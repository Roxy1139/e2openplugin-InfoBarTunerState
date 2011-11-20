# -*- coding: utf-8 -*-
from Components.Language import language
from Tools.Directories import resolveFilename, SCOPE_PLUGINS, SCOPE_LANGUAGE
from os import environ as os_environ
import gettext

def localeInit():
	lang = language.getLanguage()[:2] # getLanguage returns e.g. "fi_FI" for "language_country"
	os_environ["LANGUAGE"] = lang # Enigma doesn't set this (or LC_ALL, LC_MESSAGES, LANG). gettext needs it!
	gettext.bindtextdomain("AutoTimer", resolveFilename(SCOPE_PLUGINS, "Extensions/AutoTimer/locale"))

def _(txt):
	if txt:
		t = gettext.dgettext("AutoTimer", txt)
		if t == txt:
			t = gettext.gettext(txt)
		return t 
	else:
		return ""

localeInit()
language.addCallback(localeInit)
