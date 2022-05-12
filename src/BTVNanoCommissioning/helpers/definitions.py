def definitions():

      jetINDEX = [0,1,28,41,48,49,56,57,58,59,63,64,65] 
      trackINDEX = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,39,40,42,43,44,45,46,47,50,51,52,53,54,55,]
      svINDEX = [2,3,4,5,60,61,62,66]

      interger_variables = [59,63,64,65,66]

      definitions_dict = {
            'DeepCSV_jetNSelectedTracks':
       {'displayname': 'Jet N Selected Tracks', 'manual_ranges': [-0.5, None], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_vertexNTracks':
       {'displayname': 'Vertex N Tracks', 'manual_ranges': [-0.5, None], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_vertexJetDeltaR':
       {'displayname': 'Vertex Jet $\\Delta R$', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackSumJetEtRatio':
       {'displayname': 'Track Sum Jet $E_T$ Ratio', 'manual_ranges': [None, 1.4], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 28, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSig_4':
       {'displayname': 'Track SIP 2D Sig [4]', 'manual_ranges': [-6.5, 4.5], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 22, 'inputVar_units': ''},
      'DeepCSV_trackPtRatio_4':
       {'displayname': 'Track $p_{T,rel}$ Ratio [4]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackPtRatio_5':
       {'displayname': 'Track $p_{T,rel}$ Ratio [5]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackPtRatio_0':
       {'displayname': 'Track $p_{T,rel}$ Ratio [0]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackPtRatio_1':
       {'displayname': 'Track $p_{T,rel}$ Ratio [1]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackPtRatio_2':
       {'displayname': 'Track $p_{T,rel}$ Ratio [2]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackPtRatio_3':
       {'displayname': 'Track $p_{T,rel}$ Ratio [3]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_vertexEnergyRatio':
       {'displayname': 'Vertex Energy Ratio', 'manual_ranges': [0, 2.5], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSig_5':
       {'displayname': 'Track SIP 2D Sig [5]', 'manual_ranges': [-7, 2], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 18, 'inputVar_units': ''},
      'DeepCSV_trackSumJetDeltaR':
       {'displayname': 'Track Sum Jet $\\Delta R$', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackSip3dSig_0':
       {'displayname': 'Track SIP 3D Sig [0]', 'manual_ranges': [-25, 50], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackDecayLenVal_5':
       {'displayname': 'Track Decay Len Val [5]', 'manual_ranges': [-0.1, 1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 22, 'inputVar_units': 'cm'},
      'DeepCSV_trackDecayLenVal_4':
       {'displayname': 'Track Decay Len Val [4]', 'manual_ranges': [-0.1, 1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 22, 'inputVar_units': 'cm'},
      'DeepCSV_vertexMass':
       {'displayname': 'Vertex Mass', 'manual_ranges': [0, 20], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 20, 'inputVar_units': 'GeV'},
      'DeepCSV_trackSip3dSig_3':
       {'displayname': 'Track SIP 3D Sig [3]', 'manual_ranges': [-25, 50], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackDecayLenVal_1':
       {'displayname': 'Track Decay Len Val [1]', 'manual_ranges': [-0.1, 1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 22, 'inputVar_units': 'cm'},
      'DeepCSV_trackDecayLenVal_0':
       {'displayname': 'Track Decay Len Val [0]', 'manual_ranges': [-0.1, 1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 22, 'inputVar_units': 'cm'},
      'DeepCSV_trackDecayLenVal_3':
       {'displayname': 'Track Decay Len Val [3]', 'manual_ranges': [-0.1, 1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 22, 'inputVar_units': 'cm'},
      'DeepCSV_trackDecayLenVal_2':
       {'displayname': 'Track Decay Len Val [2]', 'manual_ranges': [-0.1, 1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 22, 'inputVar_units': 'cm'},
      'DeepCSV_trackPtRel_0':
       {'displayname': 'Track $p_{T,rel}$ [0]', 'manual_ranges': [-0.1, 3.1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 32, 'inputVar_units': 'GeV'},
      'pt':
       {'displayname': 'Jet $p_T$', 'manual_ranges': [0, 250], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 0, 'bins': 50, 'inputVar_units': 'GeV'},
      'DeepCSV_jetNTracksEtaRel':
       {'displayname': 'Jet N Tracks $\\eta_{rel}$', 'manual_ranges': [-0.5, None], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSig_0':
       {'displayname': 'Track SIP 2D Sig [0]', 'manual_ranges': [-4.5, 16], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 21, 'inputVar_units': ''},
      'DeepCSV_trackSip3dSigAboveCharm':
       {'displayname': 'Track SIP 3D Sig Above Charm', 'manual_ranges': [-6.5, 6.5], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 26, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSig_3':
       {'displayname': 'Track SIP 2D Sig [3]', 'manual_ranges': [-6, 7], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 26, 'inputVar_units': ''},
      'DeepCSV_trackSip3dSig_4':
       {'displayname': 'Track SIP 3D Sig [4]', 'manual_ranges': [-25, 50], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackSip3dSig_5':
       {'displayname': 'Track SIP 3D Sig [5]', 'manual_ranges': [-25, 50], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSig_2':
       {'displayname': 'Track SIP 2D Sig [2]', 'manual_ranges': [-5.5, 10], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 16, 'inputVar_units': ''},
      'DeepCSV_trackSip2dValAboveCharm':
       {'displayname': 'Track SIP 2D Val Above Charm', 'manual_ranges': [-0.06, 0.06], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 24, 'inputVar_units': 'cm'},
      'DeepCSV_trackSip3dSig_1':
       {'displayname': 'Track SIP 3D Sig [1]', 'manual_ranges': [-25, 50], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackSip3dSig_2':
       {'displayname': 'Track SIP 3D Sig [2]', 'manual_ranges': [-25, 50], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'eta':
       {'displayname': 'Jet $\\eta$', 'manual_ranges': [None, None], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSig_1':
       {'displayname': 'Track SIP 2D Sig [1]', 'manual_ranges': [-5, 13], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 18, 'inputVar_units': ''},
      'DeepCSV_trackSip2dSigAboveCharm':
       {'displayname': 'Track SIP 2D Sig Above Charm', 'manual_ranges': [-5.5, 5.5], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 22, 'inputVar_units': ''},
      'DeepCSV_trackDeltaR_4':
       {'displayname': 'Track $\\Delta R$ [4]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackDeltaR_5':
       {'displayname': 'Track $\\Delta R$ [5]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackDeltaR_2':
       {'displayname': 'Track $\\Delta R$ [2]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackDeltaR_3':
       {'displayname': 'Track $\\Delta R$ [3]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackDeltaR_0':
       {'displayname': 'Track $\\Delta R$ [0]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_flightDistance3dVal':
       {'displayname': 'Flight Distance 3D Val', 'manual_ranges': [-0.1, 5], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 51, 'inputVar_units': 'cm'},
      'DeepCSV_flightDistance3dSig':
       {'displayname': 'Flight Distance 3D Sig', 'manual_ranges': [-0.1, 100], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 1, 'bins': 100, 'inputVar_units': ''},
      'DeepCSV_jetNSecondaryVertices':
       {'displayname': 'Jet N Secondary Vertices', 'manual_ranges': [-0.5, None], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 25, 'inputVar_units': ''},
      'DeepCSV_trackPtRel_2':
       {'displayname': 'Track $p_{T,rel}$ [2]', 'manual_ranges': [-0.1, 3.1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 32, 'inputVar_units': 'GeV'},
      'DeepCSV_trackDeltaR_1':
       {'displayname': 'Track $\\Delta R$ [1]', 'manual_ranges': [-0.001, 0.301], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackPtRel_3':
       {'displayname': 'Track $p_{T,rel}$ [3]', 'manual_ranges': [-0.1, 3.1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 32, 'inputVar_units': 'GeV'},
      'DeepCSV_vertexCategory':
       {'displayname': 'Vertex Category', 'manual_ranges': [-0.6, 2.6], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 26, 'inputVar_units': ''},
      'DeepCSV_flightDistance2dVal':
       {'displayname': 'Flight Distance 2D Val', 'manual_ranges': [-0.1, 2.6], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 27, 'inputVar_units': 'cm'},
      'DeepCSV_trackPtRel_5':
       {'displayname': 'Track $p_{T,rel}$ [5]', 'manual_ranges': [-0.1, 3.1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 32, 'inputVar_units': 'GeV'},
      'DeepCSV_trackEtaRel_3':
       {'displayname': 'Track $\\eta_{rel}$ [3]', 'manual_ranges': [-0.0, 9], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackEtaRel_2':
       {'displayname': 'Track $\\eta_{rel}$ [2]', 'manual_ranges': [-0.0, 9], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackEtaRel_1':
       {'displayname': 'Track $\\eta_{rel}$ [1]', 'manual_ranges': [-0.0, 9], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackEtaRel_0':
       {'displayname': 'Track $\\eta_{rel}$ [0]', 'manual_ranges': [-0.0, 9], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 30, 'inputVar_units': ''},
      'DeepCSV_trackJetDistVal_4':
       {'displayname': 'Track Jet Dist Val [4]', 'manual_ranges': [-0.08, 0.0025], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 4, 'bins': 35, 'inputVar_units': 'cm'},
      'DeepCSV_trackJetDistVal_5':
       {'displayname': 'Track Jet Dist Val [5]', 'manual_ranges': [-0.08, 0.0025], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 4, 'bins': 35, 'inputVar_units': 'cm'},
      'DeepCSV_trackPtRel_1':
       {'displayname': 'Track $p_{T,rel}$ [1]', 'manual_ranges': [-0.1, 3.1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 32, 'inputVar_units': 'GeV'},
      'DeepCSV_trackJetDistVal_0':
       {'displayname': 'Track Jet Dist Val [0]', 'manual_ranges': [-0.08, 0.0025], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 4, 'bins': 35, 'inputVar_units': 'cm'},
      'DeepCSV_trackJetDistVal_1':
       {'displayname': 'Track Jet Dist Val [1]', 'manual_ranges': [-0.08, 0.0025], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 4, 'bins': 35, 'inputVar_units': 'cm'},
      'DeepCSV_trackJetDistVal_2':
       {'displayname': 'Track Jet Dist Val [2]', 'manual_ranges': [-0.08, 0.0025], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 4, 'bins': 35, 'inputVar_units': 'cm'},
      'DeepCSV_trackJetDistVal_3':
       {'displayname': 'Track Jet Dist Val [3]', 'manual_ranges': [-0.08, 0.0025], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 4, 'bins': 35, 'inputVar_units': 'cm'},
      'DeepCSV_flightDistance2dSig':
       {'displayname': 'Flight Distance 2D Sig', 'manual_ranges': [-0.1, 100], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 1, 'bins': 101, 'inputVar_units': ''},
      'DeepCSV_trackPtRel_4':
       {'displayname': 'Track $p_{T,rel}$ [4]', 'manual_ranges': [-0.1, 3.1], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 2, 'bins': 32, 'inputVar_units': 'GeV'},
      'DeepCSV_trackSip3dValAboveCharm':
       {'displayname': 'Track SIP 3D Val Above Charm', 'manual_ranges': [-0.06, 0.06], 'ylabel_text': 'Tracks', 'format_unit': '2f', 'format_unit_digits': 3, 'bins': 24, 'inputVar_units': 'cm'},
      'DeepCSV_trackJetPt':
       {'displayname': 'Track Jet $p_T$', 'manual_ranges': [0, 250], 'ylabel_text': 'Jets', 'format_unit': '2f', 'format_unit_digits': 1, 'bins': 50, 'inputVar_units': 'GeV'}}
      return definitions_dict
