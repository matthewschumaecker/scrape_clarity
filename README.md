This is a program designed to scrape open.ai.com to create a data dictionary in JSON format of all of the Clarity tables listed here.


 {
        "table_name": "BAT_DB_MAIN",
        "table_description": "Stores unique values for the batch that do not change over time.",
        "columns": [
            {
                "column_name": "BATCH_NUMBER_ID",
                "column_data_type": "VARCHAR",
                "column_description": " The unique ID of the batch."
            },
            {
                "column_name": "BATCH_COMMENT_ID",
                "column_data_type": "VARCHAR",
                "column_description": " The unique ID for the comment on the batch."
            }
        ]
    },




Once the dictionary is created as 'clarity_data_dictionary.json', 'convert_to_text_dictionary.py' can be run to create a plain text version with following example format:


===============================================================================
Table: WOUND_THERAPY_TREAT_AUDIT

Description: This table stores audit trail data about wound therapy treatments that have been applied to a wound.

Columns:
  - IP_LDA_ID (VARCHAR):  The unique identifier for the wound.
  - LINE (INTEGER):  The line number for the information associated with this record. Multiple pieces of information can be associated with this record.
  - THERAPY_IP_LDA_ID (VARCHAR):  The previously documented wound therapy device that treated this wound.
  - TREATMENT_START_UTC_DTTM (DATETIME (UTC) ):  The previously documented treatment start instant
  - TREATMENT_END_UTC_DTTM (DATETIME (UTC) ):  The previously documented treatment end instant
  - USER_ID (VARCHAR):  The user who previously documented this data
  - USER_ID_NAME (VARCHAR):  The name of the user record. This name may be hidden.
  - ENTRY_UTC_DTTM (DATETIME (UTC) ):  The instant this data was previously documented at
  - EDITED_LINE (INTEGER):  The line number for the value documented before this line was entered, if this was not the first entry. Corresponds to the value of LINE for another row in WOUND_THERAPY_TREAT_AUDIT.
===============================================================================
prom
