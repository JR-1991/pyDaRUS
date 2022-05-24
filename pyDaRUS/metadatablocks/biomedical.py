# generated by datamodel-codegen:
#   filename:  biomedical.json
#   timestamp: 2022-05-24T09:26:50+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from easyDataverse.core import DataverseBase
from pydantic import Field


class DesignType(Enum):
    """
    Design types that are based on the overall experimental design.
    """

    case__control = 'Case Control'
    cross__sectional = 'Cross Sectional'
    cohort__study = 'Cohort Study'
    nested__case__control__design = 'Nested Case Control Design'
    not__specified = 'Not Specified'
    parallel__group__design = 'Parallel Group Design'
    perturbation__design = 'Perturbation Design'
    randomized__controlled__trial = 'Randomized Controlled Trial'
    technological__design = 'Technological Design'
    other = 'Other'


class FactorType(Enum):
    """
    Factors used in the Dataset.
    """

    age = 'Age'
    biomarkers = 'Biomarkers'
    cell__surface__markers = 'Cell Surface Markers'
    cell__type__cell__line = 'Cell Type/Cell Line'
    developmental__stage = 'Developmental Stage'
    disease__state = 'Disease State'
    drug__susceptibility = 'Drug Susceptibility'
    extract__molecule = 'Extract Molecule'
    genetic__characteristics = 'Genetic Characteristics'
    immunoprecipitation__antibody = 'Immunoprecipitation Antibody'
    organism = 'Organism'
    passages = 'Passages'
    platform = 'Platform'
    sex = 'Sex'
    strain = 'Strain'
    time__point = 'Time Point'
    tissue__type = 'Tissue Type'
    treatment__compound = 'Treatment Compound'
    treatment__type = 'Treatment Type'
    other = 'Other'


class Organism(Enum):
    """
    The taxonomic name of the organism used in the Dataset or from which the  starting biological material derives.
    """

    arabidopsis_thaliana = 'Arabidopsis thaliana'
    bos_taurus = 'Bos taurus'
    caenorhabditis_elegans = 'Caenorhabditis elegans'
    chlamydomonas_reinhardtii = 'Chlamydomonas reinhardtii'
    danio_rerio__zebrafish_ = 'Danio rerio (zebrafish)'
    dictyostelium_discoideum = 'Dictyostelium discoideum'
    drosophila_melanogaster = 'Drosophila melanogaster'
    escherichia_coli = 'Escherichia coli'
    hepatitis_c_virus = 'Hepatitis C virus'
    homo_sapiens = 'Homo sapiens'
    mus_musculus = 'Mus musculus'
    mycobacterium_africanum = 'Mycobacterium africanum'
    mycobacterium_canetti = 'Mycobacterium canetti'
    mycobacterium_tuberculosis = 'Mycobacterium tuberculosis'
    mycoplasma_pneumoniae = 'Mycoplasma pneumoniae'
    oryza_sativa = 'Oryza sativa'
    plasmodium_falciparum = 'Plasmodium falciparum'
    pneumocystis_carinii = 'Pneumocystis carinii'
    rattus_norvegicus = 'Rattus norvegicus'
    saccharomyces_cerevisiae__brewer_s_yeast_ = (
        'Saccharomyces cerevisiae (brewer\'s yeast)'
    )
    schizosaccharomyces_pombe = 'Schizosaccharomyces pombe'
    takifugu_rubripes = 'Takifugu rubripes'
    xenopus_laevis = 'Xenopus laevis'
    zea_mays = 'Zea mays'
    other = 'Other'


