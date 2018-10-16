"""A snapshot of current codenames.

Validated with the PermissionsInspector in tests and system checks.

"""

from edc_permissions.constants import (
    AUDITOR, LAB, EVERYONE, PII, ADMINISTRATION, PHARMACY,
    ACCOUNT_MANAGER, CLINIC, PII_VIEW, EXPORT)

from .group_names import TMG, RANDO


CODENAMES = {
    ACCOUNT_MANAGER: [
        'add_group',
        'add_permission',
        'add_user',
        'add_userprofile',
        'change_group',
        'change_permission',
        'change_user',
        'change_userprofile',
        'delete_group',
        'delete_permission',
        'delete_user',
        'delete_userprofile',
        'view_group',
        'view_permission',
        'view_user',
        'view_userprofile'],
    ADMINISTRATION: ['nav_administration'],
    AUDITOR: [
        'nav_lab_requisition',
        'nav_lab_section',
        'view_abnormalresultsreason',
        'view_action',
        'view_actionitem',
        'view_actionitemupdate',
        'view_actiontype',
        'view_aefollowup',
        'view_aeinitial',
        'view_aetmg',
        'view_aliquot',
        'view_amphotericinmisseddoses',
        'view_antibiotic',
        'view_antibiotictreatment',
        'view_appointment',
        'view_bloodresult',
        'view_box',
        'view_boxitem',
        'view_boxtype',
        'view_consignee',
        'view_cxrtype',
        'view_day14medication',
        'view_deathreport',
        'view_deathreporttmg',
        'view_education',
        'view_educationhoh',
        'view_fluconazolemisseddoses',
        'view_flucytosinemisseddoses',
        'view_followup',
        'view_followupdiagnoses',
        'view_historicalactionitem',
        'view_historicalactionitemupdate',
        'view_historicalaefollowup',
        'view_historicalaeinitial',
        'view_historicalaliquot',
        'view_historicalamphotericinmisseddoses',
        'view_historicalappointment',
        'view_historicalbloodresult',
        'view_historicalbox',
        'view_historicalboxitem',
        'view_historicalconsignee',
        'view_historicaldeathreport',
        'view_historicaleducation',
        'view_historicaleducationhoh',
        'view_historicalfluconazolemisseddoses',
        'view_historicalflucytosinemisseddoses',
        'view_historicalfollowup',
        'view_historicalfollowupdiagnoses',
        'view_historicallumbarpuncturecsf',
        'view_historicalmanifest',
        'view_historicalmedicalexpenses',
        'view_historicalmedicalexpensestwo',
        'view_historicalmedicalexpensestwodetail',
        'view_historicalmicrobiology',
        'view_historicalonschedule',
        'view_historicalonschedulew10',
        'view_historicalorder',
        'view_historicalpatienthistory',
        'view_historicalpkpdcrf',
        'view_historicalpkpdextrasamples',
        'view_historicalpreviousopportunisticinfection',
        'view_historicalprotocoldeviationviolation',
        'view_historicalradiology',
        'view_historicalrecurrencesymptom',
        'view_historicalresult',
        'view_historicalresultitem',
        'view_historicalshipper',
        'view_historicalsignificantdiagnoses',
        'view_historicalstudyterminationconclusion',
        'view_historicalstudyterminationconclusionw10',
        'view_historicalsubjectoffstudy',
        'view_historicalsubjectrequisition',
        'view_historicalsubjectscreening',
        'view_historicalsubjectvisit',
        'view_historicalweek16',
        'view_historicalweek2',
        'view_historicalweek4',
        'view_historicalweek4diagnoses',
        'view_infiltratelocation',
        'view_lab_aliquot_listboard',
        'view_lab_box_listboard',
        'view_lab_manifest_listboard',
        'view_lab_pack_listboard',
        'view_lab_process_listboard',
        'view_lab_receive_listboard',
        'view_lab_requisition_listboard',
        'view_lab_result_listboard',
        'view_lumbarpuncturecsf',
        'view_manifest',
        'view_manifestitem',
        'view_medicalexpenses',
        'view_medicalexpensestwo',
        'view_medicalexpensestwodetail',
        'view_medication',
        'view_meningitissymptom',
        'view_microbiology',
        'view_misseddoses',
        'view_neurological',
        'view_neurological',
        'view_onschedule',
        'view_onschedulew10',
        'view_order',
        'view_otherdrug',
        'view_panel',
        'view_patienthistory',
        'view_pkpdcrf',
        'view_pkpdextrasamples',
        'view_previousopportunisticinfection',
        'view_protocoldeviationviolation',
        'view_radiology',
        'view_recurrencesymptom',
        'view_reference',
        'view_result',
        'view_resultitem',
        'view_screening_listboard',
        'view_shipper',
        'view_significantdiagnoses',
        'view_significantnewdiagnosis',
        'view_studyterminationconclusion',
        'view_studyterminationconclusionw10',
        'view_subject_listboard',
        'view_subjectconsent',
        'view_subjectoffstudy',
        'view_subjectreconsent',
        'view_subjectrequisition',
        'view_subjectscreening',
        'view_subjectvisit',
        'view_symptom',
        'view_tmg_listboard',
        'view_week16',
        'view_week2',
        'view_week4',
        'view_week4diagnoses',
    ],
    CLINIC: [
        'add_abnormalresultsreason',
        'add_action',
        'add_actionitem',
        'add_actionitemupdate',
        'add_actiontype',
        'add_aefollowup',
        'add_aeinitial',
        'add_amphotericinmisseddoses',
        'add_antibiotic',
        'add_antibiotictreatment',
        'add_appointment',
        'add_bloodresult',
        'add_cxrtype',
        'add_day14medication',
        'add_deathreport',
        'add_education',
        'add_educationhoh',
        'add_fluconazolemisseddoses',
        'add_flucytosinemisseddoses',
        'add_followup',
        'add_followupdiagnoses',
        'add_infiltratelocation',
        'add_lumbarpuncturecsf',
        'add_medicalexpenses',
        'add_medicalexpensestwo',
        'add_medicalexpensestwodetail',
        'add_medication',
        'add_meningitissymptom',
        'add_microbiology',
        'add_misseddoses',
        'add_neurological',
        'add_neurological',
        'add_onschedule',
        'add_onschedulew10',
        'add_otherdrug',
        'add_patienthistory',
        'add_pkpdcrf',
        'add_pkpdextrasamples',
        'add_previousopportunisticinfection',
        'add_protocoldeviationviolation',
        'add_radiology',
        'add_recurrencesymptom',
        'add_reference',
        'add_significantdiagnoses',
        'add_significantnewdiagnosis',
        'add_studyterminationconclusion',
        'add_studyterminationconclusionw10',
        'add_subjectoffstudy',
        'add_subjectrequisition',
        'add_subjectvisit',
        'add_symptom',
        'add_week16',
        'add_week2',
        'add_week4',
        'add_week4diagnoses',
        'change_abnormalresultsreason',
        'change_action',
        'change_actionitem',
        'change_actionitemupdate',
        'change_actiontype',
        'change_aefollowup',
        'change_aeinitial',
        'change_amphotericinmisseddoses',
        'change_antibiotic',
        'change_antibiotictreatment',
        'change_appointment',
        'change_bloodresult',
        'change_cxrtype',
        'change_day14medication',
        'change_deathreport',
        'change_education',
        'change_educationhoh',
        'change_fluconazolemisseddoses',
        'change_flucytosinemisseddoses',
        'change_followup',
        'change_followupdiagnoses',
        'change_infiltratelocation',
        'change_lumbarpuncturecsf',
        'change_medicalexpenses',
        'change_medicalexpensestwo',
        'change_medicalexpensestwodetail',
        'change_medication',
        'change_meningitissymptom',
        'change_microbiology',
        'change_misseddoses',
        'change_neurological',
        'change_neurological',
        'change_onschedule',
        'change_onschedulew10',
        'change_otherdrug',
        'change_patienthistory',
        'change_pkpdcrf',
        'change_pkpdextrasamples',
        'change_previousopportunisticinfection',
        'change_protocoldeviationviolation',
        'change_radiology',
        'change_recurrencesymptom',
        'change_reference',
        'change_significantdiagnoses',
        'change_significantnewdiagnosis',
        'change_studyterminationconclusion',
        'change_studyterminationconclusionw10',
        'change_subjectoffstudy',
        'change_subjectrequisition',
        'change_subjectvisit',
        'change_symptom',
        'change_week16',
        'change_week2',
        'change_week4',
        'change_week4diagnoses',
        'delete_abnormalresultsreason',
        'delete_action',
        'delete_actionitem',
        'delete_actionitemupdate',
        'delete_actiontype',
        'delete_aefollowup',
        'delete_aeinitial',
        'delete_amphotericinmisseddoses',
        'delete_antibiotic',
        'delete_antibiotictreatment',
        'delete_bloodresult',
        'delete_cxrtype',
        'delete_day14medication',
        'delete_deathreport',
        'delete_education',
        'delete_educationhoh',
        'delete_fluconazolemisseddoses',
        'delete_flucytosinemisseddoses',
        'delete_followup',
        'delete_followupdiagnoses',
        'delete_infiltratelocation',
        'delete_lumbarpuncturecsf',
        'delete_medicalexpenses',
        'delete_medicalexpensestwo',
        'delete_medicalexpensestwodetail',
        'delete_medication',
        'delete_meningitissymptom',
        'delete_microbiology',
        'delete_misseddoses',
        'delete_neurological',
        'delete_neurological',
        'delete_onschedule',
        'delete_onschedulew10',
        'delete_otherdrug',
        'delete_patienthistory',
        'delete_pkpdcrf',
        'delete_pkpdextrasamples',
        'delete_previousopportunisticinfection',
        'delete_protocoldeviationviolation',
        'delete_radiology',
        'delete_recurrencesymptom',
        'delete_reference',
        'delete_significantdiagnoses',
        'delete_significantnewdiagnosis',
        'delete_studyterminationconclusion',
        'delete_studyterminationconclusionw10',
        'delete_subjectoffstudy',
        'delete_subjectrequisition',
        'delete_subjectvisit',
        'delete_symptom',
        'delete_week16',
        'delete_week2',
        'delete_week4',
        'delete_week4diagnoses',
        'nav_lab_requisition',
        'nav_lab_section',
        'nav_screening_section',
        'nav_subject_section',
        'view_abnormalresultsreason',
        'view_action',
        'view_actionitem',
        'view_actionitemupdate',
        'view_actiontype',
        'view_aefollowup',
        'view_aeinitial',
        'view_aetmg',
        'view_amphotericinmisseddoses',
        'view_antibiotic',
        'view_antibiotictreatment',
        'view_appointment',
        'view_bloodresult',
        'view_cxrtype',
        'view_day14medication',
        'view_deathreport',
        'view_education',
        'view_educationhoh',
        'view_fluconazolemisseddoses',
        'view_flucytosinemisseddoses',
        'view_followup',
        'view_followupdiagnoses',
        'view_historicalactionitem',
        'view_historicalactionitemupdate',
        'view_historicalaefollowup',
        'view_historicalaeinitial',
        'view_historicalamphotericinmisseddoses',
        'view_historicalappointment',
        'view_historicalbloodresult',
        'view_historicaldeathreport',
        'view_historicaleducation',
        'view_historicaleducationhoh',
        'view_historicalfluconazolemisseddoses',
        'view_historicalflucytosinemisseddoses',
        'view_historicalfollowup',
        'view_historicalfollowupdiagnoses',
        'view_historicallumbarpuncturecsf',
        'view_historicalmedicalexpenses',
        'view_historicalmedicalexpensestwo',
        'view_historicalmedicalexpensestwodetail',
        'view_historicalmicrobiology',
        'view_historicalonschedule',
        'view_historicalonschedulew10',
        'view_historicalpatienthistory',
        'view_historicalpkpdcrf',
        'view_historicalpkpdextrasamples',
        'view_historicalpreviousopportunisticinfection',
        'view_historicalprotocoldeviationviolation',
        'view_historicalradiology',
        'view_historicalrecurrencesymptom',
        'view_historicalsignificantdiagnoses',
        'view_historicalstudyterminationconclusion',
        'view_historicalstudyterminationconclusionw10',
        'view_historicalsubjectoffstudy',
        'view_historicalsubjectrequisition',
        'view_historicalsubjectvisit',
        'view_historicalweek16',
        'view_historicalweek2',
        'view_historicalweek4',
        'view_historicalweek4diagnoses',
        'view_infiltratelocation',
        'view_lab_aliquot_listboard',
        'view_lab_box_listboard',
        'view_lab_manifest_listboard',
        'view_lab_pack_listboard',
        'view_lab_process_listboard',
        'view_lab_receive_listboard',
        'view_lab_requisition_listboard',
        'view_lab_result_listboard',
        'view_lumbarpuncturecsf',
        'view_medicalexpenses',
        'view_medicalexpensestwo',
        'view_medicalexpensestwodetail',
        'view_medication',
        'view_meningitissymptom',
        'view_microbiology',
        'view_misseddoses',
        'view_neurological',
        'view_neurological',
        'view_onschedule',
        'view_onschedulew10',
        'view_otherdrug',
        'view_patienthistory',
        'view_pkpdcrf',
        'view_pkpdextrasamples',
        'view_previousopportunisticinfection',
        'view_protocoldeviationviolation',
        'view_radiology',
        'view_recurrencesymptom',
        'view_reference',
        'view_screening_listboard',
        'view_significantdiagnoses',
        'view_significantnewdiagnosis',
        'view_studyterminationconclusion',
        'view_studyterminationconclusionw10',
        'view_subject_listboard',
        'view_subjectoffstudy',
        'view_subjectrequisition',
        'view_subjectvisit',
        'view_symptom',
        'view_tmg_listboard',
        'view_week16',
        'view_week2',
        'view_week4',
        'view_week4diagnoses',
    ],
    EVERYONE: [
        'view_group',
        'view_logentry',
        'view_permission',
        'view_site',
        'view_user',
        'view_userprofile'],
    LAB: [
        'add_aliquot',
        'add_box',
        'add_boxitem',
        'add_boxtype',
        'add_consignee',
        'add_manifest',
        'add_manifestitem',
        'add_order',
        'add_panel',
        'add_result',
        'add_resultitem',
        'add_shipper',
        'change_aliquot',
        'change_box',
        'change_boxitem',
        'change_boxtype',
        'change_consignee',
        'change_manifest',
        'change_manifestitem',
        'change_order',
        'change_panel',
        'change_result',
        'change_resultitem',
        'change_shipper',
        'change_subjectrequisition',
        'delete_aliquot',
        'delete_box',
        'delete_boxitem',
        'delete_boxtype',
        'delete_consignee',
        'delete_manifest',
        'delete_manifestitem',
        'delete_order',
        'delete_panel',
        'delete_result',
        'delete_resultitem',
        'delete_shipper',
        'nav_lab_aliquot',
        'nav_lab_manifest',
        'nav_lab_pack',
        'nav_lab_process',
        'nav_lab_receive',
        'nav_lab_requisition',
        'nav_lab_section',
        'nav_subject_section',
        'view_aliquot',
        'view_box',
        'view_boxitem',
        'view_boxtype',
        'view_consignee',
        'view_historicalaliquot',
        'view_historicalbox',
        'view_historicalboxitem',
        'view_historicalconsignee',
        'view_historicalmanifest',
        'view_historicalorder',
        'view_historicalresult',
        'view_historicalresultitem',
        'view_historicalshipper',
        'view_lab_aliquot_listboard',
        'view_lab_box_listboard',
        'view_lab_manifest_listboard',
        'view_lab_pack_listboard',
        'view_lab_process_listboard',
        'view_lab_receive_listboard',
        'view_lab_requisition_listboard',
        'view_lab_result_listboard',
        'view_manifest',
        'view_manifestitem',
        'view_order',
        'view_panel',
        'view_result',
        'view_resultitem',
        'view_screening_listboard',
        'view_shipper',
        'view_subject_listboard',
        'view_subjectrequisition',
    ],
    PHARMACY: ['add_appointment',
               'add_dispenseditem',
               'add_dosageguideline',
               'add_medication',
               'add_prescription',
               'add_prescriptionitem',
               'change_appointment',
               'change_dispenseditem',
               'change_dosageguideline',
               'change_medication',
               'change_prescription',
               'change_prescriptionitem',
               'delete_appointment',
               'delete_dispenseditem',
               'delete_dosageguideline',
               'delete_medication',
               'delete_prescription',
               'delete_prescriptionitem',
               'nav_pharmacy_section',
               'view_appointment',
               'view_dispenseditem',
               'view_dosageguideline',
               'view_medication',
               'view_prescription',
               'view_prescriptionitem'],
    PII: [
        'add_subjectconsent',
        'add_subjectlocator',
        'add_subjectreconsent',
        'add_subjectscreening',
        'change_subjectconsent',
        'change_subjectlocator',
        'change_subjectreconsent',
        'change_subjectscreening',
        'delete_subjectconsent',
        'delete_subjectlocator',
        'delete_subjectreconsent',
        'delete_subjectscreening',
        'display_dob',
        'display_firstname',
        'display_identity',
        'display_initials',
        'display_lastname',
        'view_registeredsubject',
        'view_subjectconsent',
        'view_subjectlocator',
        'view_subjectreconsent',
        'view_subjectscreening'],
    PII_VIEW: [
        'display_dob',
        'display_firstname',
        'display_identity',
        'display_initials',
        'display_lastname',
        'view_registeredsubject',
        'view_subjectconsent',
        'view_subjectlocator',
        'view_subjectreconsent',
        'view_subjectscreening'],
    RANDO: ['display_randomization'],
    TMG: [
        'add_action',
        'add_actionitem',
        'add_actionitemupdate',
        'add_actiontype',
        'add_aetmg',
        'add_appointment',
        'add_deathreporttmg',
        'add_reference',
        'change_action',
        'change_actionitem',
        'change_actionitemupdate',
        'change_actiontype',
        'change_aetmg',
        'change_appointment',
        'change_deathreporttmg',
        'change_reference',
        'delete_action',
        'delete_actionitem',
        'delete_actionitemupdate',
        'delete_actiontype',
        'delete_aetmg',
        'delete_appointment',
        'delete_deathreporttmg',
        'delete_reference',
        'nav_tmg_section',
        'view_abnormalresultsreason',
        'view_action',
        'view_actionitem',
        'view_actionitemupdate',
        'view_actiontype',
        'view_aefollowup',
        'view_aeinitial',
        'view_aetmg',
        'view_amphotericinmisseddoses',
        'view_antibiotic',
        'view_antibiotictreatment',
        'view_appointment',
        'view_bloodresult',
        'view_cxrtype',
        'view_day14medication',
        'view_deathreport',
        'view_deathreporttmg',
        'view_education',
        'view_educationhoh',
        'view_fluconazolemisseddoses',
        'view_flucytosinemisseddoses',
        'view_followup',
        'view_followupdiagnoses',
        'view_historicalactionitem',
        'view_historicalactionitemupdate',
        'view_historicalaefollowup',
        'view_historicalaeinitial',
        'view_historicalamphotericinmisseddoses',
        'view_historicalbloodresult',
        'view_historicaleducation',
        'view_historicaleducationhoh',
        'view_historicalfluconazolemisseddoses',
        'view_historicalflucytosinemisseddoses',
        'view_historicalfollowup',
        'view_historicalfollowupdiagnoses',
        'view_historicallumbarpuncturecsf',
        'view_historicalmedicalexpenses',
        'view_historicalmedicalexpensestwo',
        'view_historicalmedicalexpensestwodetail',
        'view_historicalmicrobiology',
        'view_historicalpatienthistory',
        'view_historicalpkpdcrf',
        'view_historicalpkpdextrasamples',
        'view_historicalpreviousopportunisticinfection',
        'view_historicalradiology',
        'view_historicalrecurrencesymptom',
        'view_historicalsignificantdiagnoses',
        'view_historicalsubjectrequisition',
        'view_historicalsubjectvisit',
        'view_historicalweek16',
        'view_historicalweek2',
        'view_historicalweek4',
        'view_historicalweek4diagnoses',
        'view_infiltratelocation',
        'view_lab_aliquot_listboard',
        'view_lab_box_listboard',
        'view_lab_manifest_listboard',
        'view_lab_pack_listboard',
        'view_lab_process_listboard',
        'view_lab_receive_listboard',
        'view_lab_requisition_listboard',
        'view_lab_result_listboard',
        'view_lumbarpuncturecsf',
        'view_medicalexpenses',
        'view_medicalexpensestwo',
        'view_medicalexpensestwodetail',
        'view_medication',
        'view_meningitissymptom',
        'view_microbiology',
        'view_misseddoses',
        'view_neurological',
        'view_neurological',  # from two different apps
        'view_otherdrug',
        'view_patienthistory',
        'view_pkpdcrf',
        'view_pkpdextrasamples',
        'view_previousopportunisticinfection',
        'view_radiology',
        'view_recurrencesymptom',
        'view_reference',
        'view_screening_listboard',
        'view_significantdiagnoses',
        'view_significantnewdiagnosis',
        'view_subject_listboard',
        'view_subjectrequisition',
        'view_subjectvisit',
        'view_symptom',
        'view_tmg_listboard',
        'view_week16',
        'view_week2',
        'view_week4',
        'view_week4diagnoses',
    ],
    EXPORT: [
        'add_datarequest',
        'add_datarequesthistory',
        'add_exportreceipt',
        'add_filehistory',
        'add_objecthistory',
        'add_plan',
        'add_uploadexportreceiptfile',
        'change_datarequest',
        'change_datarequesthistory',
        'change_exportreceipt',
        'change_filehistory',
        'change_objecthistory',
        'change_plan',
        'change_uploadexportreceiptfile',
        'delete_datarequest',
        'delete_datarequesthistory',
        'delete_exportreceipt',
        'delete_filehistory',
        'delete_objecthistory',
        'delete_plan',
        'delete_uploadexportreceiptfile',
        'view_datarequest',
        'view_datarequesthistory',
        'view_exportreceipt',
        'view_filehistory',
        'view_historicaldatarequest',
        'view_historicalexportreceipt',
        'view_historicalfilehistory',
        'view_historicalobjecthistory',
        'view_historicalplan',
        'view_objecthistory',
        'view_plan',
        'view_uploadexportreceiptfile',
    ],
}
