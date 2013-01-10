"""
Bulky data structures for assertion in pyteomics test suites.
"""

pepxml_spectra = [
            {'spectrum': 'pps_sl20060731_18mix_25ul_r1_1154456409.0100.0100.1',
             'end_scan': 100, 
             'start_scan': 100, 
             'index': 1,
             'assumed_charge': 1,
             'precursor_neutral_mass': 860.392,
             'search_hit': [{
             'num_missed_cleavages': 0, 
             'tot_num_ions': 12, 
             'is_rejected': False,
             'search_score': {
                'deltacn': 0.081,
                'sprank': 1.0, 
                'deltacnstar': 0.0, 
                'spscore': 894.0, 
                'xcorr': 1.553},
             'hit_rank': 1, 
             'num_matched_ions': 11, 
             'num_tot_proteins': 1, 
             'peptide': 'SLNGEWR', 
             'massdiff': -0.5, 
             'analysis_result': [{'analysis': 'peptideprophet',
                 'peptideprophet_result':
                 {'all_ntt_prob': [0.0422, 0.509, 0.96],
                  'parameter': 
                    {'fval': 1.4723, 'massd': -0.5, 'nmc': 0.0, 'ntt': 2.0},
                  'probability': 0.96}}],
             'modifications': [],
             'modified_peptide': 'SLNGEWR', 
             'proteins': [{'num_tol_term': 2,
                           'protein': 'sp|P00722|BGAL_ECOLI',
                           'peptide_prev_aa': 'R',
                           'protein_descr': 'BETA-GALACTOSIDASE (EC 3.2.1.23) '
                                            '(LACTASE) - Escherichia coli.',
                           'peptide_next_aa': 'F'}], 
             'calc_neutral_pep_mass': 860.892}]}, 
            {'precursor_neutral_mass': 677.392,
             'spectrum': 'pps_sl20060731_18mix_25ul_r1_1154456409.0040.0040.1',
             'start_scan': 40, 
             'assumed_charge': 1, 
             'index': 2,
             'end_scan': 40,
             'search_hit': [{'tot_num_ions': 10,
             'num_missed_cleavages': 1,
             'is_rejected': False,
             'hit_rank': 1,
             'num_matched_ions': 8,
             'search_score': {
                'sprank': 1.0,
                'deltacn': 0.165,
                'deltacnstar': 0.0,
                'spscore': 427.0,
                'xcorr': 1.644},
             'num_tot_proteins': 1,
             'peptide': 'GKKFAK', 
             'massdiff': -0.5,
             'analysis_result': [{'analysis': 'peptideprophet',
              'peptideprophet_result': {
                  'all_ntt_prob': [0.0491, 0.548, 0.9656],
                  'parameter': {
                      'fval': 2.0779, 'massd': -0.5, 'nmc': 1.0, 'ntt': 1.0},
                  'probability': 0.548}}],
             'modifications': [],
             'modified_peptide': 'GKKFAK', 
             'proteins': [{'num_tol_term': 1,
                           'protein': 'gi|3212198|gb|AAC22319.1|', 
                           'peptide_prev_aa': 'N', 
                           'protein_descr': 'hemoglobin-binding protein '
                                            '[Haemophilus influenzae Rd]',
                           'peptide_next_aa': 'I'}],
             'calc_neutral_pep_mass': 677.892}]},
              {'assumed_charge': 2,
             'end_scan': 1366,
             'index': 29,
             'precursor_neutral_mass': 718.4136,
             'retention_time_sec': 38.426123,
             'search_hit': [{'calc_neutral_pep_mass': 718.4126,
               'search_score': {
                   'expect': 0.0,
                   'homologyscore': 46.61,
                   'identityscore': 25.38,
                   'star': 0.0,
                   'ionscore': 36.45},
               'hit_rank': 1,
               'is_rejected': False,
               'massdiff': 0.0011,
               'modifications': [],
               'modified_peptide': 'VGQFIR',
               'num_matched_ions': 5,
               'num_missed_cleavages': 0,
               'num_tot_proteins': 1,
               'peptide': 'VGQFIR',
               'analysis_result': [{'analysis': 'peptideprophet',
                    'peptideprophet_result':
                    {'all_ntt_prob': [0., 0.5741, 0.7264],
                      'parameter': {
                      'fval': 0.6052, 'massd': 0.001, 'nmc': 0.0, 'ntt': 2.0},
                    'probability': 0.7264}}],
               'proteins': [{'num_tol_term': 2,
                 'peptide_next_aa': 'L',
                 'peptide_prev_aa': 'K',
                 'protein': 'IPI00200898',
                 'protein_descr': None}],
               'tot_num_ions': 10}],
             'spectrum': 'MASCOT',
             'start_scan': 1366},
             {'assumed_charge': 2,
             'end_scan': 6862,
             'index': 49,
             'precursor_neutral_mass': 1404.7476,
             'search_hit': [{'search_score': {
                   'bscore': 2.0,
                   'expect': 0.012,
                   'nextscore': 14.6,
                   'hyperscore': 23.5,
                   'yscore': 8.7},
               'calc_neutral_pep_mass': 1404.7435,
               'hit_rank': 1,
               'is_rejected': False,
               'massdiff': 0.004,
               'modifications': [{'mass': 147.0354, 'position': 10}],
               'modified_peptide': 'EVPLNTIIFMGR',
               'num_matched_ions': 8,
               'num_missed_cleavages': 0,
               'num_tot_proteins': 2,
               'peptide': 'EVPLNTIIFMGR',
               'proteins': [{'num_tol_term': 2,
                 'peptide_next_aa': 'V',
                 'peptide_prev_aa': 'R',
                 'protein': 'sp|P01008|ANT3_HUMAN',
                 'protein_descr': 'Antithrombin-III OS=Homo sapiens GN=SERPINC1 PE=1 SV=1'},
                {'num_tol_term': 2, 'protein': 'tr|Q8TCE1|Q8TCE1_HUMAN', 'protein_descr': 'SERPINC1 protein OS=Homo sapiens GN=SERPINC1 PE=2 SV=1'}],
               'tot_num_ions': 22}],
             'spectrum': 'X!Tandem',
             'start_scan': 6862},
            {'assumed_charge': 3,
             'end_scan': 23,
             'index': 3,
             'precursor_neutral_mass': 3254.044921875,
             'search_hit': [{'calc_neutral_pep_mass': 3254.04711914062,
                 'search_score': {
                   'expect': 13690.946579388728,
                   'pvalue': 59.52585469299447},
               'hit_rank': 1,
               'is_rejected': False,
               'massdiff': -0.002197265625,
               'modifications': [{'mass': 166.99803, 'position': 6},
                {'mass': 166.99803, 'position': 7},
                {'mass': 166.99803, 'position': 9},
                {'mass': 160.03019, 'position': 15},
                {'mass': 160.03019, 'position': 21}],
               'modified_peptide': 'DQQFDS[166]S[166]SS[166]MALEDCGEETNCQSDFK',
               'num_matched_ions': 3,
               'num_tot_proteins': 1,
               'peptide': 'DQQFDSSSSMALEDCGEETNCQSDFK',
               'proteins': [{'num_tol_term': 0,
                 'peptide_next_aa': 'I',
                 'peptide_prev_aa': 'R',
                 'protein': 'BL_ORD_ID:125453',
                 'protein_descr': 'sp|O43149|ZZEF1_HUMAN Zinc finger ZZ-type and EF-hand domain-containing protein 1 OS=Homo sapiens GN=ZZEF1 PE=1 SV=6:reversed'}],
               'tot_num_ions': 50},
              {'calc_neutral_pep_mass': 3254.04711914062,
                  'search_score': {'expect': 14837.682803311733,
                   'pvalue': 64.51166436222492},
               'hit_rank': 2,
               'is_rejected': False,
               'massdiff': -0.002197265625,
               'modifications': [{'mass': 243.02933, 'position': 6},
                {'mass': 170.10596, 'position': 8},
                {'mass': 181.01368, 'position': 11},
                {'mass': 181.01368, 'position': 13},
                {'mass': 181.01368, 'position': 18},
                {'mass': 181.01368, 'position': 21},
                {'mass': 160.03019, 'position': 1},
                {'mass': 160.03019, 'position': 4}],
               'modified_peptide': 'CENCNY[243]PK[170]EGT[181]HT[181]NQHET[181]LHT[181]SR',
               'num_matched_ions': 6,
               'num_tot_proteins': 2,
               'peptide': 'CENCNYPKEGTHTNQHETLHTSR',
               'proteins': [{'num_tol_term': 0,
                 'peptide_next_aa': 'S',
                 'peptide_prev_aa': 'R',
                 'protein': 'BL_ORD_ID:144314',
                 'protein_descr': 'tr|Q6ZND3|Q6ZND3_HUMAN Zinc finger protein 184 OS=Homo sapiens GN=ZNF184 PE=2 SV=1:reversed'},
                {'protein': 'BL_ORD_ID:154629', 'protein_descr': 'sp|Q99676|ZN184_HUMAN Zinc finger protein 184 OS=Homo sapiens GN=ZNF184 PE=1 SV=4:reversed'}],
               'tot_num_ions': 44}],
             'spectrum': ' Cmpd 24, +MSn(1085.6886), 1.2 min.23.23.3',
             'start_scan': 23}]

