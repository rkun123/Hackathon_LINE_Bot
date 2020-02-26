def templateMessageGenerator():
    # Signatureチェック等
    date_picker = TemplateSendMessage(
        alt_text='予定日を設定',
        template=ButtonsTemplate(
            text='予定日を設定',
            title='YYYY-MM-dd H:M',
            actions=[
                DatetimePickerTemplateAction(
                    label='設定',
                    data='action=buy&itemid=2&mode=datetime',
                    mode='datetime',
                    initial='2017-04-01T10:00',
                    min='2017-04-01T00:00',
                    max='2099-12-31T23:59'
                )
            ]
        )
    )

    return date_picker
