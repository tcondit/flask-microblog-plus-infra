from app import app
from flask_babel import _
import json
import requests


# f"https://translator0.cognitiveservices.azure.com/Translate?text={text}&from={source_language}&to={dest_language}",
#      -H "Ocp-Apim-Subscription-Region:canadacentral" \
def translate(text, source_language, dest_language):
    if "MS_TRANSLATOR_KEY" not in app.config or not app.config["MS_TRANSLATOR_KEY"]:
        return _("Error: the translation service is not configured.")
    auth = {
        "Ocp-Apim-Subscription-Key": app.config["MS_TRANSLATOR_KEY"],
        "Ocp-Apim-Subscription-Region": "canadacentral",
    }
    r = requests.get(
        f"https://api.microsofttranslator.com/v2/Ajax.svc/Translate?text={text}&from={source_language}&to={dest_language}",
        headers=auth,
    )
    if r.status_code != 200:
        return _("Error: the translation service failed.")
    return json.loads(r.content.decode("utf-8-sig"))
