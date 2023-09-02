import openai


def GetResponse(text):
    try:
        openai.api_key = "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"
        result = openai.Completion.create(model = "text-davinci-003",
                                          prompt = text,
                                          n = 1,
                                          max_tokens = 500
                                          )
        response = result.choices[0].text
        return response
    except Exception as exception:
        print(exception)
        return "error"