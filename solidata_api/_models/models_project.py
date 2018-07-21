# -*- encoding: utf-8 -*-

"""
_models/models_projects.py  
- provides the models for all api routes
"""

from log_config import log, pformat

log.debug("... loading models_projects.py ...")


from flask_restplus import fields

### import data serializers
from solidata_api._serializers.schema_logs import *  
from solidata_api._serializers.schema_generic import *  
from solidata_api._serializers.schema_projects import *  

### import generic models functions
from solidata_api._models.models_generic import * 

### create models from serializers
# nested models : https://github.com/noirbizarre/flask-restplus/issues/8
# model_user_infos 	= ns.model( "User model", user_infos) #, mask="{name,surname,email}" )



class Project_infos : 
	"""
	Model to display / marshal 
	specific projects's infos
	"""

	def __init__(self, ns_) :
		
		### SELF MODULES
		self.basic_infos 			= create_model_basic_infos(ns_, model_name="Project_infos")
		self.log						 	= create_model_log(ns_, 				model_name="Project_log", include_is_running=True )
		self.modif_log				= create_model_modif_log(ns_, 	model_name="Project_modif_log")
		self.specs						= create_model_specs(ns_,				model_name="Project_specs")
		self.team 						= create_model_team(ns_,				model_name="Project_team")
		self.datasets 				= create_model_datasets(ns_, 		model_name="Project_datasets", 	schema_list=["dmt","dsi","rec","dso"])
		self.uses							= create_uses(ns_,							model_name="Project_uses", 			schema_list=["usr"])
		
		### IN / complete data to enter in DB
		self.mod_complete_in 	= ns_.model('Project_in', {

				'infos' 		: self.basic_infos,
				'specs'			: self.specs , 
				'log'				: self.log , 
				'modif_log'	: self.modif_log , 
				'uses'			: self.uses,

				### team and edition levels
				'team'		: self.team ,

				### datasets 
				"datasets"		: self.datasets ,
				# 'dmt' 		: oid_dmt,
				# 'dsi' 		: fields.List(oid_dsi),
				# 'rec' 		: fields.List(oid_rec),
				# 'dso' 		: fields.List(oid_dso),
		})

		### OUT / complete data to enter in DB
		# self.mod_complete_out  = ns_.model('Project_out', {

		# 		'infos' 	: self.basic_infos,
		# 		'log' 		: self.project_log , 
				
		# 		### team and edition levels
		# 		# 'project_team'					: fields.List(self.collaborator) ,
		# 		'proj_team'		: self.collaborators ,

		# 		### datasets 
		# 		'datamodel' 						: oid,
		# 		'dataset_inputs' 				: fields.List(oid),
		# 		'correspondance_dicts' 	: fields.List(oid),
		# 		'recipes' 							: fields.List(oid),

		# 	})


	@property
	def model_complete_in(self): 
		return self.mod_complete_in

	# @property
	# def model_complete_out(self): 
	# 	return self.mod_complete_out