mzid_spectra = [
           {'SpectrumIdentificationItem': [
               {'ProteinScape:IntensityCoverage': 0.3919545603809718, 
                'PeptideEvidenceRef': [{'peptideEvidence_ref': 'PE1_SEQ_spec1_pep1'}],
                'passThreshold': True, 
                'rank': 1, 'chargeState': 1, 
                'calculatedMassToCharge': 1507.695, 
                'peptide_ref': 'prot1_pep1', 
                'experimentalMassToCharge': 1507.696, 
                'id': 'SEQ_spec1_pep1', 
                'ProteinScape:SequestMetaScore': 7.59488518903425}], 
            'spectrumID': 'databasekey=1', 
            'id': 'SEQ_spec1', 
            'spectraData_ref': 'LCMALDI_spectra'},
 
            {'SpectrumIdentificationItem': [
                {'ProteinScape:IntensityCoverage': 0.5070386909133888, 
                'PeptideEvidenceRef': [{'peptideEvidence_ref': 'PE1_SEQ_spec2a_pep1'}], 
                'passThreshold': True, 
                'rank': 1, 
                'chargeState': 1, 
                'calculatedMassToCharge': 1920.9224, 
                'peptide_ref': 'prot1_pep2', 
                'experimentalMassToCharge': 1920.923, 
                'id': 'SEQ_spec2a_pep1', 'ProteinScape:SequestMetaScore': 10.8810331335713}], 
            'spectrumID': 'databasekey=2', 
            'id': 'SEQ_spec2a', 
            'spectraData_ref': 'LCMALDI_spectra'}, 

            {'SpectrumIdentificationItem': [
                {'ProteinScape:IntensityCoverage': 0.43376827663349576, 
                'PeptideEvidenceRef': [{'peptideEvidence_ref': 'PE1_SEQ_spec3a_pep1'}], 
                'passThreshold': True, 
                'rank': 1, 
                'chargeState': 1, 
                'calculatedMassToCharge': 864.4752, 
                'peptide_ref': 'prot1_pep3', 
                'experimentalMassToCharge': 864.474, 
                'id': 'SEQ_spec3a_pep1', 
                'ProteinScape:SequestMetaScore': 6.1021771936508955}], 
            'spectrumID': 'databasekey=3', 
            'id': 'SEQ_spec3a', 
            'spectraData_ref': 'LCMALDI_spectra'}, 

            {'SpectrumIdentificationItem': 
                [{'ProteinScape:IntensityCoverage': 0.16164593872706742, 
                'PeptideEvidenceRef': [{'peptideEvidence_ref': 'PE1_SEQ_spec10_pep1'}], 
                'passThreshold': True, 
                'rank': 1, 
                'chargeState': 1, 
                'calculatedMassToCharge': 1832.862115, 
                'peptide_ref': 'prot1_pep4', 
                'experimentalMassToCharge': 1832.863, 
                'id': 'SEQ_spec10_pep1', 'ProteinScape:SequestMetaScore': 5.635013787097159}], 
                'spectrumID': 'databasekey=10', 
                'id': 'SEQ_spec10', 
                'spectraData_ref': 'LCMALDI_spectra'}]