class MeasurementType(Enum):
    """
    A term to qualify the endpoint, or what is being measured (e.g. gene expression profiling; protein identification).
    """

    cell_sorting = 'cell sorting'
    clinical_chemistry_analysis = 'clinical chemistry analysis'
    copy_number_variation_profiling = 'copy number variation profiling'
    dna_methylation_profiling = 'DNA methylation profiling'
    dna_methylation_profiling___bisulfite__seq_ = (
        'DNA methylation profiling (Bisulfite-Seq)'
    )
    dna_methylation_profiling___me_dip__seq_ = 'DNA methylation profiling (MeDIP-Seq)'
    drug_susceptibility = 'drug susceptibility'
    environmental_gene_survey = 'environmental gene survey'
    genome_sequencing = 'genome sequencing'
    hematology = 'hematology'
    histology = 'histology'
    histone__modification___ch_ip__seq_ = 'Histone Modification (ChIP-Seq)'
    loss_of_heterozygosity_profiling = 'loss of heterozygosity profiling'
    metabolite_profiling = 'metabolite profiling'
    metagenome_sequencing = 'metagenome sequencing'
    protein_expression_profiling = 'protein expression profiling'
    protein_identification = 'protein identification'
    protein_dna_binding_site_identification = 'protein-DNA binding site identification'
    protein_protein_interaction_detection = 'protein-protein interaction detection'
    protein_rna_binding__rip__seq_ = 'protein-RNA binding (RIP-Seq)'
    snp_analysis = 'SNP analysis'
    targeted_sequencing = 'targeted sequencing'
    transcription_factor_binding___ch_ip__seq_ = (
        'transcription factor binding (ChIP-Seq)'
    )
    transcription_factor_binding_site_identification = (
        'transcription factor binding site identification'
    )
    transcription_profiling = 'transcription profiling'
    transcription_profiling_1 = 'transcription profiling'
    transcription_profiling___microarray_ = 'transcription profiling (Microarray)'
    transcription_profiling__rna__seq_ = 'transcription profiling (RNA-Seq)'
    trap_translational_profiling = 'TRAP translational profiling'
    other = 'Other'


class TechnologyType(Enum):
    """
    A term to identify the technology used to perform the measurement (e.g. DNA microarray; mass spectrometry).
    """

    culture_based_drug_susceptibility_testing__single_concentration = (
        'culture based drug susceptibility testing, single concentration'
    )
    culture_based_drug_susceptibility_testing__two_concentrations = (
        'culture based drug susceptibility testing, two concentrations'
    )
    culture_based_drug_susceptibility_testing__three_or_more_concentrations__minimium_inhibitory_concentration_measurement_ = 'culture based drug susceptibility testing, three or more concentrations (minimium inhibitory concentration measurement)'
    dna_microarray = 'DNA microarray'
    flow_cytometry = 'flow cytometry'
    gel_electrophoresis = 'gel electrophoresis'
    mass_spectrometry = 'mass spectrometry'
    nmr_spectroscopy = 'NMR spectroscopy'
    nucleotide_sequencing = 'nucleotide sequencing'
    protein_microarray = 'protein microarray'
    real_time_pcr = 'real time PCR'
    no_technology_required = 'no technology required'
    other = 'Other'


