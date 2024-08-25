This is a program designed to scrape open.ai.com to create a data dictionary in JSON format of all of the Clarity tables listed here.

For example:

{
        "table_name": "ACIB_MISC_HD_INF",
        "table_description": "This table stores the extra information gathered by Help Desk messages.",
        "columns": [
            {
                "column name": "MSG_ID",
                "column data type": "VARCHAR",
                "column description": " The unique identifier for the task record."
            },
            {
                "column name": "LINE",
                "column data type": "INTEGER",
                "column description": " The line number for the information associated with this record. Multiple pieces of information can be associated with this record."
            },
            {
                "column name": "MISC_HELPDESK_INF",
                "column data type": "VARCHAR",
                "column description": " Stores the extra information gathered by Help Desk messages."
            },
            {
                "column name": "PAT_INF_YN",
                "column data type": "VARCHAR",
                "column description": " Indicates whether help desk extra information is patient specific."
            },
            {
                "column name": "HELP_DESK_INF_LABEL",
                "column data type": "VARCHAR",
                "column description": " The label for extra information stored in a help desk message."
            }
        ]
    },