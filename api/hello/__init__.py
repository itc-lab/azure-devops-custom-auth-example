import json

import logging

import azure.functions as func

import base64


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("Python HTTP trigger function processed a request.")

    name = req.params.get("name")
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get("name")

    if name:
        aadAccessToken = req.headers.get("X-MS-TOKEN-AAD-ACCESS-TOKEN")
        principalID = req.headers.get("X-MS-CLIENT-PRINCIPAL-ID")
        principalName = req.headers.get("X-MS-CLIENT-PRINCIPAL-NAME")
        idProviderId = req.headers.get("X-MS-CLIENT-PRINCIPAL-IDP")
        aadRefreshToken = req.headers.get("X-MS-TOKEN-AAD-REFRESH-TOKEN")
        aadIdToken = req.headers.get("X-MS-TOKEN-AAD-ID-TOKEN")

        clientPrincipal = req.headers.get("X-MS-CLIENT-PRINCIPAL")
        clientPrincipal = base64.b64decode(clientPrincipal)

        result = "\n"
        myDict = sorted(dict(req.headers))
        for key in myDict:
            result += f"{key} = {dict(req.headers)[key]}\n"

        return func.HttpResponse(
            json.dumps(
                {
                    "message": f"Hello, {name}. How are you ? Doing well ?"
                    f"\n\nHere is some data concerning your Client principal:"
                    f"\nThis is your X-MS-CLIENT-PRINCIPAL-ID: {principalID}"
                    f"\nThis is your X-MS-CLIENT-PRINCIPAL-NAME: {principalName}"
                    f"\nThis is your X-MS-CLIENT-PRINCIPAL-IDP: {idProviderId}"
                    f"\nThis is your X-MS-CLIENT-PRINCIPAL: {clientPrincipal}"
                    f"\n\nHere is some data concerning your AAD-token:"
                    f"\nThis is your X-MS-TOKEN-AAD-ID-TOKEN: {aadIdToken}"
                    f"\nThis is your X-MS-TOKEN-AAD-ACCESS-TOKEN: {aadAccessToken}"
                    f"\nThis is your X-MS-TOKEN-AAD-REFRESH-TOKEN: {aadRefreshToken}"
                    f"\n\n\nresult: {result}"
                }
            ),
            mimetype="application/json",
        )
    else:
        return func.HttpResponse(
            json.dumps(
                {
                    "message": "This HTTP triggered function executed successfully."
                    "Pass a name in the query string"
                    " or in the request body for a personalized response."
                }
            ),
            status_code=200,
            mimetype="application/json",
        )
