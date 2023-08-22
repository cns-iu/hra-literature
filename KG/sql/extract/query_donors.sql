\t
\a
\o donors_metadata.json
SELECT
  jsonb_strip_nulls(ROW_TO_JSON(ROW)::jsonb) AS json_data
FROM (
  SELECT
    '#Donor/' || normalize_id(donor_id) AS "@id",
    'Donor' AS "@type",
    donor_id AS identifier,
    'Donor' AS "role",
    sex,
    age,
    death_event AS "deathEvent",
    source,
    age_unit AS "ageUnit",
    weight,
    weight_unit AS "weightUnit",
    height,
    height_unit AS "heightUnit",
    race,
    body_mass_index AS "bodyMassIndex",
    body_mass_index_unit AS "bodyMassIndexUnit",
    blood_type AS "bloodType",
    rh_blood_group AS "rhBloodGroup",
    rh_factor AS "rhFactor",
    kidney_donor_profile_index AS "kidneyDonorProfileIndex",
    kidney_donor_profile_index_unit AS "kidneyDonorProfileIndexUnit",
    cause_of_death AS "causeOfDeath",
    medical_history AS "medicalHistory",
    mechanism_of_injury AS "mechanismOfInjury",
    social_history AS "socialHistory",
    sex_ontotlogy AS "sexOntotlogy",
    race_ontotlogy AS "raceOntotlogy"
  FROM
    donor_metadata)
  ROW
