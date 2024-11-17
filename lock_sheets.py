from tracemalloc import start
from typing import Literal
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

# Replace with your own details
SERVICE_ACCOUNT_FILE = "credentials.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = "1QWQpMMJb4NAzRciXlI1F6C9rz_diqEwu0oNa6oGt2z4"
DAILY_SHEET_ID = (
    "1793215811"  # Replace with the correct sheet ID (get it from the API or UI)
)
WEEKLY_SHEET_ID = (
    "1824706805"  # Replace with the correct sheet ID (get it from the API or UI)
)
MONTHLY_SHEET_ID = (
    "169913752"  # Replace with the correct sheet ID (get it from the API or UI)
)


sheets = [
    {
        "id": "1QWQpMMJb4NAzRciXlI1F6C9rz_diqEwu0oNa6oGt2z4",
        "end_row_index": 23,
    },
    {
        "id": "1ikcVP8cd73pYy5LR8HOtu8BtZfCCUWJpb98suuwHkxo",
        "end_row_index": 24,
    },
    {
        "id": "1f1Ve-GuPnSizx-gZsm2mjI6f4U4rbC7Bw8pCm8fde4U",
        "end_row_index": 22,
    },
    {
        "id": "156e1Vr-DNWgVSeyciv0Wm5K-8EerzLMvtVJwchEX9FI",
        "end_row_index": 22,
    },
    {
        "id": "1DpqcwtE6ewqLNYjXPVh9yK6nF68PxAuTPjUyqHQi8gk",
        "end_row_index": 22,
    },
    {
        "id": "1tuOjbPy0h5y7F4L_MXlWVy8CRZxWK8OkAqqR_mIsMgM",
        "end_row_index": 24,
    },
    {
        "id": "1qLK5sbaK103-S91ZN9bw2D6xn9uvdOLepHYTLuvtQWo",
        "end_row_index": 25,
    },
    {
        "id": "1GO_ANCNewoTMjDoHgxBMiQR2p5GJOOFfB1GH5msMzPQ",
        "end_row_index": 23,
    },
    {
        "id": "1RDFB-LYCxuWCley02xJlq-Qy4bGAzOapedUGh5CHyXg",
        "end_row_index": 22,
    },
    {
        "id": "1b8PG9tm09M93Dl40C4DNvhfrBPZPVMINMevss0bKsFc",
        "end_row_index": 23,
    },
    {
        "id": "1Vk89XNDGc4UlCyoeDgVXl6wcQg6fL3zlmdeqU8SRG6A",
        "end_row_index": 21,
    },
    {
        "id": "1nMS5l3A7zQjxTixKfF4S4IWD4ijOi_c5X_JiOzDjQ4s",
        "end_row_index": 25,
    },
]


def lock_range(
    spreadsheet_id: int,
    end_row_index: int,
    start_column_index: int,
    sheet: Literal["daily", "weekly", "monthly"] = "daily",
):
    # Authenticate and build the service
    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build("sheets", "v4", credentials=creds)

    if sheet == "daily":
        sheet_id = DAILY_SHEET_ID
    elif sheet == "weekly":
        sheet_id = WEEKLY_SHEET_ID
    else:
        sheet_id = MONTHLY_SHEET_ID

    requests = [
        {
            "addProtectedRange": {
                "protectedRange": {
                    "range": {
                        "sheetId": sheet_id,
                        "startRowIndex": 2,  # Row index starts from 0
                        "endRowIndex": end_row_index,  # Exclusive
                        "startColumnIndex": start_column_index,  # Column index starts from 0
                        "endColumnIndex": start_column_index + 2,  # Exclusive
                    },
                    "description": "Locking this range",
                    "warningOnly": False,  # Set to True if you just want to show warnings
                    "editors": {
                        "users": [
                            "test-account@united-electron-441922-e4.iam.gserviceaccount.com",
                            "daviddawoud022@gmail.com",
                            "demiananasr61@gmail.com",
                            "demiananasr92@gmail.com",
                        ],  # Add emails if specific users can edit
                    },
                }
            }
        }
    ]

    # Execute the batch update
    body = {"requests": requests}

    try:
        response = (
            service.spreadsheets()
            .batchUpdate(spreadsheetId=spreadsheet_id, body=body)
            .execute()
        )

        print("Range locked successfully!")
        print(response)
    except Exception as e:
        print(f"An error occurred: {e}")


# def unlock_sheet(
#     spreadsheet_id: int,
#     end_row_index: int,
#     start_column_index: int,
#     sheet: Literal["daily", "weekly", "monthly"] = "daily",
# ):
#     # Authenticate and build the service
#     creds = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
#     service = build("sheets", "v4", credentials=creds)


#     if sheet == "daily":
#         sheet_id = DAILY_SHEET_ID
#         local_start_column_index = 1
#         local_end_column_index = 15
#     elif sheet == "weekly":
#         sheet_id = WEEKLY_SHEET_ID
#         local_start_column_index = start_column_index
#         local_end_column_index = start_column_index+2
#     else:
#         sheet_id = MONTHLY_SHEET_ID
#         local_start_column_index = start_column_index
#         local_end_column_index = start_column_index+2


#     requests = [
#         {
#             "addProtectedRange": {
#                 "protectedRange": {
#                     "range": {
#                         "sheetId": sheet_id,
#                         "startRowIndex": 2,  # Row index starts from 0
#                         "endRowIndex": end_row_index,  # Exclusive
#                         "startColumnIndex": local_start_column_index,  # Column index starts from 0
#                         "endColumnIndex": local_end_column_index,  # Exclusive
#                     },
#                     "description": "Locking this range",
#                     "warningOnly": False,  # Set to True if you just want to show warnings
#                     "editors": {
#                         "users": [
#                             "test-account@united-electron-441922-e4.iam.gserviceaccount.com",
#                             "daviddawoud022@gmail.com",
#                             "demiananasr61@gmail.com",
#                             "demiananasr92@gmail.com",
#                         ],  # Add emails if specific users can edit
#                     },
#                 }
#             }
#         }
#     ]

#     # Execute the batch update
#     body = {"requests": requests}

#     try:
#         response = (
#             service.spreadsheets()
#             .batchUpdate(spreadsheetId=spreadsheet_id, body=body)
#             .execute()
#         )

#         print("Range locked successfully!")
#         print(response)
#     except Exception as e:
#         print(f"An error occurred: {e}")


def lock_day(day: int):
    for i in range(len(sheets)):
        # Run the function
        lock_range(
            start_column_index=((day - 1) * 2) + 1,
            end_row_index=sheets[i]["end_row_index"],
            spreadsheet_id=sheets[i]["id"],
        )


# TODO: Add a function for unlocking all

day = input("Enter which day to lock (Friday = 1, Saturday = 2, etc.): ")

lock_day(int(day))

print("All ranges locked successfully!")
