import datetime

db.define_table('aluno',
                Field('foto','upload'),
                Field('nome','string',requires=IS_NOT_EMPTY()),
                Field('idade','string',requires=IS_NOT_EMPTY()),
                Field('responsavel', requires=IS_IN_DB(db,'responsavel.nome','%(nome)s')),
                Field('discipulador','string', requires=IS_NOT_EMPTY()),
                Field('sala', requires=IS_IN_DB(db,'sala.nome','%(nome)s')),
                Field('professor', requires=IS_IN_DB(db,'professor.nome','%(nome)s'))
                )

db.define_table('responsavel',
				Field('nome', 'string', requires=IS_NOT_EMPTY()),
				Field('idade','string',requires=IS_NOT_EMPTY()),
				Field('telefone','string', requires=IS_NOT_EMPTY()),
				Field('email','string'),
				Field('foto','upload'),
				Field('discipulo','boolean', label='É discípulo?'),
				Field('discipulador', label='Discipulador',requires=IS_IN_DB(db,'discipuladores.nome','%(nome)s')),
				Field('rua','string'),
 				Field('numero','string'),
  				Field('bairro','string'),
  				Field('complemento','string'),
  				Field('cidade',requires=IS_IN_DB(db,'cidade.nome','%(nome)s')),
                Field('cep',length=8,requires=[IS_NOT_EMPTY(error_message='Informe o campo CEP.'),
                                IS_MATCH('^\d{8}$', error_message="O CEP deve conter apenas dígitos."),
                                IS_LENGTH(minsize=8, maxsize=8, error_message="O CEP deve ter 8 caracteres")]),
                Field('criado_em', 'datetime', default=request.now),
                Field('criado_por', 'reference auth_user', requires=IS_IN_DB(db, 'auth_user.id', '%(first_name)s'))
				)

db.define_table('sala',
				Field('nome','string')
				)

db.define_table('professor',
				Field('nome','string'),
				Field('foto','upload'),
				Field('telefone','string')
				)

db.define_table('cidade',
  				Field('nome',requires=[IS_NOT_EMPTY()]),
  				Field('uf',requires=IS_IN_DB(db,'uf.id','%(nome)s')),
				)

db.define_table('uf',
  				Field('nome',requires=[IS_NOT_EMPTY()]),
				)

db.define_table('discipuladores',
				Field ('nome','string', requires=IS_NOT_EMPTY()),
				Field('telefone','string',requires=IS_NOT_EMPTY())
				)

