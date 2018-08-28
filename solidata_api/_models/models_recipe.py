# -*- encoding: utf-8 -*-

"""
_models/models_recipes.py  
"""

from log_config import log, pformat

log.debug("... loading models_recipes.py ...")


from flask_restplus import fields

### import data serializers
from solidata_api._serializers.schema_logs import *  
from solidata_api._serializers.schema_generic import *  
# from solidata_api._serializers.schema_projects import *  

### import generic models functions
from solidata_api._models.models_generic import * 

### create models from serializers
# nested models : https://github.com/noirbizarre/flask-restplus/issues/8
# model_user_infos 	= ns.model( "User model", user_infos) #, mask="{name,surname,email}" )


class NewDmt : 
	"""
	Model to display / marshal rec basic form
	"""

	def __init__(self, ns_):
		self.mod = ns_.model( "Rec_basics", doc_basics )
	
	@property
	def model(self): 
		return self.mod


class Dmt_infos : 
	"""
	Model to display / marshal 
	recipe
	"""

	def __init__(self, ns_) :
    		
		model_type 					= "Rec"

		### SELF MODULES
		self._id 					= oid_field
		self.basic_infos 			= create_model_basic_infos(	ns_,	model_name=model_type+"_infos")
		self.public_auth			= create_model_public_auth(	ns_,	model_name=model_type+"_public_auth")
		self.specs					= create_model_specs(		ns_,	model_name=model_type+"_specs")
		self.log					= create_model_log(			ns_,	model_name=model_type+"_log" )
		self.modif_log				= create_model_modif_log(	ns_, 	model_name=model_type+"_modif_log")

		self.uses					= create_model_uses(		ns_,	model_name=model_type+"_uses", 		schema_list=[ "usr","prj" ])
		self.datasets 				= create_model_datasets(	ns_, 	model_name=model_type+"_datasets", 	schema_list=[ "tag","func" ])
		self.translations			= create_model_translations(ns_, 	model_name=model_type+"_translations")
		self.team 					= create_model_team(		ns_,	model_name=model_type+"_team")

		self.mapping				= create_model_mappings(	ns_,	model_name=model_type+"_mapping", 	schema_list=[ "dsi_to_dmf", "rec_to_dmf" ])


		self.model_id = {
			'_id' 			: self._id,
		}		
		self.model_in = {
			'modif_log'		: self.modif_log , 
			"datasets"		: self.datasets ,
		
		}
		self.model_min = {
			'infos' 		: self.basic_infos,
			'public_auth' 	: self.public_auth,
			'specs'			: self.specs , 
			'log'			: self.log , 
			
			'uses'			: self.uses,
			'translations' 	: self.translations,
			'team'			: self.team ,
		
		
		}

		### IN / complete data to enter in DB
		self.mod_complete_in 	= ns_.model(model_type+"_in", { **self.model_min, **self.model_in } )

		### MIN / minimum data to marshall out 
		self.mod_minimum 		= ns_.model(model_type+"_minimum", { **self.model_min, **self.model_id })


	@property
	def model_complete_in(self): 
		return self.mod_complete_in

	@property
	def model_minimum(self): 
		return self.mod_minimum

