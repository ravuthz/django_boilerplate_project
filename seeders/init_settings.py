from apps.settings.models import Setting, SettingItem

social = Setting.objects.create(
    name="social_media",
    desc="Social Media"
)

contact = Setting.objects.create(
    name="contact",
    desc="Contact"
)

open_hours = Setting.objects.create(
    name="open_hour",
    desc="Open Hours"
)

SettingItem.objects.create(
    setting=social,
    name="facebook",
    desc="Facebook",
    value="https://facebook.com/ravuthz"
)

SettingItem.objects.create(
    setting=social,
    name="twitter",
    desc="Twitter",
    value="https://twitter.com/vutyo"
)

SettingItem.objects.create(
    setting=contact,
    name="phone",
    desc="Phone Number",
    value="+855964577770"
)

SettingItem.objects.create(
    setting=contact,
    name="email",
    desc="Email Address",
    value="ravuthz@gmail.com"
)

SettingItem.objects.create(
    setting=contact,
    name="messager",
    desc="Messager",
    value="https://m.me/ravuthz"
)

SettingItem.objects.create(
    setting=contact,
    name="telegram",
    desc="Telegram",
    value="https://t.me/ravuthz"
)

# 24h * 7days = 168h
SettingItem.objects.create(
    setting=open_hours,
    name="24_7",
    desc="24H/7days",
    value="168"
)

# 8h * 7days = 40h
SettingItem.objects.create(
    setting=open_hours,
    name="8_7",
    desc="Working Days - 8h/Mon-Fri",
    value="40"
)

# 24h * 2days = 48h
SettingItem.objects.create(
    setting=open_hours,
    name="24_2",
    desc="Weekend - 24h/Sat-Sun",
    value="48"
)
