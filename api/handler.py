import pickle
import os
import pandas as pd
from flask                     import Flask, request, Response
from pmmanutencao.PmManutencao import PmManutencao

# loading model
model = pickle.load( open( 'models/xgb.pkl', 'rb' ) )


# initialize api
app = Flask( __name__ )

@app.route( '/predict', methods=['POST'] )
def pmmanutencao_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance( test_json, dict ): # unique example
            test_raw = pd.DataFrame( test_json, index=[0] )
            
        else: # multiple examples
            test_raw = pd.DataFrame( test_json, columns=test_json[0].keys() )
            
        # Instatiate PmManutencao Class
        pipeline = PmManutencao()
        
        
        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df3 )
        
        return df_response
    
    
    else:
        return Response( '{}', status=200, mimetype='application/json' )




if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( '127.0.0.1', port=port, debug=True )