class TechnologyPlatform(Enum):
    """
    The manufacturer and name of the technology platform used in the assay (e.g. Bruker AVANCE).
    """

    field_210_ms_gc__ion__trap___varian_ = '210-MS GC Ion Trap (Varian)'
    field_220_ms_gc__ion__trap___varian_ = '220-MS GC Ion Trap (Varian)'
    field_225_ms_gc__ion__trap___varian_ = '225-MS GC Ion Trap (Varian)'
    field_240_ms_gc__ion__trap___varian_ = '240-MS GC Ion Trap (Varian)'
    field_300_ms_quadrupole_gc_ms___varian_ = '300-MS quadrupole GC/MS (Varian)'
    field_320_ms_lc_ms___varian_ = '320-MS LC/MS (Varian)'
    field_325_ms_lc_ms___varian_ = '325-MS LC/MS (Varian)'
    field_320_ms_gc_ms___varian_ = '320-MS GC/MS (Varian)'
    field_500_ms_lc_ms___varian_ = '500-MS LC/MS (Varian)'
    field_800_d___jeol_ = '800D (Jeol)'
    field_910_ms_tq_ft___varian_ = '910-MS TQ-FT (Varian)'
    field_920_ms_tq_ft___varian_ = '920-MS TQ-FT (Varian)'
    field_3100__mass__detector___waters_ = '3100 Mass Detector (Waters)'
    field_6110__quadrupole_lc_ms___agilent_ = '6110 Quadrupole LC/MS (Agilent)'
    field_6120__quadrupole_lc_ms___agilent_ = '6120 Quadrupole LC/MS (Agilent)'
    field_6130__quadrupole_lc_ms___agilent_ = '6130 Quadrupole LC/MS (Agilent)'
    field_6140__quadrupole_lc_ms___agilent_ = '6140 Quadrupole LC/MS (Agilent)'
    field_6310__ion__trap_lc_ms___agilent_ = '6310 Ion Trap LC/MS (Agilent)'
    field_6320__ion__trap_lc_ms___agilent_ = '6320 Ion Trap LC/MS (Agilent)'
    field_6330__ion__trap_lc_ms___agilent_ = '6330 Ion Trap LC/MS (Agilent)'
    field_6340__ion__trap_lc_ms___agilent_ = '6340 Ion Trap LC/MS (Agilent)'
    field_6410__triple__quadrupole_lc_ms___agilent_ = (
        '6410 Triple Quadrupole LC/MS (Agilent)'
    )
    field_6430__triple__quadrupole_lc_ms___agilent_ = (
        '6430 Triple Quadrupole LC/MS (Agilent)'
    )
    field_6460__triple__quadrupole_lc_ms___agilent_ = (
        '6460 Triple Quadrupole LC/MS (Agilent)'
    )
    field_6490__triple__quadrupole_lc_ms___agilent_ = (
        '6490 Triple Quadrupole LC/MS (Agilent)'
    )
    field_6530_q_tof_lc_ms___agilent_ = '6530 Q-TOF LC/MS (Agilent)'
    field_6540_q_tof_lc_ms___agilent_ = '6540 Q-TOF LC/MS (Agilent)'
    field_6210_tof_lc_ms___agilent_ = '6210 TOF LC/MS (Agilent)'
    field_6220_tof_lc_ms___agilent_ = '6220 TOF LC/MS (Agilent)'
    field_6230_tof_lc_ms___agilent_ = '6230 TOF LC/MS (Agilent)'
    field_7000_b__triple__quadrupole_gc_ms___agilent_ = (
        '7000B Triple Quadrupole GC/MS (Agilent)'
    )
    accu_to_dart___jeol_ = 'AccuTO DART (Jeol)'
    accu_tof_gc___jeol_ = 'AccuTOF GC (Jeol)'
    accu_tof_lc___jeol_ = 'AccuTOF LC (Jeol)'
    acquity_sqd___waters_ = 'ACQUITY SQD (Waters)'
    acquity_tqd___waters_ = 'ACQUITY TQD (Waters)'
    agilent = 'Agilent'
    agilent_5975_e_gc_msd___agilent_ = 'Agilent 5975E GC/MSD (Agilent)'
    agilent_5975_t_ltm_gc_msd___agilent_ = 'Agilent 5975T LTM GC/MSD (Agilent)'
    field_5975_c__series_gc_msd___agilent_ = '5975C Series GC/MSD (Agilent)'
    affymetrix = 'Affymetrix'
    ama_zon_etd_esi__ion__trap___bruker_ = 'amaZon ETD ESI Ion Trap (Bruker)'
    ama_zon_x_esi__ion__trap___bruker_ = 'amaZon X ESI Ion Trap (Bruker)'
    apex_ultra_hybrid__qq_ftms___bruker_ = 'apex-ultra hybrid Qq-FTMS (Bruker)'
    api_2000__ab__sciex_ = 'API 2000 (AB Sciex)'
    api_3200__ab__sciex_ = 'API 3200 (AB Sciex)'
    api_3200_qtrap__ab__sciex_ = 'API 3200 QTRAP (AB Sciex)'
    api_4000__ab__sciex_ = 'API 4000 (AB Sciex)'
    api_4000_qtrap__ab__sciex_ = 'API 4000 QTRAP (AB Sciex)'
    api_5000__ab__sciex_ = 'API 5000 (AB Sciex)'
    api_5500__ab__sciex_ = 'API 5500 (AB Sciex)'
    api_5500_qtrap__ab__sciex_ = 'API 5500 QTRAP (AB Sciex)'
    applied__biosystems__group__abi_ = 'Applied Biosystems Group (ABI)'
    aqi__biosciences = 'AQI Biosciences'
    atmospheric__pressure_gc___waters_ = 'Atmospheric Pressure GC (Waters)'
    autoflex_iii_maldi_tof_ms___bruker_ = 'autoflex III MALDI-TOF MS (Bruker)'
    autoflex_speed__bruker_ = 'autoflex speed(Bruker)'
    auto_spec__premier___waters_ = 'AutoSpec Premier (Waters)'
    axima__mega_tof___shimadzu_ = 'AXIMA Mega TOF (Shimadzu)'
    axima__performance_maldi_tof_tof___shimadzu_ = (
        'AXIMA Performance MALDI TOF/TOF (Shimadzu)'
    )
    a_10__analyzer___apogee_ = 'A-10 Analyzer (Apogee)'
    a_40__mini_fcm___apogee_ = 'A-40-MiniFCM (Apogee)'
    bactiflow___chemunex_sa_ = 'Bactiflow (Chemunex SA)'
    base4innovation = 'Base4innovation'
    bd_bactec_mgit_320 = 'BD BACTEC MGIT 320'
    bd_bactec_mgit_960 = 'BD BACTEC MGIT 960'
    bd__radiometric_bactec_460_tb = 'BD Radiometric BACTEC 460TB'
    bio_nanomatrix = 'BioNanomatrix'
    cell__lab__quanta_sc___becman__coulter_ = 'Cell Lab Quanta SC (Becman Coulter)'
    clarus_560_d_gc_ms___perkin_elmer_ = 'Clarus 560 D GC/MS (PerkinElmer)'
    clarus_560_s_gc_ms___perkin_elmer_ = 'Clarus 560 S GC/MS (PerkinElmer)'
    clarus_600_gc_ms___perkin_elmer_ = 'Clarus 600 GC/MS (PerkinElmer)'
    complete__genomics = 'Complete Genomics'
    cyan___dako__cytomation_ = 'Cyan (Dako Cytomation)'
    cy_flow_ml___partec_ = 'CyFlow ML (Partec)'
    cyow_sl___partec_ = 'Cyow SL (Partec)'
    cy_flow_sl3___partec_ = 'CyFlow SL3 (Partec)'
    cyto_buoy___cyto__buoy__inc_ = 'CytoBuoy (Cyto Buoy Inc)'
    cyto_sence___cyto__buoy__inc_ = 'CytoSence (Cyto Buoy Inc)'
    cyto_sub___cyto__buoy__inc_ = 'CytoSub (Cyto Buoy Inc)'
    danaher = 'Danaher'
    dfs___thermo__scientific_ = 'DFS (Thermo Scientific)'
    exactive__thermo__scientific_ = 'Exactive(Thermo Scientific)'
    facs__canto___becton__dickinson_ = 'FACS Canto (Becton Dickinson)'
    facs__canto2___becton__dickinson_ = 'FACS Canto2 (Becton Dickinson)'
    facs__scan___becton__dickinson_ = 'FACS Scan (Becton Dickinson)'
    fc_500___becman__coulter_ = 'FC 500 (Becman Coulter)'
    g_cmate_ii_gc_ms___jeol_ = 'GCmate II GC/MS (Jeol)'
    gcms_qp2010__plus___shimadzu_ = 'GCMS-QP2010 Plus (Shimadzu)'
    gcms_qp2010_s__plus___shimadzu_ = 'GCMS-QP2010S Plus (Shimadzu)'
    gct__premier___waters_ = 'GCT Premier (Waters)'
    geneq = 'GENEQ'
    genome__corp_ = 'Genome Corp.'
    geno_voxx = 'GenoVoxx'
    gnu_bio = 'GnuBio'
    guava__easy_cyte__mini___millipore_ = 'Guava EasyCyte Mini (Millipore)'
    guava__easy_cyte__plus___millipore_ = 'Guava EasyCyte Plus (Millipore)'
    guava__personal__cell__analysis___millipore_ = (
        'Guava Personal Cell Analysis (Millipore)'
    )
    guava__personal__cell__analysis_96___millipore_ = (
        'Guava Personal Cell Analysis-96 (Millipore)'
    )
    helicos__bio_sciences = 'Helicos BioSciences'
    illumina = 'Illumina'
    indirect_proportion_method_on_lj_medium = 'Indirect proportion method on LJ medium'
    indirect_proportion_method_on__middlebrook__agar_7_h9 = (
        'Indirect proportion method on Middlebrook Agar 7H9'
    )
    indirect_proportion_method_on__middlebrook__agar_7_h10 = (
        'Indirect proportion method on Middlebrook Agar 7H10'
    )
    indirect_proportion_method_on__middlebrook__agar_7_h11 = (
        'Indirect proportion method on Middlebrook Agar 7H11'
    )
    in_flux__analyzer___cytopeia_ = 'inFlux Analyzer (Cytopeia)'
    intelligent__bio__systems = 'Intelligent Bio-Systems'
    itq_700___thermo__scientific_ = 'ITQ 700 (Thermo Scientific)'
    itq_900___thermo__scientific_ = 'ITQ 900 (Thermo Scientific)'
    itq_1100___thermo__scientific_ = 'ITQ 1100 (Thermo Scientific)'
    jms_53000__spiral_tof___jeol_ = 'JMS-53000 SpiralTOF (Jeol)'
    laser_gen = 'LaserGen'
    lcms_2020___shimadzu_ = 'LCMS-2020 (Shimadzu)'
    lcms_2010_ev___shimadzu_ = 'LCMS-2010EV (Shimadzu)'
    lcms_it_tof___shimadzu_ = 'LCMS-IT-TOF (Shimadzu)'
    li__cor = 'Li-Cor'
    life__tech = 'Life Tech'
    light_speed__genomics = 'LightSpeed Genomics'
    lct__premier_xe___waters_ = 'LCT Premier XE (Waters)'
    lcq__deca_xp_max___thermo__scientific_ = 'LCQ Deca XP MAX (Thermo Scientific)'
    lcq__fleet___thermo__scientific_ = 'LCQ Fleet (Thermo Scientific)'
    lxq___thermo__scientific_ = 'LXQ (Thermo Scientific)'
    ltq__classic___thermo__scientific_ = 'LTQ Classic (Thermo Scientific)'
    ltq_xl___thermo__scientific_ = 'LTQ XL (Thermo Scientific)'
    ltq__velos___thermo__scientific_ = 'LTQ Velos (Thermo Scientific)'
    ltq__orbitrap__classic___thermo__scientific_ = (
        'LTQ Orbitrap Classic (Thermo Scientific)'
    )
    ltq__orbitrap_xl___thermo__scientific_ = 'LTQ Orbitrap XL (Thermo Scientific)'
    ltq__orbitrap__discovery___thermo__scientific_ = (
        'LTQ Orbitrap Discovery (Thermo Scientific)'
    )
    ltq__orbitrap__velos___thermo__scientific_ = (
        'LTQ Orbitrap Velos (Thermo Scientific)'
    )
    luminex_100___luminex_ = 'Luminex 100 (Luminex)'
    luminex_200___luminex_ = 'Luminex 200 (Luminex)'
    macs__quant___miltenyi_ = 'MACS Quant (Miltenyi)'
    maldi_synapt_g2_hdms___waters_ = 'MALDI SYNAPT G2 HDMS (Waters)'
    maldi_synapt_g2_ms___waters_ = 'MALDI SYNAPT G2 MS (Waters)'
    maldi_synapt_hdms___waters_ = 'MALDI SYNAPT HDMS (Waters)'
    maldi_synapt_ms___waters_ = 'MALDI SYNAPT MS (Waters)'
    maldi_micro_mx___waters_ = 'MALDI micro MX (Waters)'
    ma_xis___bruker_ = 'maXis (Bruker)'
    ma_xis_g4___bruker_ = 'maXis G4 (Bruker)'
    microflex_lt_maldi_tof_ms___bruker_ = 'microflex LT MALDI-TOF MS (Bruker)'
    microflex_lrf_maldi_tof_ms___bruker_ = 'microflex LRF MALDI-TOF MS (Bruker)'
    microflex_iii_maldi_tof_ms___bruker_ = 'microflex III MALDI-TOF MS (Bruker)'
    micr_otof_ii_esi_tof___bruker_ = 'micrOTOF II ESI TOF (Bruker)'
    micr_otof_q_ii_esi__qq_tof___bruker_ = 'micrOTOF-Q II ESI-Qq-TOF (Bruker)'
    microplate__alamar__blue__resazurin__colorimetric_method = (
        'microplate Alamar Blue (resazurin) colorimetric method'
    )
    mstation___jeol_ = 'Mstation (Jeol)'
    msq__plus___thermo__scientific_ = 'MSQ Plus (Thermo Scientific)'
    na_bsys = 'NABsys'
    nanophotonics__biosciences = 'Nanophotonics Biosciences'
    network__biosystems = 'Network Biosystems'
    nimblegen = 'Nimblegen'
    oxford__nanopore__technologies = 'Oxford Nanopore Technologies'
    pacific__biosciences = 'Pacific Biosciences'
    population__genetics__technologies = 'Population Genetics Technologies'
    q1000_gc__ultra_quad___jeol_ = 'Q1000GC UltraQuad (Jeol)'
    quattro_micro_api___waters_ = 'Quattro micro API (Waters)'
    quattro_micro_gc___waters_ = 'Quattro micro GC (Waters)'
    quattro__premier_xe___waters_ = 'Quattro Premier XE (Waters)'
    qstar__ab__sciex_ = 'QSTAR (AB Sciex)'
    reveo = 'Reveo'
    roche = 'Roche'
    seirad = 'Seirad'
    solari_x_hybrid__qq_ftms___bruker_ = 'solariX hybrid Qq-FTMS (Bruker)'
    somacount___bently__instruments_ = 'Somacount (Bently Instruments)'
    soma_scope___bently__instruments_ = 'SomaScope (Bently Instruments)'
    synapt_g2_hdms___waters_ = 'SYNAPT G2 HDMS (Waters)'
    synapt_g2_ms___waters_ = 'SYNAPT G2 MS (Waters)'
    synapt_hdms___waters_ = 'SYNAPT HDMS (Waters)'
    synapt_ms___waters_ = 'SYNAPT MS (Waters)'
    triple_tof_5600__ab__sciex_ = 'TripleTOF 5600 (AB Sciex)'
    tsq__quantum__ultra___thermo__scientific_ = 'TSQ Quantum Ultra (Thermo Scientific)'
    tsq__quantum__access___thermo__scientific_ = (
        'TSQ Quantum Access (Thermo Scientific)'
    )
    tsq__quantum__access_max___thermo__scientific_ = (
        'TSQ Quantum Access MAX (Thermo Scientific)'
    )
    tsq__quantum__discovery_max___thermo__scientific_ = (
        'TSQ Quantum Discovery MAX (Thermo Scientific)'
    )
    tsq__quantum_gc___thermo__scientific_ = 'TSQ Quantum GC (Thermo Scientific)'
    tsq__quantum_xls___thermo__scientific_ = 'TSQ Quantum XLS (Thermo Scientific)'
    tsq__vantage___thermo__scientific_ = 'TSQ Vantage (Thermo Scientific)'
    ultrafle_xtreme_maldi_tof_ms___bruker_ = 'ultrafleXtreme MALDI-TOF MS (Bruker)'
    visi_gen__biotechnologies = 'VisiGen Biotechnologies'
    xevo_g2_qtof___waters_ = 'Xevo G2 QTOF (Waters)'
    xevo_q_tof_ms___waters_ = 'Xevo QTof MS (Waters)'
    xevo_tq_ms___waters_ = 'Xevo TQ MS (Waters)'
    xevo_tq_s___waters_ = 'Xevo TQ-S (Waters)'
    other = 'Other'


