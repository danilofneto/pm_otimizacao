import pickle
import inflection
import pandas as pd

class PmManutencao( object ):

	def __init__( self ):
		self.home_path  =  '../parameters/'
		self.min_max    = pickle.load( open( self.home_path + '/min_max.pkl', 'rb' ) )


	def data_cleaning( self, df1 ):

		df1.replace( 'na',np.nan,inplace = True )

		imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
		df1_imp_mean =  pd.DataFrame( imp_mean.fit_transform( df1.values ), columns=df1.columns )
		df1 = df1_imp_mean.copy()

		feature_new = ['aa_000', 'ag_001', 'ag_002', 'ag_003', 'al_000', 'am_0', 'aq_000', 'ay_005', 'ay_006', 'ay_008', 'bb_000', 'bj_000', 'bt_000', 'ci_000', 'ck_000', 'cn_000', 'cn_004', 'dn_000', 'ee_005', 'ee_007', 'class']

		df1 = df1[feature_new]

		df1 = pd.DataFrame( data = self.min_max.fit_transform(df1) , columns = df1.columns )

		return df1


	def get_prediction( self, model, original_data, test_data ):

		# prediction
		pred = model.predict( test_Data )

		# Join pred into original data
		original_data['pred'] = pred[:,1].tolist()

		return original_data.to_json( orient = 'records', data_format = 'iso' )



