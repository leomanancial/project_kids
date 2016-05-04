# @auth.requires(auth.has_membership(role='Administradores') or
#                auth.has_membership(role='Equipe'))
@auth.requires_login()
def alunos():

	"""Form cadastro de Aluno """

	response.title = "Administração"

	teste

	form = SQLFORM(db.aluno)
	
	return locals()

def responsavel():

	form = SQLFORM(db.responsavel)

	return locals()

def discipuladores():

	form = SQLFORM(db.discipuladores)

	return locals()	
    

	   