class Biomedical(DataverseBase):
    design_type: Optional[Union[List, DesignType]] = Field(
        None,
        description='Design types that are based on the overall experimental design.',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyDesignType',
    )
    other_design_type: Optional[List] = Field(
        None,
        description='If Other was selected in Design Type, list any other design types that were used in this Dataset.',
        multiple=True,
        typeClass='primitive',
        typeName='studyOtherDesignType',
    )
    factor_type: Optional[Union[List, FactorType]] = Field(
        None,
        description='Factors used in the Dataset.',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyFactorType',
    )
    other_factor_type: Optional[List] = Field(
        None,
        description='If Other was selected in Factor Type, list any other factor types that were used in this Dataset.',
        multiple=True,
        typeClass='primitive',
        typeName='studyOtherFactorType',
    )
    organism: Optional[Union[List, Organism]] = Field(
        None,
        description='The taxonomic name of the organism used in the Dataset or from which the  starting biological material derives.',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyAssayOrganism',
    )
    other_organism: Optional[List] = Field(
        None,
        description='If Other was selected in Organism, list any other organisms that were used in this Dataset. Terms from the NCBI Taxonomy are recommended.',
        multiple=True,
        typeClass='primitive',
        typeName='studyAssayOtherOrganism',
    )
    measurement_type: Optional[Union[List, MeasurementType]] = Field(
        None,
        description='A term to qualify the endpoint, or what is being measured (e.g. gene expression profiling; protein identification).',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyAssayMeasurementType',
    )
    other_measurement_type: Optional[List] = Field(
        None,
        description='If Other was selected in Measurement Type, list any other measurement types that were used. Terms from NCBO Bioportal are recommended.',
        multiple=True,
        typeClass='primitive',
        typeName='studyAssayOtherMeasurmentType',
    )
    technology_type: Optional[Union[List, TechnologyType]] = Field(
        None,
        description='A term to identify the technology used to perform the measurement (e.g. DNA microarray; mass spectrometry).',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyAssayTechnologyType',
    )
    other_technology_type: Optional[List] = Field(
        None,
        description='If Other was selected in Technology Type, list any other technology types that were used in this Dataset.',
        multiple=True,
        typeClass='primitive',
        typeName='studyAssayOtherTechnologyType',
    )
    technology_platform: Optional[Union[List, TechnologyPlatform]] = Field(
        None,
        description='The manufacturer and name of the technology platform used in the assay (e.g. Bruker AVANCE).',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyAssayPlatform',
    )
    other_technology_platform: Optional[List] = Field(
        None,
        description='If Other was selected in Technology Platform, list any other technology platforms that were used in this Dataset.',
        multiple=True,
        typeClass='primitive',
        typeName='studyAssayOtherPlatform',
    )
    cell_type: Optional[List] = Field(
        None,
        description='The name of the cell line from which the source or sample derives.',
        multiple=True,
        typeClass='controlledVocabulary',
        typeName='studyAssayCellType',
    )
    _metadatablock_name: Optional[str] = 'biomedical'