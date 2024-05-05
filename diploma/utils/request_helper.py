import json
import logging
import os

import allure
import requests
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

from diploma.pages.api.token import api_token

load_dotenv()
api_url = os.getenv('API_URL')
headers = {
    'User-Agent': os.getenv('API_USER_AGENT'),
    "Authorization": "Bearer " + api_token(),
    "Content-Type": "application/json"
}


def api_post(url, **kwargs):
    with allure.step("API Request POST"):
        result = requests.post(url=api_url + url, headers=headers, **kwargs)

        allure.attach(
            body=result.request.url,
            name="Request url",
            attachment_type=AttachmentType.TEXT,
        )
        allure.attach(
            body=result.text,
            name="Response",
            attachment_type=AttachmentType.TEXT, extension="txt"
        )
        allure.attach(
            body=str(result.cookies),
            name="Cookies",
            attachment_type=AttachmentType.TEXT, extension="txt"
        )
        allure.attach(
            body=json.dumps(result.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )

        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)

    return result


def api_get(url, **kwargs):
    with allure.step("API Request GET"):
        result = requests.get(url=api_url + url, headers=headers, **kwargs)

        allure.attach(
            body=result.request.url,
            name="Request url",
            attachment_type=AttachmentType.TEXT,
        )
        allure.attach(
            body=result.text,
            name="Response",
            attachment_type=AttachmentType.TEXT, extension="txt"
        )
        allure.attach(
            body=str(result.cookies),
            name="Cookies",
            attachment_type=AttachmentType.TEXT, extension="txt"
        )
        allure.attach(
            body=json.dumps(result.request.body, indent=4, ensure_ascii=True),
            name="Request body",
            attachment_type=AttachmentType.JSON,
            extension="json",
        )
        allure.attach(
            body=json.dumps(result.json(), indent=4, ensure_ascii=True),
            name="Response",
            attachment_type=AttachmentType.JSON, extension="json"
        )

        logging.info(result.request.url)
        logging.info(result.status_code)
        logging.info(result.text)

    return result
