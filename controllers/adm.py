# -*- coding: utf-8 -*-


def index():
    """
    Action index.
    """
    response.title = "Administração"
    response.flash = T("Teste")
    return {}

def teste():
	return redirect(URL(c='adm', f='index'))