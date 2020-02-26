import re, datetime
from linebot.models import (
    TemplateSendMessage, ButtonsTemplate, DatetimePickerTemplateAction, PostbackAction
)

def arrival_datepicker():
    now_date = datetime.datetime.now().isoformat()
    regex  = re.findall(r"[0-9]{4}-[0-9]{2}-[0-9]{2}|[0-9]{2}:[0-9]{2}", now_date)
    tstr = regex[0] + "T" + regex[1]
    # Signatureチェック等
    date_picker = TemplateSendMessage(
        alt_text="予定日を設定",
        template=ButtonsTemplate(
            text="予定日を設定",
            title="集合日時を設定",
            actions=[
                DatetimePickerTemplateAction(
                    label="設定",
                    data="action=buy&itemid=2&mode=datetime",
                    mode="datetime",
                    initial=tstr,
                    min=tstr,
                    max="2099-12-31T23:59"
                )
            ]
        )
    )

    return date_picker

def arrival_button():
    return TemplateSendMessage(
            alt_text="到着ボタン",
            template=ButtonsTemplate(
                # thumbnail_image_url="https://example.com/image.jpg",
                title="Menu", text="Please select",
                actions=[
                    PostbackAction(
                        label="到着", display_text="到着",
                        data="data not served"
                    )
                ]
            )
        )
